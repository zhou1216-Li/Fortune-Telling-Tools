# Flask应用工厂
from flask import Flask
import os

def create_app():
    """创建Flask应用"""
    # 获取应用根目录
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    app.secret_key = os.urandom(24)
    
    # 注册蓝图（只使用主路由，纯Python后端渲染）
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app

