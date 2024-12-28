from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# 初始化擴展
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 初始化 Flask 擴展
    db.init_app(app)
    migrate.init_app(app, db)

    # 註冊藍圖
    from app.routes import main
    app.register_blueprint(main)

    return app 