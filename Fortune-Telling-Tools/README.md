# 命理预测工具 - Web版

## 项目简介

这是一个基于Flask的命理预测Web应用，帮助用户通过输入个人信息（如出生日期、MBTI类型等），提供性格分析和运势预测。

## 功能特性

### 核心功能
- **用户信息输入**：用户输入生日、MBTI类型等信息
- **星座分析**：根据用户的出生日期，判断用户的星座哦并提供相应的星座性格分析
- **MBTI性格分析**：根据用户的MBTI类型，提供性格分析及与其他类型的相容性描述
- **运势预测**：根据星座和MBTI类型，结合模拟运势数据，预测用户的财运、感情运等
- **历史记录保存**：每次分析后，用户的分析结果、反馈以及相关信息将保存到数据库中
- **用户反馈机制**：用户在查看结果后，可以提供反馈信息，帮助优化未来的分析结果
- **心理聊天助手**：AI心理疏导功能，提供心理支持和情感交流

### 新增功能 ✨
- **💕 匹配度分析**：分析两个人之间的情感匹配度、生活匹配度、事业匹配度
- **📊 可视化图表**：使用Plotly生成匹配度分析和运势预测的可视化图表
- **💚 心理健康分析**：基于MBTI类型进行心理健康分析，提供建议和应对技巧
- **🔮 多命理学分析**：支持八字分析和塔罗牌占卜（可选）
- **🎯 个性化推荐**：根据运势预测结果生成个性化的内容推荐
- **📋 行动计划**：基于运势预测结果生成具体的行动计划
- **🏠 风水分析**：根据居住方位和房屋朝向进行风水分析（可选）

## 技术栈

- **后端**：Flask (Python Web框架)
- **前端**：PyScript (浏览器中运行Python)
- **数据库**：SQLite
- **AI聊天**：免费API（无需配置）

**全栈Python**：前后端都使用Python开发！

## 安装步骤

### 1. 安装依赖

**Windows 用户：**
```bash
# 方法一：使用安装脚本（推荐）
scripts\install.bat

# 方法二：手动安装
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Linux/Mac 用户：**
```bash
# 方法一：使用安装脚本（推荐）
chmod +x scripts/install.sh
./scripts/install.sh

# 方法二：手动安装
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```

### 2. 运行应用

**Windows 用户：**
```bash
# 方法一：使用启动脚本（推荐，会自动检查依赖）
scripts\start.bat

# 方法二：使用增强脚本（包含依赖与数据库检查）
scripts\启动应用.bat

# 方法三：直接运行
python run.py
```

**Linux/Mac 用户：**
```bash
# 方法一：使用启动脚本（推荐，会自动检查依赖）
chmod +x scripts/start.sh
./scripts/start.sh

# 方法二：使用增强脚本（包含依赖与数据库检查）
chmod +x scripts/启动应用.sh
./scripts/启动应用.sh

# 方法三：直接运行
python3 run.py
```

### 3. 访问应用

打开浏览器访问：http://localhost:5000

**注意：** 如果遇到 `ModuleNotFoundError: No module named 'flask'` 错误，请先执行步骤 1 安装依赖。

## 部署到公网

### 方法一：使用 GitHub Actions 自动部署到 Heroku（推荐）

1. **配置 Heroku Secrets**
   - 在 GitHub 仓库中，进入 Settings > Secrets and variables > Actions
   - 添加以下 Secrets：
     - `HEROKU_API_KEY`: 您的 Heroku API Key（在 Heroku 账户设置中获取）
     - `HEROKU_APP_NAME`: 您的 Heroku 应用名称
     - `HEROKU_EMAIL`: 您的 Heroku 账户邮箱

2. **创建 Heroku 应用**
   ```bash
   heroku create your-app-name
   ```

3. **推送代码到 GitHub**
   - 推送到 `main` 或 `master` 分支
   - GitHub Actions 会自动触发部署

4. **访问应用**
   - 部署完成后访问：https://your-app-name.herokuapp.com

### 方法二：手动部署到 Heroku

1. **安装 Heroku CLI**
   - 访问：https://devcenter.heroku.com/articles/heroku-cli
   - 下载并安装

2. **登录 Heroku**
   ```bash
   heroku login
   ```

3. **创建应用**
   ```bash
   heroku create your-app-name
   ```

4. **部署**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

5. **访问应用**
   - 应用会自动部署
   - 访问：https://your-app-name.herokuapp.com

### 方法三：使用 Railway

1. **注册 Railway**
   - 访问：https://railway.app
   - 注册账号

2. **连接 GitHub**
   - 点击 "New Project"
   - 选择 "Deploy from GitHub repo"
   - 选择您的仓库

3. **自动部署**
   - Railway 会自动检测 Flask 应用
   - 自动部署并生成 URL

### 方法四：使用 Vercel

1. **安装 Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **部署**
   ```bash
   vercel
   ```

### 方法五：使用 PythonAnywhere

1. **注册 PythonAnywhere**
   - 访问：https://www.pythonanywhere.com
   - 注册免费账号

2. **上传文件**
   - 使用 Files 标签页上传项目文件

3. **配置 Web App**
   - 在 Web 标签页创建新的 Web App
   - 配置 WSGI 文件

## 项目结构

```
python/
├── app/                   # Flask应用主目录
│   ├── __init__.py       # 应用工厂
│   ├── routes.py         # 主路由
│   ├── api/              # API路由
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── static/           # 静态文件
│   │   └── css/
│   │       └── style.css
│   └── templates/        # 模板文件
│       └── index.html
├── modules/              # 业务逻辑模块
│   ├── __init__.py
│   ├── zodiac.py
│   ├── mbti.py
│   ├── fortune.py
│   ├── chat_assistant.py
│   └── data/
│       ├── zodiac_data.json
│       └── mbti_data.json
├── database/             # 数据库模块
│   ├── __init__.py
│   └── db_manager.py
├── data/                 # 数据目录（数据库文件）
│   └── fortune_telling.db
├── docs/                 # 项目文档
│   ├── 功能说明.md
│   ├── 检查清单.md
│   └── 运行指南.md
├── scripts/              # 跨平台辅助脚本
│   ├── install.bat
│   ├── install.sh
│   ├── start.bat
│   ├── start.sh
│   ├── restart.bat
│   ├── restart.sh
│   ├── 启动应用.bat
│   ├── 启动应用.sh
│   └── smoke_test.py
├── run.py                # 运行入口
├── config.py             # 配置文件
├── requirements.txt      # 依赖管理
├── Procfile              # Heroku部署配置
├── runtime.txt           # Python版本
├── .gitignore            # Git忽略文件
├── .github/              # GitHub Actions 工作流
│   └── workflows/
│       ├── deploy.yml           # 部署工作流
│       └── heroku-deploy.yml    # Heroku 自动部署工作流
└── README.md             # 项目说明
```

## 使用说明

### 基本使用
1. 运行程序后，在主页输入您的姓名、生日和MBTI类型
2. 可选：输入出生时辰、居住方位、房屋朝向等信息
3. 可选：启用八字分析和塔罗牌占卜
4. 点击"开始分析"按钮，系统将为您生成全面的分析结果
5. 查看分析结果，包括：
   - 星座分析和MBTI分析
   - 运势预测（带可视化图表）
   - 心理健康分析
   - 个性化推荐
   - 行动计划
   - 八字分析（如果启用）
   - 塔罗牌占卜（如果启用）
6. 查看分析结果后，可以提交反馈
7. 在历史记录界面可以查看之前的分析记录
8. 在心理聊天界面可以与AI助手聊天

### 匹配度分析
1. 进入"匹配度分析"页面
2. 输入两个人的姓名、生日和MBTI类型
3. 点击"开始匹配度分析"按钮
4. 查看匹配度分析结果，包括：
   - 情感匹配度
   - 生活匹配度
   - 事业匹配度
   - 综合匹配度
   - 详细分析和可视化图表

### 删除历史记录
1. 在"历史记录"页面，每条记录右侧有删除按钮（🗑️）
2. 点击删除按钮，确认删除操作
3. 删除成功后，记录将从列表中移除
4. 也可以在查看历史记录详情页面直接删除记录

## API接口

- `POST /api/analyze` - 分析接口
- `POST /api/feedback` - 提交反馈接口
- `GET /api/history` - 获取历史记录接口
- `GET /api/history/<id>` - 获取历史记录详情接口
- `GET /api/mbti/types` - 获取MBTI类型列表接口
- `POST /api/chat` - 聊天接口
- `POST /api/chat/clear` - 清空聊天记录接口

## 数据库说明

程序使用SQLite数据库存储用户信息和分析历史记录。数据库文件（fortune_telling.db）会自动创建在 `data/` 目录中。

## 许可证

本项目仅供学习和研究使用。
