# 个人化推荐系统模块
"""
基于用户的历史运势预测和反馈数据，推荐个性化的内容或建议
"""

# 推荐内容库
RECOMMENDATIONS = {
    "财运较差": {
        "财务管理": [
            "《富爸爸穷爸爸》- 提升财商意识",
            "《小狗钱钱》- 理财入门书籍",
            "制定预算计划，控制支出",
            "学习投资基础知识",
            "建立紧急基金"
        ],
        "自我提升": [
            "学习新技能，提高竞争力",
            "参加财务管理课程",
            "阅读理财博客和文章",
            "寻找副业机会",
            "提升工作效率"
        ]
    },
    "感情运较差": {
        "情感建议": [
            "《爱的五种语言》- 了解爱的表达方式",
            "提升沟通技巧",
            "学会表达情感",
            "关注对方需求",
            "保持耐心和理解"
        ],
        "自我提升": [
            "提升自信",
            "改善个人形象",
            "培养兴趣爱好",
            "扩展社交圈子",
            "学习情感管理"
        ]
    },
    "事业运较差": {
        "职业发展": [
            "《原则》- 职业发展指南",
            "提升专业技能",
            "学习时间管理",
            "建立职业网络",
            "寻求 mentor 指导"
        ],
        "自我提升": [
            "参加职业培训",
            "阅读行业资讯",
            "提升领导力",
            "改善工作方法",
            "设定职业目标"
        ]
    },
    "健康运较差": {
        "健康管理": [
            "《健康生活指南》- 健康管理书籍",
            "规律作息时间",
            "适度运动",
            "健康饮食",
            "定期体检"
        ],
        "生活方式": [
            "减少压力",
            "保持乐观心态",
            "充足睡眠",
            "避免不良习惯",
            "寻求专业建议"
        ]
    },
    "情感匹配度较低": {
        "关系改善": [
            "《非暴力沟通》- 改善沟通方式",
            "学习倾听技巧",
            "表达真实感受",
            "寻找共同兴趣",
            "给予对方空间"
        ],
        "自我提升": [
            "提升情商",
            "学习冲突解决",
            "改善沟通方式",
            "理解对方需求",
            "保持耐心"
        ]
    },
    "生活匹配度较低": {
        "生活建议": [
            "寻找共同生活方式",
            "尊重彼此习惯",
            "协商生活安排",
            "创造共同回忆",
            "保持开放心态"
        ],
        "自我提升": [
            "适应能力",
            "灵活性",
            "包容心",
            "沟通技巧",
            "理解能力"
        ]
    },
    "事业匹配度较低": {
        "职业建议": [
            "寻找互补的工作伙伴",
            "学习团队合作",
            "理解不同工作风格",
            "寻找共同目标",
            "建立有效沟通"
        ],
        "自我提升": [
            "团队协作能力",
            "沟通技巧",
            "适应能力",
            "职业素养",
            "学习能力"
        ]
    }
}


def get_recommendations(fortune_prediction, compatibility_result=None, user_feedback=None):
    """
    根据运势预测和匹配度分析生成个性化推荐
    
    参数:
        fortune_prediction: 运势预测字典
        compatibility_result: 匹配度分析结果（可选）
        user_feedback: 用户反馈文本（可选）
    
    返回:
        推荐内容字典
    """
    recommendations = {
        "财务管理": [],
        "情感建议": [],
        "职业发展": [],
        "健康管理": [],
        "关系改善": [],
        "生活建议": [],
        "职业建议": [],
        "自我提升": []
    }
    
    # 根据运势预测推荐
    if fortune_prediction:
        for fortune_type, fortune_info in fortune_prediction.items():
            level = fortune_info.get('level', '一般')
            score = fortune_info.get('score', 50)
            
            if score < 40:  # 运势较差
                if fortune_type == "财运":
                    key = "财运较差"
                    if key in RECOMMENDATIONS:
                        recommendations["财务管理"].extend(RECOMMENDATIONS[key].get("财务管理", []))
                        recommendations["自我提升"].extend(RECOMMENDATIONS[key].get("自我提升", []))
                elif fortune_type == "感情运":
                    key = "感情运较差"
                    if key in RECOMMENDATIONS:
                        recommendations["情感建议"].extend(RECOMMENDATIONS[key].get("情感建议", []))
                        recommendations["自我提升"].extend(RECOMMENDATIONS[key].get("自我提升", []))
                elif fortune_type == "事业运":
                    key = "事业运较差"
                    if key in RECOMMENDATIONS:
                        recommendations["职业发展"].extend(RECOMMENDATIONS[key].get("职业发展", []))
                        recommendations["自我提升"].extend(RECOMMENDATIONS[key].get("自我提升", []))
                elif fortune_type == "健康运":
                    key = "健康运较差"
                    if key in RECOMMENDATIONS:
                        recommendations["健康管理"].extend(RECOMMENDATIONS[key].get("健康管理", []))
                        recommendations["生活方式"] = RECOMMENDATIONS[key].get("生活方式", [])
    
    # 根据匹配度分析推荐（如果提供了匹配度数据）
    # 注意：这里的compatibility_result参数是可选的，只在匹配度分析页面使用
    # 在分析预测页面不提供此参数
    
    # 根据用户反馈推荐
    if user_feedback:
        feedback_lower = user_feedback.lower()
        if "财务" in feedback_lower or "钱" in feedback_lower or "理财" in feedback_lower:
            recommendations["财务管理"].extend([
                "学习理财知识",
                "制定财务计划",
                "控制消费支出"
            ])
        if "感情" in feedback_lower or "恋爱" in feedback_lower or "关系" in feedback_lower:
            recommendations["情感建议"].extend([
                "学习情感沟通",
                "理解对方需求",
                "表达真实感受"
            ])
        if "工作" in feedback_lower or "事业" in feedback_lower or "职业" in feedback_lower:
            recommendations["职业发展"].extend([
                "提升职业技能",
                "寻找发展机会",
                "建立职业网络"
            ])
        if "健康" in feedback_lower or "身体" in feedback_lower or "疾病" in feedback_lower:
            recommendations["健康管理"].extend([
                "保持规律作息",
                "适度运动",
                "健康饮食"
            ])
    
    # 去重并限制数量
    for key in recommendations:
        recommendations[key] = list(set(recommendations[key]))[:5]  # 每个类别最多5条
    
    return recommendations


def format_recommendations(recommendations):
    """
    格式化推荐内容
    
    参数:
        recommendations: 推荐内容字典
    
    返回:
        格式化的字符串
    """
    result = "【个人化推荐】\n\n"
    
    has_recommendations = False
    
    for category, items in recommendations.items():
        if items:
            has_recommendations = True
            result += f"━━━ {category} ━━━\n"
            for i, item in enumerate(items, 1):
                result += f"{i}. {item}\n"
            result += "\n"
    
    if not has_recommendations:
        result += "根据您的运势分析，当前状态良好，建议继续保持！\n"
        result += "• 保持积极心态\n"
        result += "• 继续努力\n"
        result += "• 享受生活\n\n"
    
    return result

