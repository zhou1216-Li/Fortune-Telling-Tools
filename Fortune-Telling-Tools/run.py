# 运行入口
"""
Flask Web 应用启动脚本
"""
import os
import sys

from flask import Flask

from app import create_app

def main():
    """主函数"""
    try:
        # 创建 Flask 应用实例
        app = create_app()
        
        # 获取端口号，默认为 5000
        port = int(os.environ.get('PORT', 5000))
        
        # 获取调试模式，生产环境应为 False
        debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
        
        # 启动应用
        print("启动 Flask 应用...")
        print(f"访问地址: http://0.0.0.0:{port}")
        print(f"调试模式: {debug}")
        
        app.run(
            debug=debug,
            host='0.0.0.0',
            port=port,
            threaded=True  # 启用多线程支持
        )
    except KeyboardInterrupt:
        print("\n应用已停止")
        sys.exit(0)
    except Exception as e:
        print(f"启动失败: {e}")
        print("尝试回退至最小化 Flask 应用以便公网连通性验证。")

        fallback_app = Flask(__name__)

        @fallback_app.route("/")
        def _fallback_home():
            return "Hello, World! (Fallback Flask App)"

        port = int(os.environ.get('PORT', 5000))
        debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
        print(f"回退应用启动中 http://0.0.0.0:{port}")
        fallback_app.run(
            debug=debug,
            host='0.0.0.0',
            port=port,
            threaded=True
        )

if __name__ == '__main__':
    main()

