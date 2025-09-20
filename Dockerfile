# Multi-stage build for pdf-reader-mcp
FROM python:3.11-slim as builder

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock* ./

# Install dependencies
RUN uv sync --no-dev

# Copy source code
COPY src/ ./src/
COPY README.md LICENSE ./

# Build the package
RUN uv build

# Production stage
FROM python:3.11-slim as production

LABEL maintainer="tsaol <tsaol@outlook.com>"
LABEL description="A simplified Python MCP server for reading PDF files"
LABEL version="0.1.0"

# Create non-root user
RUN useradd --create-home --shell /bin/bash --user-group pdfuser

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy built package and install
COPY --from=builder /app/dist/*.whl ./
RUN uv pip install --system *.whl && rm *.whl

# Copy source code (needed for MCP server)
COPY --from=builder /app/src/ ./src/
COPY --from=builder /app/README.md /app/LICENSE ./

# Create directory for PDF files and change ownership
RUN mkdir -p /app/pdfs && chown -R pdfuser:pdfuser /app

# Switch to non-root user
USER pdfuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD timeout 5s python -c "import sys; sys.path.insert(0, '/app'); from src.main import server; print('OK')" || exit 1

# Environment variables
ENV PYTHONPATH="/app"
ENV PYTHONUNBUFFERED=1
ENV LOG_LEVEL=INFO

# Expose port (although MCP typically uses stdio)
EXPOSE 8000

# Default command
CMD ["python", "src/main.py"]

# Alternative commands for different use cases:
# For development with volume mount:
# docker run -v $(pwd)/pdfs:/app/pdfs pdf-reader-mcp

# For production with custom config:
# docker run -e LOG_LEVEL=DEBUG pdf-reader-mcp

# For testing:
# docker run --rm pdf-reader-mcp python tests/simple_test.py