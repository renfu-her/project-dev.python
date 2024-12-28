# project-dev.python

## 環境變數

```
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
DATABASE_URL=mysql://root:password@localhost/blog_db 
```

## 資料庫

```
mysql -u root -p
```

## 遷移（初始化 DB）

```
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

## 遷移（更新 DB）

```
flask db migrate -m "update migration"
flask db upgrade
```