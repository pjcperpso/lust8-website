# LUST8 Backend - FastAPI

成人用品独立站后端 API，基于 FastAPI + SQLAlchemy + SQLite（可平滑迁移到 PostgreSQL）。

## 功能模块

- **产品管理** - 产品 CRUD、分类、筛选、排序、搜索
- **购物车** - 登录用户/游客购物车增删改查
- **订单系统** - 下单、订单查询、库存扣减
- **B2B Wholesale** - 报价申请、管理后台
- **Newsletter** - 邮件订阅/退订
- **用户认证** - JWT 注册登录（管理员 & 普通用户）
- **多语言支持** - i18n (en / zh)
- **管理后台** - 订单管理、产品管理、数据统计

## 环境要求

- Python 3.11+ （推荐 3.11 或 3.12）
- pip

> ⚠️ **Windows 用户注意**：安装 Python 时请勾选 "Add Python to PATH"。如果命令行找不到 `python`，可以尝试用 `py` 命令调用。

## 快速开始

### Windows

```bash
# 1. 创建虚拟环境
py -m venv venv
# 或
python -m venv venv

# 2. 激活虚拟环境
.\venv\Scripts\activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 启动服务（三选一）
# 方式 A：run.py 启动脚本（推荐）
python run.py

# 方式 B：uvicorn 直接启动（带热重载）
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 方式 C：python -m uvicorn
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Mac / Linux

```bash
# 1. 创建虚拟环境
python3 -m venv venv

# 2. 激活
source venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 启动
python run.py
# 或
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 验证

启动成功后访问：

- **API 文档 (Swagger)**：http://localhost:8000/docs
- **健康检查**：http://localhost:8000/health
- **产品列表**：http://localhost:8000/api/products

## 默认账号

- 管理员：`admin@lust8.com` / `admin123`

## 数据库切换到 PostgreSQL

修改 `.env` 文件中的 `DATABASE_URL`：

```
DATABASE_URL=postgresql://user:password@localhost:5432/lust8
```

需要额外安装：
```bash
pip install psycopg2-binary
```

## API 概览

| 模块 | 方法 | 路径 | 说明 |
|------|------|------|------|
| **产品** | GET | `/api/products` | 产品列表（分页/筛选/排序/搜索） |
| | GET | `/api/products/featured` | 精选产品 |
| | GET | `/api/products/categories` | 分类列表 |
| | GET | `/api/products/{id_or_slug}` | 产品详情 |
| | POST/PUT/DELETE | `/api/products/...` | 产品 CRUD（管理员） |
| **购物车** | GET | `/api/cart` | 获取购物车 |
| | POST | `/api/cart` | 添加商品 |
| | PUT | `/api/cart/{item_id}` | 修改数量 |
| | DELETE | `/api/cart/{item_id}` | 删除商品 |
| | DELETE | `/api/cart` | 清空购物车 |
| **订单** | POST | `/api/orders` | 创建订单 |
| | GET | `/api/orders` | 我的订单 |
| | GET | `/api/orders/{id}` | 订单详情 |
| **认证** | POST | `/api/auth/register` | 注册 |
| | POST | `/api/auth/login` | 登录 |
| | GET | `/api/auth/me` | 当前用户信息 |
| **B2B** | POST | `/api/wholesale/inquiry` | 提交报价申请 |
| **Newsletter** | POST | `/api/newsletter/subscribe` | 订阅 |
| | POST | `/api/newsletter/unsubscribe` | 退订 |
| **管理** | GET | `/api/admin/stats` | 数据统计 |
| | GET | `/api/admin/orders` | 订单列表 |
| | PATCH | `/api/admin/orders/{id}/status` | 更新订单状态 |

## 项目结构

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI 入口
│   ├── config.py            # 配置（pydantic-settings）
│   ├── database.py          # 数据库连接 & Session
│   ├── models.py            # SQLAlchemy ORM 模型
│   ├── schemas.py           # Pydantic 请求/响应模型
│   ├── auth.py              # JWT 认证 & 密码哈希
│   ├── seed.py              # 初始化种子数据
│   └── api/
│       ├── __init__.py
│       ├── products.py      # 产品 API
│       ├── cart.py          # 购物车 API
│       ├── orders.py        # 订单 API
│       ├── auth.py          # 认证 API
│       ├── wholesale.py     # B2B 报价 API
│       ├── newsletter.py    # 订阅 API
│       └── admin.py         # 管理后台 API
├── requirements.txt
├── run.py                   # 启动脚本
├── .env.example             # 环境变量示例
└── lust8.db                 # SQLite 数据库（自动生成）
```

## 前端对接说明

- 所有 API 路径前缀：`/api`
- 支持 CORS（默认允许 localhost:5173 / 3000）
- 认证方式：Bearer Token (JWT)
- 游客购物车使用 `session_id` Cookie 标识
- 多语言通过 `?lang=en` 或 `?lang=zh` 查询参数切换
