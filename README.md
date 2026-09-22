# 班级量化管理系统

一个基于 Flask + SQLite + Tailwind CSS 的班级量化管理应用，支持学生信息管理、量化评分、排行榜、统计报表和 AI 智能分析。

## 功能特性

- **学生信息管理**：添加、编辑、删除学生信息，支持搜索和筛选
- **量化评分系统**：支持奖励/扣分，多种分类维度，快速评分按钮
- **排行榜**：可视化排名，前三名颁奖台展示
- **统计报表**：分数分布图、分类统计图、及格率等
- **AI 智能分析**：基于大模型的学生表现分析和建议（需配置 API Key）
- **导出功能**：导出全班 Excel 报表、个人评分记录

## 技术栈

- **后端**：Python Flask + SQLAlchemy
- **数据库**：SQLite
- **前端**：HTML + Tailwind CSS + Chart.js
- **AI**：OpenAI API（可配置）

## 安装与运行

### 1. 安装依赖

```bash
cd class-management
pip install -r requirements.txt
```

### 2. 配置 AI（可选）

如需使用 AI 分析功能，设置环境变量：

```bash
# Windows PowerShell
$env:OPENAI_API_KEY="your-api-key"
$env:OPENAI_BASE_URL="https://api.openai.com/v1"
$env:AI_MODEL="gpt-3.5-turbo"

# 或使用其他兼容 API（如 DeepSeek、通义千问等）
$env:OPENAI_BASE_URL="https://api.deepseek.com/v1"
```

### 3. 启动应用

```bash
python app.py
```

访问 http://localhost:5000 即可使用。

## 项目结构

```
class-management/
├── app.py              # Flask 主应用
├── models.py           # 数据模型
├── requirements.txt    # 依赖列表
├── database.db         # SQLite 数据库（自动创建）
├── templates/          # HTML 模板
│   ├── base.html       # 基础模板
│   ├── index.html      # 数据看板
│   ├── students.html   # 学生管理
│   ├── scoring.html    # 量化评分
│   ├── rankings.html   # 排行榜
│   └── reports.html    # 统计报表
└── static/
    ├── css/
    │   └── style.css   # 自定义样式
    └── js/
        └── app.js      # 前端脚本
```

## 使用说明

1. **添加学生**：进入「学生管理」页面，点击「添加学生」
2. **进行评分**：进入「量化评分」页面，选择学生和评分类型
3. **查看排名**：进入「排行榜」页面查看全班排名
4. **导出报表**：进入「统计报表」页面导出 Excel
5. **AI 分析**：在「统计报表」页面配置 API Key 后使用 AI 分析

## 截图

- 数据看板：展示学生总数、平均分、最近记录等
- 学生管理：支持增删改查和搜索筛选
- 量化评分：表单评分 + 快速评分按钮
- 排行榜：颁奖台 + 分数图表 + 完整排名
- 统计报表：数据统计 + AI 分析 + 导出功能

## License

MIT
