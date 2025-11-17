#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
应用测试脚本
用于检查所有模块是否能正常导入和运行
"""
import sys
import os
import io

# 设置输出编码为UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def test_imports():
    """测试所有模块导入"""
    print("=" * 60)
    print("[测试模块导入]")
    print("=" * 60)
    
    modules_to_test = [
        ('flask', 'Flask'),
        ('requests', 'requests'),
        ('plotly', 'plotly'),
        ('pandas', 'pandas'),
        ('app', 'app'),
        ('database.db_manager', 'DatabaseManager'),
        ('modules.zodiac', 'get_zodiac'),
        ('modules.mbti', 'format_mbti_analysis'),
        ('modules.fortune', 'get_fortune_prediction'),
        ('modules.fengshui', 'get_fengshui_analysis'),
        ('modules.compatibility', 'analyze_combined_compatibility'),
        ('modules.visualization', 'create_fortune_chart'),
        ('modules.mental_health', 'analyze_mental_health'),
        ('modules.recommendation', 'get_recommendations'),
        ('modules.action_plan', 'generate_action_plan'),
        ('modules.divination', 'calculate_bazi'),
        ('modules.chat_assistant', 'ChatAssistant'),
    ]
    
    failed_imports = []
    
    for module_name, item_name in modules_to_test:
        try:
            if '.' in module_name:
                # 处理子模块
                module = __import__(module_name, fromlist=[item_name])
                if hasattr(module, item_name):
                    print(f"[OK] {module_name}.{item_name}")
                else:
                    print(f"[WARN] {module_name}.{item_name} - 属性不存在")
                    failed_imports.append((module_name, item_name))
            else:
                # 处理顶级模块
                __import__(module_name)
                print(f"[OK] {module_name}")
        except ImportError as e:
            print(f"[FAIL] {module_name}.{item_name} - 导入失败: {e}")
            failed_imports.append((module_name, item_name))
        except Exception as e:
            print(f"[WARN] {module_name}.{item_name} - 错误: {e}")
            failed_imports.append((module_name, item_name))
    
    return failed_imports

def test_database():
    """测试数据库功能"""
    print("\n" + "=" * 60)
    print("[测试数据库功能]")
    print("=" * 60)
    
    try:
        from database.db_manager import DatabaseManager
        
        db_manager = DatabaseManager()
        print("[OK] 数据库管理器初始化成功")
        
        # 测试数据库连接
        conn = db_manager.get_connection()
        if conn:
            print("[OK] 数据库连接成功")
            conn.close()
        else:
            print("[FAIL] 数据库连接失败")
            return False
        
        return True
    except Exception as e:
        print(f"[FAIL] 数据库测试失败: {e}")
        return False

def test_flask_app():
    """测试Flask应用创建"""
    print("\n" + "=" * 60)
    print("[测试Flask应用]")
    print("=" * 60)
    
    try:
        from app import create_app
        
        app = create_app()
        print("[OK] Flask应用创建成功")
        
        # 测试客户端
        with app.test_client() as client:
            # 测试主页
            response = client.get('/')
            if response.status_code == 200:
                print("[OK] 主页路由正常")
            else:
                print(f"[WARN] 主页路由状态码: {response.status_code}")
            
            # 测试历史记录页面
            response = client.get('/history')
            if response.status_code == 200:
                print("[OK] 历史记录页面路由正常")
            else:
                print(f"[WARN] 历史记录页面路由状态码: {response.status_code}")
            
            # 测试聊天页面
            response = client.get('/chat')
            if response.status_code == 200:
                print("[OK] 聊天页面路由正常")
            else:
                print(f"[WARN] 聊天页面路由状态码: {response.status_code}")
            
            # 测试匹配度分析页面
            response = client.get('/compatibility')
            if response.status_code == 200:
                print("[OK] 匹配度分析页面路由正常")
            else:
                print(f"[WARN] 匹配度分析页面路由状态码: {response.status_code}")
        
        return True
    except Exception as e:
        print(f"[FAIL] Flask应用测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_modules():
    """测试业务逻辑模块"""
    print("\n" + "=" * 60)
    print("[测试业务逻辑模块]")
    print("=" * 60)
    
    try:
        from modules.zodiac import get_zodiac
        from modules.mbti import format_mbti_analysis
        from modules.fortune import get_fortune_prediction
        
        # 测试星座获取
        zodiac = get_zodiac('2000-01-15')
        if zodiac:
            print(f"[OK] 星座获取成功: {zodiac}")
        else:
            print("[FAIL] 星座获取失败")
            return False
        
        # 测试MBTI分析
        mbti_analysis = format_mbti_analysis('INTJ')
        if mbti_analysis:
            print("[OK] MBTI分析成功")
        else:
            print("[FAIL] MBTI分析失败")
            return False
        
        # 测试运势预测
        fortune = get_fortune_prediction(zodiac, 'INTJ')
        if fortune:
            print("[OK] 运势预测成功")
        else:
            print("[FAIL] 运势预测失败")
            return False
        
        return True
    except Exception as e:
        print(f"[FAIL] 业务逻辑模块测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主函数"""
    print("\n" + "=" * 60)
    print("[应用测试开始]")
    print("=" * 60 + "\n")
    
    # 测试模块导入
    failed_imports = test_imports()
    
    # 测试数据库
    db_ok = test_database()
    
    # 测试Flask应用
    flask_ok = test_flask_app()
    
    # 测试业务逻辑模块
    modules_ok = test_modules()
    
    # 总结
    print("\n" + "=" * 60)
    print("[测试总结]")
    print("=" * 60)
    
    if failed_imports:
        print(f"[FAIL] 有 {len(failed_imports)} 个模块导入失败")
        for module_name, item_name in failed_imports:
            print(f"   - {module_name}.{item_name}")
    else:
        print("[OK] 所有模块导入成功")
    
    if db_ok:
        print("[OK] 数据库功能正常")
    else:
        print("[FAIL] 数据库功能异常")
    
    if flask_ok:
        print("[OK] Flask应用正常")
    else:
        print("[FAIL] Flask应用异常")
    
    if modules_ok:
        print("[OK] 业务逻辑模块正常")
    else:
        print("[FAIL] 业务逻辑模块异常")
    
    if not failed_imports and db_ok and flask_ok and modules_ok:
        print("\n[SUCCESS] 所有测试通过！应用可以正常运行。")
        return 0
    else:
        print("\n[WARN] 部分测试未通过，请检查上述错误。")
        return 1

if __name__ == '__main__':
    sys.exit(main())

