#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试所有模块是否能正常导入和运行
"""
import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """测试所有模块导入"""
    print("=" * 50)
    print("开始测试模块导入...")
    print("=" * 50)
    
    modules_to_test = [
        ("modules.zodiac", ["get_zodiac", "format_zodiac_analysis"]),
        ("modules.mbti", ["format_mbti_analysis"]),
        ("modules.fortune", ["get_fortune_prediction", "format_fortune_prediction"]),
        ("modules.fengshui", ["get_fengshui_analysis", "format_fengshui_analysis"]),
        ("modules.compatibility", ["analyze_combined_compatibility", "format_compatibility_analysis"]),
        ("modules.visualization", ["create_compatibility_chart", "create_fortune_chart"]),
        ("modules.mental_health", ["analyze_mental_health", "format_mental_health_analysis"]),
        ("modules.recommendation", ["get_recommendations", "format_recommendations"]),
        ("modules.action_plan", ["generate_action_plan", "format_action_plan"]),
        ("modules.divination", ["calculate_bazi", "analyze_bazi", "format_bazi_analysis", "analyze_tarot_reading", "format_tarot_reading"]),
        ("modules.chat_assistant", ["ChatAssistant"]),
        ("database.db_manager", ["DatabaseManager"]),
    ]
    
    failed_modules = []
    
    for module_name, functions in modules_to_test:
        try:
            module = __import__(module_name, fromlist=functions)
            for func_name in functions:
                if not hasattr(module, func_name):
                    print(f"❌ {module_name}.{func_name} 不存在")
                    failed_modules.append(f"{module_name}.{func_name}")
                else:
                    print(f"✓ {module_name}.{func_name} 导入成功")
        except Exception as e:
            print(f"❌ {module_name} 导入失败: {e}")
            failed_modules.append(module_name)
    
    print("=" * 50)
    if failed_modules:
        print(f"❌ 有 {len(failed_modules)} 个模块/函数导入失败")
        for item in failed_modules:
            print(f"  - {item}")
        return False
    else:
        print("✓ 所有模块导入成功！")
        return True

def test_functions():
    """测试关键功能"""
    print("\n" + "=" * 50)
    print("开始测试功能...")
    print("=" * 50)
    
    try:
        from modules.zodiac import get_zodiac
        from modules.fortune import get_fortune_prediction
        from modules.compatibility import analyze_combined_compatibility
        from modules.visualization import create_compatibility_chart, create_fortune_chart
        from modules.mental_health import analyze_mental_health
        from modules.recommendation import get_recommendations
        from modules.action_plan import generate_action_plan
        from modules.divination import calculate_bazi, analyze_tarot_reading
        
        # 测试星座
        zodiac = get_zodiac("2000-01-15")
        print(f"✓ 星座测试: {zodiac}")
        
        # 测试运势
        fortune = get_fortune_prediction("白羊座", "INTJ")
        print(f"✓ 运势测试: {len(fortune)} 个运势类型")
        
        # 测试匹配度
        compatibility = analyze_combined_compatibility("白羊座", "INTJ", "狮子座", "ENFP")
        if compatibility:
            print(f"✓ 匹配度测试: 综合匹配 {compatibility.get('综合匹配', {}).get('score', 0)}分")
        else:
            print("❌ 匹配度测试失败")
        
        # 测试图表
        if compatibility:
            chart_html = create_compatibility_chart({
                '情感匹配': compatibility.get('情感匹配', {}),
                '生活匹配': compatibility.get('生活匹配', {}),
                '事业匹配': compatibility.get('事业匹配', {})
            })
            if chart_html:
                print("✓ 匹配度图表生成成功")
            else:
                print("❌ 匹配度图表生成失败")
        
        fortune_chart = create_fortune_chart(fortune)
        if fortune_chart:
            print("✓ 运势图表生成成功")
        else:
            print("❌ 运势图表生成失败")
        
        # 测试心理健康
        mental_health = analyze_mental_health("INTJ")
        if mental_health:
            print(f"✓ 心理健康测试: {mental_health.get('mbti_type', '')}")
        
        # 测试推荐
        recommendations = get_recommendations(fortune)
        print(f"✓ 推荐测试: {len([k for k, v in recommendations.items() if v])} 个推荐类别")
        
        # 测试行动计划
        action_plan = generate_action_plan(fortune, "白羊座", "INTJ")
        print(f"✓ 行动计划测试: {len([k for k, v in action_plan.items() if v])} 个行动计划类别")
        
        # 测试八字
        bazi = calculate_bazi("2000-01-15", 14)
        if bazi:
            print(f"✓ 八字测试: {bazi.get('year', '')}")
        
        # 测试塔罗牌
        tarot = analyze_tarot_reading(3)
        if tarot:
            print(f"✓ 塔罗牌测试: {len(tarot.get('cards', []))} 张牌")
        
        print("=" * 50)
        print("✓ 所有功能测试通过！")
        return True
        
    except Exception as e:
        print(f"❌ 功能测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_flask_app():
    """测试Flask应用"""
    print("\n" + "=" * 50)
    print("开始测试Flask应用...")
    print("=" * 50)
    
    try:
        from app import create_app
        app = create_app()
        print("✓ Flask应用创建成功")
        
        # 测试路由
        with app.test_client() as client:
            # 测试主页
            response = client.get('/')
            if response.status_code == 200:
                print("✓ 主页路由正常")
            else:
                print(f"❌ 主页路由失败: {response.status_code}")
            
            # 测试分析页面
            response = client.get('/analyze')
            if response.status_code == 200:
                print("✓ 分析页面路由正常")
            else:
                print(f"❌ 分析页面路由失败: {response.status_code}")
            
            # 测试匹配度页面
            response = client.get('/compatibility')
            if response.status_code == 200:
                print("✓ 匹配度页面路由正常")
            else:
                print(f"❌ 匹配度页面路由失败: {response.status_code}")
            
            # 测试历史记录页面
            response = client.get('/history')
            if response.status_code == 200:
                print("✓ 历史记录页面路由正常")
            else:
                print(f"❌ 历史记录页面路由失败: {response.status_code}")
            
            # 测试聊天页面
            response = client.get('/chat')
            if response.status_code == 200:
                print("✓ 聊天页面路由正常")
            else:
                print(f"❌ 聊天页面路由失败: {response.status_code}")
        
        print("=" * 50)
        print("✓ Flask应用测试通过！")
        return True
        
    except Exception as e:
        print(f"❌ Flask应用测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("命理预测工具 - 模块测试")
    print("=" * 50 + "\n")
    
    # 测试模块导入
    import_ok = test_imports()
    
    if import_ok:
        # 测试功能
        function_ok = test_functions()
        
        # 测试Flask应用
        flask_ok = test_flask_app()
        
        print("\n" + "=" * 50)
        print("测试总结")
        print("=" * 50)
        print(f"模块导入: {'✓ 通过' if import_ok else '❌ 失败'}")
        print(f"功能测试: {'✓ 通过' if function_ok else '❌ 失败'}")
        print(f"Flask应用: {'✓ 通过' if flask_ok else '❌ 失败'}")
        
        if import_ok and function_ok and flask_ok:
            print("\n🎉 所有测试通过！应用可以正常运行。")
            sys.exit(0)
        else:
            print("\n⚠️  部分测试失败，请检查上述错误。")
            sys.exit(1)
    else:
        print("\n❌ 模块导入失败，请先解决导入问题。")
        sys.exit(1)

