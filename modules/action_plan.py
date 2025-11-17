# 行动计划生成模块
"""
根据运势预测结果生成具体的行动计划
"""

def generate_action_plan(fortune_prediction, zodiac, mbti):
    """
    根据运势预测生成行动计划
    
    参数:
        fortune_prediction: 运势预测字典
        zodiac: 星座
        mbti: MBTI类型
    
    返回:
        行动计划字典
    """
    action_plan = {
        "财运": [],
        "感情运": [],
        "事业运": [],
        "健康运": [],
        "综合建议": []
    }
    
    if not fortune_prediction:
        return action_plan
    
    # 根据各运势类型生成行动计划
    for fortune_type, fortune_info in fortune_prediction.items():
        level = fortune_info.get('level', '一般')
        score = fortune_info.get('score', 50)
        
        if fortune_type == "财运":
            if score >= 80:
                action_plan["财运"] = [
                    "把握投资机会，但需谨慎分析",
                    "考虑长期投资计划",
                    "扩大收入来源",
                    "学习理财知识",
                    "保持理性消费"
                ]
            elif score >= 60:
                action_plan["财运"] = [
                    "制定理财计划",
                    "控制不必要支出",
                    "寻找额外收入机会",
                    "学习投资知识",
                    "建立紧急基金"
                ]
            elif score >= 40:
                action_plan["财运"] = [
                    "严格控制支出",
                    "避免高风险投资",
                    "寻找稳定收入来源",
                    "学习财务管理",
                    "建立预算计划"
                ]
            else:
                action_plan["财运"] = [
                    "保守理财，避免冲动消费",
                    "减少非必要支出",
                    "寻找稳定工作",
                    "学习财务知识",
                    "建立紧急储备"
                ]
        
        elif fortune_type == "感情运":
            if score >= 80:
                action_plan["感情运"] = [
                    "主动表达情感",
                    "安排浪漫约会",
                    "加深感情交流",
                    "分享生活乐趣",
                    "规划未来 together"
                ]
            elif score >= 60:
                action_plan["感情运"] = [
                    "加强沟通交流",
                    "关注对方需求",
                    "创造共同回忆",
                    "表达真实感受",
                    "保持耐心和理解"
                ]
            elif score >= 40:
                action_plan["感情运"] = [
                    "改善沟通方式",
                    "学会倾听",
                    "表达真实感受",
                    "寻找共同兴趣",
                    "给予彼此空间"
                ]
            else:
                action_plan["感情运"] = [
                    "保持冷静，避免冲突",
                    "学习情感管理",
                    "寻求专业建议",
                    "改善沟通技巧",
                    "给予彼此时间"
                ]
        
        elif fortune_type == "事业运":
            if score >= 80:
                action_plan["事业运"] = [
                    "把握工作机会",
                    "展现领导能力",
                    "提出创新想法",
                    "建立职业网络",
                    "设定更高目标"
                ]
            elif score >= 60:
                action_plan["事业运"] = [
                    "提升工作技能",
                    "加强团队合作",
                    "寻找发展机会",
                    "建立职业关系",
                    "设定职业目标"
                ]
            elif score >= 40:
                action_plan["事业运"] = [
                    "保持稳定工作",
                    "学习新技能",
                    "改善工作方法",
                    "寻求 mentor 指导",
                    "规划职业发展"
                ]
            else:
                action_plan["事业运"] = [
                    "保持耐心，等待时机",
                    "提升自身能力",
                    "寻找新的机会",
                    "学习职业技能",
                    "建立职业网络"
                ]
        
        elif fortune_type == "健康运":
            if score >= 80:
                action_plan["健康运"] = [
                    "保持健康习惯",
                    "适度运动",
                    "规律作息",
                    "健康饮食",
                    "定期体检"
                ]
            elif score >= 60:
                action_plan["健康运"] = [
                    "改善生活习惯",
                    "增加运动量",
                    "保持规律作息",
                    "注意饮食健康",
                    "关注身体状况"
                ]
            elif score >= 40:
                action_plan["健康运"] = [
                    "重视健康问题",
                    "调整生活方式",
                    "减少压力",
                    "保持充足睡眠",
                    "寻求医疗建议"
                ]
            else:
                action_plan["健康运"] = [
                    "立即关注健康",
                    "调整作息时间",
                    "减少压力来源",
                    "寻求专业医疗建议",
                    "改善生活方式"
                ]
    
    # 生成综合建议
    total_score = sum([info.get('score', 50) for info in fortune_prediction.values()]) / len(fortune_prediction)
    
    if total_score >= 75:
        action_plan["综合建议"] = [
            "运势整体良好，继续保持积极心态",
            "把握机会，实现目标",
            "保持平衡，享受生活",
            "继续努力，追求卓越"
        ]
    elif total_score >= 60:
        action_plan["综合建议"] = [
            "运势平稳，保持现状",
            "寻找改进机会",
            "保持积极心态",
            "继续努力"
        ]
    else:
        action_plan["综合建议"] = [
            "运势需要关注，保持耐心",
            "调整心态，积极面对",
            "寻找改善方法",
            "保持乐观，等待时机"
        ]
    
    return action_plan


def format_action_plan(action_plan):
    """
    格式化行动计划
    
    参数:
        action_plan: 行动计划字典
    
    返回:
        格式化的字符串
    """
    result = "【行动计划】\n\n"
    
    for category, actions in action_plan.items():
        if actions:
            result += f"━━━ {category}行动计划 ━━━\n"
            for i, action in enumerate(actions, 1):
                result += f"{i}. {action}\n"
            result += "\n"
    
    return result

