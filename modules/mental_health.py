# 心理健康分析模块
"""
基于MBTI类型和用户反馈进行心理健康分析
"""

# MBTI类型对应的心理健康特征
MBTI_MENTAL_HEALTH = {
    "INTJ": {
        "优势": ["理性思考", "独立自主", "目标明确"],
        "风险": ["过度思考", "社交孤立", "完美主义"],
        "建议": ["保持社交联系", "适度放松", "接受不完美"]
    },
    "INTP": {
        "优势": ["逻辑思维", "创新思考", "独立思考"],
        "风险": ["情绪忽视", "社交困难", "拖延症"],
        "建议": ["关注情绪", "加强社交", "设定 deadline"]
    },
    "ENTJ": {
        "优势": ["领导力", "决策力", "执行力"],
        "风险": ["压力过大", "工作狂", "忽视他人"],
        "建议": ["平衡工作生活", "学会放松", "倾听他人"]
    },
    "ENTP": {
        "优势": ["创造力", "适应性", "乐观"],
        "风险": ["注意力分散", "缺乏耐心", "冲动"],
        "建议": ["专注目标", "培养耐心", "三思后行"]
    },
    "INFJ": {
        "优势": ["同理心", "洞察力", "理想主义"],
        "风险": ["过度敏感", "理想化", "情绪波动"],
        "建议": ["保护自己", "接受现实", "情绪管理"]
    },
    "INFP": {
        "优势": ["创造力", "价值观", "同理心"],
        "风险": ["过度理想化", "情绪敏感", "自我批评"],
        "建议": ["接受现实", "自我接纳", "寻求支持"]
    },
    "ENFJ": {
        "优势": ["社交能力", "领导力", "同理心"],
        "风险": ["过度付出", "忽视自己", "压力过大"],
        "建议": ["学会说不", "关注自己", "设定边界"]
    },
    "ENFP": {
        "优势": ["热情", "创造力", "适应性"],
        "风险": ["注意力分散", "情绪波动", "缺乏计划"],
        "建议": ["专注目标", "情绪管理", "制定计划"]
    },
    "ISTJ": {
        "优势": ["责任感", "可靠性", "稳定性"],
        "风险": ["固执", "缺乏灵活性", "压力积累"],
        "建议": ["保持开放", "学会放松", "寻求变化"]
    },
    "ISFJ": {
        "优势": ["责任感", "同理心", "忠诚"],
        "风险": ["过度付出", "忽视自己", "压力积累"],
        "建议": ["学会拒绝", "关注自己", "寻求帮助"]
    },
    "ESTJ": {
        "优势": ["组织能力", "决策力", "执行力"],
        "风险": ["压力过大", "缺乏灵活性", "忽视他人"],
        "建议": ["平衡工作生活", "保持开放", "倾听他人"]
    },
    "ESFJ": {
        "优势": ["社交能力", "责任感", "同理心"],
        "风险": ["过度付出", "忽视自己", "压力过大"],
        "建议": ["学会说不", "关注自己", "设定边界"]
    },
    "ISTP": {
        "优势": ["逻辑思维", "解决问题", "独立性"],
        "风险": ["情感忽视", "社交困难", "冲动"],
        "建议": ["关注情绪", "加强社交", "三思后行"]
    },
    "ISFP": {
        "优势": ["创造力", "同理心", "适应性"],
        "风险": ["情绪敏感", "缺乏自信", "逃避冲突"],
        "建议": ["建立自信", "表达自己", "面对冲突"]
    },
    "ESTP": {
        "优势": ["行动力", "适应性", "乐观"],
        "风险": ["冲动", "缺乏计划", "忽视后果"],
        "建议": ["三思后行", "制定计划", "考虑后果"]
    },
    "ESFP": {
        "优势": ["社交能力", "乐观", "适应性"],
        "风险": ["注意力分散", "缺乏计划", "情绪波动"],
        "建议": ["专注目标", "制定计划", "情绪管理"]
    }
}

# 压力应对建议
STRESS_COPING = {
    "轻度压力": [
        "深呼吸练习",
        "适度运动",
        "保持规律作息",
        "与朋友交流",
        "听音乐放松"
    ],
    "中度压力": [
        "时间管理",
        "设定优先级",
        "寻求支持",
        "学会拒绝",
        "放松训练"
    ],
    "重度压力": [
        "专业心理咨询",
        "医疗检查",
        "调整生活方式",
        "寻求社会支持",
        "考虑休息"
    ]
}

# 情绪管理技巧
EMOTION_MANAGEMENT = {
    "焦虑": [
        "深呼吸练习",
        "正念冥想",
        "渐进式肌肉放松",
        "写日记",
        "寻求支持"
    ],
    "抑郁": [
        "保持规律作息",
        "适度运动",
        "社交活动",
        "专业帮助",
        "设定小目标"
    ],
    "愤怒": [
        "数数冷静",
        "离开现场",
        "深呼吸",
        "表达感受",
        "寻求理解"
    ],
    "压力": [
        "时间管理",
        "设定边界",
        "放松技巧",
        "寻求支持",
        "调整期望"
    ]
}


def analyze_mental_health(mbti_type, feedback_text=None, stress_level=None):
    """
    分析心理健康状况
    
    参数:
        mbti_type: MBTI类型
        feedback_text: 用户反馈文本（可选）
        stress_level: 压力水平（可选：轻度、中度、重度）
    
    返回:
        心理健康分析字典
    """
    if mbti_type not in MBTI_MENTAL_HEALTH:
        return None
    
    mbti_data = MBTI_MENTAL_HEALTH[mbti_type]
    
    analysis = {
        "mbti_type": mbti_type,
        "优势": mbti_data.get("优势", []),
        "风险": mbti_data.get("风险", []),
        "建议": mbti_data.get("建议", []),
        "压力应对": [],
        "情绪管理": [],
        "总体评估": "良好"
    }
    
    # 根据压力水平添加应对建议
    if stress_level:
        if stress_level in STRESS_COPING:
            analysis["压力应对"] = STRESS_COPING[stress_level]
        analysis["总体评估"] = f"需要关注压力管理（{stress_level}压力）"
    else:
        analysis["压力应对"] = STRESS_COPING["轻度压力"]
    
    # 根据反馈文本分析情绪
    if feedback_text:
        feedback_lower = feedback_text.lower()
        emotions = []
        
        if "焦虑" in feedback_text or "担心" in feedback_text or "紧张" in feedback_text:
            emotions.append("焦虑")
        if "抑郁" in feedback_text or "低落" in feedback_text or "沮丧" in feedback_text:
            emotions.append("抑郁")
        if "愤怒" in feedback_text or "生气" in feedback_text or "烦躁" in feedback_text:
            emotions.append("愤怒")
        if "压力" in feedback_text or "累" in feedback_text or "疲惫" in feedback_text:
            emotions.append("压力")
        
        if emotions:
            emotion_tips = []
            for emotion in emotions:
                if emotion in EMOTION_MANAGEMENT:
                    emotion_tips.extend(EMOTION_MANAGEMENT[emotion])
            analysis["情绪管理"] = list(set(emotion_tips))  # 去重
            if len(emotions) > 1:
                analysis["总体评估"] = "需要关注情绪管理"
        else:
            analysis["情绪管理"] = EMOTION_MANAGEMENT.get("压力", [])
    else:
        analysis["情绪管理"] = EMOTION_MANAGEMENT.get("压力", [])
    
    return analysis


def format_mental_health_analysis(mental_health_data):
    """
    格式化心理健康分析结果
    
    参数:
        mental_health_data: 心理健康分析字典
    
    返回:
        格式化的字符串
    """
    if not mental_health_data:
        return "无法进行心理健康分析"
    
    result = "【心理健康分析】\n\n"
    
    result += f"━━━ MBTI类型特征 ━━━\n"
    result += f"类型：{mental_health_data['mbti_type']}\n\n"
    
    result += f"心理优势：\n"
    for advantage in mental_health_data.get('优势', []):
        result += f"✓ {advantage}\n"
    result += "\n"
    
    result += f"潜在风险：\n"
    for risk in mental_health_data.get('风险', []):
        result += f"⚠ {risk}\n"
    result += "\n"
    
    result += f"建议：\n"
    for suggestion in mental_health_data.get('建议', []):
        result += f"• {suggestion}\n"
    result += "\n"
    
    if mental_health_data.get('压力应对'):
        result += f"━━━ 压力应对建议 ━━━\n"
        for tip in mental_health_data['压力应对']:
            result += f"• {tip}\n"
        result += "\n"
    
    if mental_health_data.get('情绪管理'):
        result += f"━━━ 情绪管理技巧 ━━━\n"
        for tip in mental_health_data['情绪管理']:
            result += f"• {tip}\n"
        result += "\n"
    
    result += f"━━━ 总体评估 ━━━\n"
    result += f"{mental_health_data.get('总体评估', '良好')}\n\n"
    
    return result

