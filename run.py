# 运行入口
"""
Flask Web 应用启动脚本
"""
import os
import sys
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
        print(f"🚀 启动 Flask 应用...")
        print(f"📡 访问地址: http://0.0.0.0:{port}")
        print(f"🔧 调试模式: {debug}")
        
        app.run(
            debug=debug,
            host='0.0.0.0',
            port=port,
            threaded=True  # 启用多线程支持
        )
    except KeyboardInterrupt:
        print("\n⚠️  应用已停止")
        sys.exit(0)
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

