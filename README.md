# Django 與 AWS RDS PostgreSQL 快速入門指南

本文檔提供了 Django 項目創建和配置 AWS RDS PostgreSQL 數據庫的步驟指南。這將幫助團隊成員快速了解環境設置和當前進度。

## 1. 設置 Django 環境

首先，我們需要創建一個虛擬環境並安裝 Django：

```bash
# 創建一個名為 django-learn 的虛擬環境，使用 Python 3.12
conda create -n django-learn python=3.12

# 激活虛擬環境
source activate django-learn

# 安裝 Django 框架
pip install django

# 確認 Django 版本
python -m django --version
```

## 2. 創建 Django 項目

在環境設置好後，我們創建並啟動一個新的 Django 項目：

```bash
# 創建一個名為 django101 的新項目
django-admin startproject django101

# 進入項目目錄
cd django101

# 創建一個名為 myapp 的應用
python manage.py startapp myapp

# 完成 urls.py 和 views.py 的編輯後，啟動開發服務器
python manage.py runserver
```

## 3. 連接 AWS RDS PostgreSQL 數據庫

接下來，我們將 Django 項目連接到 AWS RDS PostgreSQL 數據庫：

```bash
# 安裝 PostgreSQL 的 Python 驅動
pip install psycopg2-binary

# 安裝環境變量管理工具，用於安全存儲數據庫憑證
pip install python-dotenv
```

### 設置環境變量

專案中已經包含了 `.env.example` 文件，您可以使用它來創建自己的 `.env` 文件：

```bash
# 複製 .env.example 文件為 .env
cp .env.example .env

# 使用文本編輯器打開 .env 文件
vim .env  # 或使用其他編輯器如 nano、vscode 等
```

在 `.env` 文件中填入您的 AWS RDS PostgreSQL 數據庫憑證和其他必要信息：

```
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your-rds-endpoint.rds.amazonaws.com
DB_PORT=5432
SECRET_KEY=django_secret_key
DEBUG=True
```

### 修改 settings.py 以連接 RDS

在 `settings.py` 文件中，需要進行如下配置：

```python
# 使用 python-dotenv 加載環境變量
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# 數據庫配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),  # RDS 端點地址
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

## 4. 數據庫遷移與管理

完成數據庫配置後，我們需要執行遷移命令以創建數據庫結構：

```bash
# 創建遷移文件
python manage.py makemigrations

# 應用遷移，更新數據庫結構
python manage.py migrate

# 創建管理員用戶，用於訪問 Django 管理界面
python manage.py createsuperuser
```

## 後續步驟

1. **完善模型設計**：在 `models.py` 中定義您的數據模型
2. **創建視圖和模板**：設計用戶界面和交互邏輯
3. **配置 AWS 安全組**：確保 RDS 僅接受來自特定 IP 的連接
4. **部署準備**：考慮使用 AWS Elastic Beanstalk 或 EC2 部署應用

## 注意事項

- 請勿將數據庫憑證直接硬編碼在代碼中
- 確保未來其他 `.env` 相關文件（例如 `.env.development`、`.env.production`）已添加到 `.gitignore` 列表
- 在生產環境中，設置 `DEBUG = False`
- 考慮為不同環境（開發、測試、生產）使用不同的設置文件
- 新加入項目的團隊成員應該使用 `.env.example` 作為模板創建自己的 `.env` 文件，並填入正確的數據庫連接信息
