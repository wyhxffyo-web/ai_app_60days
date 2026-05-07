# Day03 国内模型API入门：DeepSeek

## 学习目标
1.  了解DeepSeek API的基础使用方法
2.  完成API Key申请与配置
3.  实现一个支持命令行交互的对话程序

## 核心步骤
### 1. 环境准备
- 安装OpenAI SDK：`pip install openai`
- 申请DeepSeek API Key：登录DeepSeek开放平台，创建并复制API Key

### 2. 代码实现
- 配置DeepSeek客户端，指定API Key和base_url
- 初始化对话上下文，设置系统提示词
- 实现循环对话逻辑，支持用户输入和AI回复

### 3. 遇到的问题与解决
1.  **401认证错误**：API Key配置错误，修正了`os.environ.get`的错误用法，直接传入Key
2.  **400模型错误**：删除了`reasoning_effort`等不兼容的高级参数，使用`deepseek-chat`模型
3.  **缩进与逻辑错误**：修正了`break`语句位置，调整了消息添加顺序

## 运行结果
- 实现了命令行对话助手，支持多轮对话和上下文记忆
- 可正常调用DeepSeek API，返回符合系统提示词的回复