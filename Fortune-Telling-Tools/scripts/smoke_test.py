#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
轻量级功能检查脚本，帮助在部署前快速验证核心模块是否可用。
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

print("=== Fortune-Telling Tools: 核心模块自检 ===")

try:
    from modules.zodiac import get_zodiac
    from modules.fortune import get_fortune_prediction
    from modules.compatibility import analyze_combined_compatibility
    from modules.visualization import create_compatibility_chart
    from modules.mental_health import analyze_mental_health
    from modules.recommendation import get_recommendations
    from modules.action_plan import generate_action_plan
    from modules.divination import calculate_bazi, analyze_tarot_reading
except Exception as exc:  # pragma: no cover - diagnostic utility
    print(f"❌ 模块导入失败：{exc}")
    raise
else:
    print("✓ 模块导入成功")

try:
    zodiac = get_zodiac("2000-01-15")
    print(f"✓ 星座分析正常：{zodiac}")

    fortune = get_fortune_prediction(zodiac, "INTJ")
    print(f"✓ 运势预测返回 {len(fortune)} 个维度")

    compatibility = analyze_combined_compatibility("白羊座", "INTJ", "狮子座", "ENFP")
    combined_score = compatibility.get("综合匹配", {}).get("score", 0)
    print(f"✓ 匹配度分析正常：综合得分 {combined_score}")

    visualization = create_compatibility_chart(compatibility)
    if visualization:
        print("✓ 可视化生成成功：已返回 HTML 片段")
    else:
        print("⚠️ 可视化生成返回空结果")

    mental_health = analyze_mental_health("INTJ")
    print(f"✓ 心理健康分析结果：{mental_health.get('mbti_type', '未知')}")

    recommendations = get_recommendations("INTJ", zodiac)
    print(f"✓ 个性化推荐数量：{len(recommendations)}")

    action_plan = generate_action_plan("INTJ", zodiac)
    print(f"✓ 行动计划生成成功：{len(action_plan)} 项")

    bazi = calculate_bazi("2000-01-15", 14)
    print(f"✓ 八字分析成功：年柱 {bazi.get('year', '未知')}")

    tarot = analyze_tarot_reading(3)
    print(f"✓ 塔罗牌分析成功：抽取 {len(tarot.get('cards', []))} 张牌")

    print("\n🎉 核心功能自检通过！")
except Exception as exc:  # pragma: no cover - diagnostic utility
    print(f"\n❌ 自检失败：{exc}")
    raise

