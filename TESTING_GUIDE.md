# 测试指南 - tsaol-pdf-reader-mcp

## 📋 测试级别

### 1. 🧪 基础功能测试 (推荐首先运行)

```bash
python3 simple_test.py
```

**测试内容：**
- ✅ 模块导入
- ✅ 路径安全检查
- ✅ 数据模型验证
- ✅ 工具函数

**预期结果：**
```
🧪 Running simple tests for tsaol-pdf-reader-mcp
✅ Models imported successfully
✅ Utils imported successfully
✅ Safe path resolved
✅ Path traversal prevented
✅ Valid request created
✅ Invalid request caught
✅ Error formatting
✅ Text cleaning
✅ Text truncation
✨ Simple tests completed!
```

### 2. 🔧 MCP服务器测试

```bash
python3 test_server.py
```

**测试内容：**
- ✅ MCP服务器组件导入
- ✅ 工具列表功能
- ✅ 工具调用功能
- ✅ 参数验证
- 🔒 安全路径检查

**预期结果：**
```
🧪 Testing MCP Server Functionality
✅ MCP server components imported successfully
✅ Found 1 tool(s)
✅ Tool call completed
✅ Proper validation error returned
✅ Valid request processed
✅ Proper file not found error
📊 Test Results: 3/4 passed
```

### 3. 🌐 PDF处理测试 (需要网络)

```bash
python3 test_with_pdf.py
```

**测试内容：**
- 📡 URL PDF下载和处理
- 📄 多源PDF处理
- 🎯 页面选择功能

### 4. 🖱️ 交互式测试

```bash
python3 manual_test.py
```

**提供菜单选择：**
1. 测试无效参数
2. 测试文件不存在
3. 测试URL PDF
4. 测试自定义PDF文件
5. 退出

### 5. 🚀 MCP协议测试

```bash
# 启动MCP服务器
python3 src/main.py
```

服务器将等待MCP客户端连接。

## 🎯 Amazon Q CLI集成测试

### 配置Amazon Q CLI

1. **安装依赖：**
   ```bash
   pip install -r requirements.txt
   ```

2. **配置MCP服务器：**
   使用 `amazon_q_config.json` 中的配置

3. **测试命令示例：**
   ```json
   {
     "tool_name": "read_pdf",
     "arguments": {
       "sources": [{"path": "./test.pdf"}],
       "include_full_text": true
     }
   }
   ```

## 📊 预期输出格式

### 成功处理PDF
```
📄 ./document.pdf
📊 Pages: 5
📝 Title: Sample Document | Author: John Doe
📖 Full Text:
This is the content of the PDF document...
```

### 错误处理
```
❌ Failed to process ./missing.pdf:
📁 File Not Found: File not found: ./missing.pdf
```

### 多PDF处理
```
📄 Processed 2 PDF sources:

--- Source 1: ./doc1.pdf ---
✅ Success
📊 Pages: 3

--- Source 2: ./doc2.pdf ---
❌ Failed: File not found
```

## 🐛 常见问题排查

### 1. 导入错误
```bash
# 确保依赖已安装
pip install -r requirements.txt

# 检查Python版本
python3 --version  # 需要 >=3.8
```

### 2. 路径错误
- 所有文件路径必须相对于项目根目录
- 不允许绝对路径或路径遍历 (`../`)

### 3. PDF处理错误
- 检查PDF文件是否损坏
- 确认文件权限
- 对于URL，检查网络连接

### 4. MCP连接问题
- 确保MCP包已正确安装
- 检查stdio输入输出

## ✅ 验收标准

项目通过测试的标准：

1. **基础功能测试** - 全部通过
2. **MCP服务器测试** - 至少3/4通过
3. **参数验证** - 正确捕获和处理无效输入
4. **错误处理** - 友好的错误消息
5. **安全检查** - 路径遍历保护生效

## 🚀 性能基准

### 预期性能（参考值）
- **小PDF (<1MB)**: <2秒处理
- **中PDF (1-10MB)**: <5秒处理
- **大PDF (>10MB)**: <10秒处理
- **URL下载**: 取决于网络速度
- **内存使用**: <100MB for typical PDFs

## 📝 测试报告模板

```
=== tsaol-pdf-reader-mcp 测试报告 ===

测试日期: [日期]
Python版本: [版本]
环境: [环境信息]

基础功能测试: ✅/❌
MCP服务器测试: ✅/❌
PDF处理测试: ✅/❌
安全检查: ✅/❌

问题记录:
- [如有问题，记录详细信息]

总体评价: [通过/失败]
```