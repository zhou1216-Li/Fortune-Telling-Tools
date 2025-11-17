# 情感分析与情绪预测模块
"""
基于用户输入的文字和历史反馈数据分析情感状态
"""

import re
from datetime import datetime

# 情感关键词库
EMOTION_KEYWORDS = {
    "积极": ["开心", "快乐", "高兴", "兴奋", "满足", "愉悦", "幸福", "乐观", "积极", "愉快", "满意", "喜欢", "爱", "期待", "希望"],
    "消极": ["难过", "悲伤", "沮丧", "失望", "绝望", "痛苦", "伤心", "低落", "郁闷", "消极", "悲观", "讨厌", "恨", "恐惧", "担心"],
    "焦虑": ["焦虑", "紧张", "担心", "不安", "害怕", "恐惧", "担忧", "急躁", "烦躁", "压力", "压力大", "紧张", "慌乱"],
    "愤怒": ["生气", "愤怒", "恼火", "烦躁", "不满", "怨恨", "讨厌", "厌恶", "愤恨", "怒火", "暴躁"],
    "平静": ["平静", "放松", "安心", "舒适", "满足", "宁静", "平和", "淡定", "冷静", "稳定"],
    "疲惫": ["累", "疲惫", "疲倦", "疲劳", "困", "乏力", "无精打采", "精疲力尽", " exhaustion"],
    "孤独": ["孤独", "寂寞", "孤单", "孤立", "独自", "一个人", "没人理解", "被忽视"],
    "迷茫": ["迷茫", "困惑", "不确定", "不知道", "疑惑", "迷失", "找不到方向", "不知所措"]
}

# 情绪预测规则
EMOTION_PREDICTION = {
    "积极": {
        "未来趋势": "情绪可能会继续保持积极，建议保持当前状态",
        "建议": ["保持积极心态", "继续当前活动", "分享快乐", "记录美好时刻"]
    },
    "消极": {
        "未来趋势": "情绪可能会逐渐改善，建议寻求支持和帮助",
        "建议": ["寻求朋友支持", "进行放松活动", "关注积极事物", "寻求专业帮助"]
    },
    "焦虑": {
        "未来趋势": "焦虑可能会持续，建议学习应对技巧",
        "建议": ["深呼吸练习", "正念冥想", "时间管理", "寻求支持", "专业咨询"]
    },
    "愤怒": {
        "未来趋势": "愤怒可能会逐渐平息，建议冷静处理",
        "建议": ["冷静思考", "表达感受", "寻求理解", "避免冲动", "寻找解决方案"]
    },
    "疲惫": {
        "未来趋势": "疲惫可能会持续，建议充分休息",
        "建议": ["充足睡眠", "适度休息", "减少压力", "调整作息", "寻求帮助"]
    },
    "孤独": {
        "未来趋势": "孤独感可能会改善，建议加强社交",
        "建议": ["主动社交", "参与活动", "寻求支持", "培养兴趣", "建立联系"]
    },
    "迷茫": {
        "未来趋势": "迷茫可能会逐渐清晰，建议寻求指导",
        "建议": ["设定目标", "寻求建议", "学习知识", "尝试新事物", "保持耐心"]
    }
}


def analyze_emotion(text):
    """
    分析文本中的情感
    
    参数:
        text: 文本内容
    
    返回:
        情感分析结果字典
    """
    if not text:
        return None
    
    text_lower = text.lower()
    
    # 计算各情感类型的得分
    emotion_scores = {}
    for emotion, keywords in EMOTION_KEYWORDS.items():
        score = 0
        for keyword in keywords:
            if keyword in text_lower:
                score += 1
        emotion_scores[emotion] = score
    
    # 确定主要情感
    if max(emotion_scores.values()) == 0:
        main_emotion = "平静"
        emotion_level = "中性"
    else:
        main_emotion = max(emotion_scores, key=emotion_scores.get)
        total_score = sum(emotion_scores.values())
        emotion_score = emotion_scores[main_emotion]
        
        if emotion_score / total_score >= 0.5:
            emotion_level = "强烈"
        elif emotion_score / total_score >= 0.3:
            emotion_level = "中等"
        else:
            emotion_level = "轻微"
    
    # 获取情绪预测
    prediction = EMOTION_PREDICTION.get(main_emotion, {
        "未来趋势": "情绪状态稳定",
        "建议": ["保持当前状态", "关注情绪变化"]
    })
    
    result = {
        "main_emotion": main_emotion,
        "emotion_level": emotion_level,
        "emotion_scores": emotion_scores,
        "prediction": prediction,
        "analysis_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return result


def predict_emotion_trend(emotion_history):
    """
    预测情绪趋势
    
    参数:
        emotion_history: 情绪历史记录列表
    
    返回:
        情绪趋势预测
    """
    if not emotion_history or len(emotion_history) < 2:
        return "数据不足，无法预测趋势"
    
    # 简单的趋势分析
    recent_emotions = [record.get('main_emotion', '平静') for record in emotion_history[-5:]]
    
    positive_count = sum(1 for e in recent_emotions if e in ["积极", "平静"])
    negative_count = sum(1 for e in recent_emotions if e in ["消极", "焦虑", "愤怒", "疲惫", "孤独", "迷茫"])
    
    if positive_count > negative_count:
        trend = "情绪趋势向好，保持积极心态"
    elif negative_count > positive_count:
        trend = "情绪趋势需要关注，建议寻求支持"
    else:
        trend = "情绪状态稳定，保持当前状态"
    
    return trend


def format_emotion_analysis(emotion_data):
    """
    格式化情感分析结果
    
    参数:
        emotion_data: 情感分析数据字典
    
    返回:
        格式化的字符串
    """
    if not emotion_data:
        return "无法进行情感分析"
    
    result = "【情感分析】\n\n"
    
    result += f"━━━ 当前情感状态 ━━━\n"
    result += f"主要情感：{emotion_data['main_emotion']}\n"
    result += f"情感强度：{emotion_data['emotion_level']}\n"
    result += f"分析时间：{emotion_data['analysis_time']}\n\n"
    
    result += f"━━━ 情感分布 ━━━\n"
    for emotion, score in emotion_data['emotion_scores'].items():
        if score > 0:
            result += f"{emotion}：{score}分\n"
    result += "\n"
    
    result += f"━━━ 情绪预测 ━━━\n"
    prediction = emotion_data.get('prediction', {})
    result += f"未来趋势：{prediction.get('未来趋势', '')}\n\n"
    
    result += f"建议：\n"
    for suggestion in prediction.get('建议', []):
        result += f"• {suggestion}\n"
    result += "\n"
    
    return result

