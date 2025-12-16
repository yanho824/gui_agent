# Browser-Use Agent 项目

使用 browser-use 和阿里云通义千问模型实现的浏览器自动化 AI Agent。

## 环境要求

- Python >= 3.12
- uv（Python 包管理器）

## 快速开始

### 1. 克隆项目

```bash
git clone <你的仓库地址>
cd test1
```

### 2. 安装 uv

如果还没有安装 uv，请先安装：

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 或使用 pip
pip install uv
```

### 3. 配置环境变量

创建 `.env` 文件并添加你的 API Key：

```bash
cp .env.example .env  # 如果提供了 .env.example
# 或直接创建 .env 文件
```

在 `.env` 文件中添加：

```env
ALIBABA_CLOUD=sk-your-dashscope-api-key-here
BROWSER_USE_API_KEY=bu_your-browser-use-api-key-here
```

> **获取 API Key：**
> - 阿里云 DashScope API Key: https://modelstudio.console.alibabacloud.com/?tab=playground#/api-key
> - Browser Use API Key: https://browser-use.com/

### 4. 安装依赖并运行

使用 uv 会自动创建虚拟环境并安装依赖：

```bash
uv run main.py
```

第一次运行时，uv 会：
- 自动创建虚拟环境（`.venv`）
- 安装项目依赖（`browser-use` 等）
- 执行 `main.py`

## 项目结构

```
.
├── main.py           # 主程序入口
├── pyproject.toml    # 项目配置和依赖
├── .env             # 环境变量（不会提交到 git）
├── .gitignore       # Git 忽略文件
└── README.md        # 项目说明
```

## 使用说明

修改 `main.py` 中的任务描述来自定义 Agent 的行为：

```python
agent = Agent(
    task="你的任务描述",
    llm=llm,
    use_vision=True
)
```

## 注意事项

- 确保 `.env` 文件包含有效的 API Key
- 第一次运行会下载浏览器驱动，需要一些时间
- 某些网站可能需要登录才能访问完整内容

## 常见问题

**Q: 如何切换其他模型？**

修改 `main.py` 中的模型名称：
```python
llm = ChatOpenAI(model='qwen-turbo', api_key=api_key, base_url=base_url)
```

**Q: WSL 环境下遇到问题？**

确保使用自动浏览器管理，不要手动指定 Windows 的浏览器路径。

## 许可证

MIT