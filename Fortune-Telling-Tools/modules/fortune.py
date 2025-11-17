# 运势预测模块
import random
from datetime import datetime
from config import FORTUNE_TYPES


def generate_fortune_score():
    """生成运势分数（1-100）"""
    return random.randint(1, 100)


def get_fortune_level(score):
    """
    根据分数返回运势等级
    
    参数:
        score: 运势分数（1-100）
    
    返回:
        运势等级和描述
    """
    if score >= 80:
        return "极佳", "运势非常旺盛，是采取行动的好时机！"
    elif score >= 60:
        return "良好", "运势不错，可以积极把握机会。"
    elif score >= 40:
        return "一般", "运势平稳，保持现状即可。"
    elif score >= 20:
        return "较差", "运势偏低，需要谨慎行事。"
    else:
        return "很差", "运势不佳，建议保守应对，等待时机。"


def get_fortune_description(fortune_type, score, level, zodiac, mbti):
    """
    根据运势类型、分数、等级、星座和MBTI生成运势描述
    
    参数:
        fortune_type: 运势类型（财运、感情运等）
        score: 运势分数
        level: 运势等级
        zodiac: 星座
        mbti: MBTI类型
    
    返回:
        运势描述文本
    """
    descriptions = {
        "财运": {
            "极佳": [
                f"恭喜！您的财运非常旺盛，{zodiac}的您和{mbti}的特质相结合，近期可能会有意外之财或投资机会。建议把握良机，但也要理性决策。",
                f"财运亨通！作为{zodiac}的您，配合{mbti}的思维方式，近期在财务方面会有不错的进展。可以考虑一些稳健的投资。",
            ],
            "良好": [
                f"您的财运不错，{zodiac}和{mbti}的组合让您在财务管理方面有独特的优势。继续保持理性消费，积累财富。",
                f"财运平稳上升，{zodiac}的您具有{mbti}的特质，在理财方面会有不错的收获。建议做好规划。",
            ],
            "一般": [
                f"财运平稳，{zodiac}的您需要结合{mbti}的特点，在财务管理上保持谨慎。避免冲动消费，做好预算。",
                f"财运一般，作为{zodiac}的您，配合{mbti}的思维方式，近期在财务方面不会有太大波动。保持现状即可。",
            ],
            "较差": [
                f"财运稍显低迷，{zodiac}的您需要利用{mbti}的理性思维，谨慎处理财务问题。避免高风险投资。",
                f"财运不太理想，{zodiac}和{mbti}的组合提示您近期在财务方面需要更加谨慎。建议保守理财。",
            ],
            "很差": [
                f"财运不佳，{zodiac}的您需要充分发挥{mbti}的谨慎特质，避免不必要的支出。等待更好的时机。",
                f"财运低迷，作为{zodiac}的您，配合{mbti}的特点，近期在财务方面需要格外小心。建议保守应对。",
            ],
        },
        "感情运": {
            "极佳": [
                f"感情运势极佳！{zodiac}的您和{mbti}的特质相结合，近期在感情方面会有很好的发展。单身者可能有新的邂逅，有伴者关系更加和谐。",
                f"感情运旺盛！作为{zodiac}的您，配合{mbti}的性格特点，近期在感情方面会有惊喜。多参与社交活动，展现真实的自己。",
            ],
            "良好": [
                f"感情运势不错，{zodiac}和{mbti}的组合让您在感情方面有独特的魅力。继续保持真诚和沟通，关系会越来越好。",
                f"感情运平稳上升，{zodiac}的您具有{mbti}的特质，在感情方面会有不错的进展。珍惜眼前人，用心经营。",
            ],
            "一般": [
                f"感情运势平稳，{zodiac}的您需要结合{mbti}的特点，在感情方面保持耐心和理解。沟通是关键。",
                f"感情运一般，作为{zodiac}的您，配合{mbti}的思维方式，近期在感情方面不会有太大变化。保持现状，顺其自然。",
            ],
            "较差": [
                f"感情运势稍显低迷，{zodiac}的您需要利用{mbti}的理性思维，冷静处理感情问题。避免情绪化决策。",
                f"感情运不太理想，{zodiac}和{mbti}的组合提示您近期在感情方面需要更加用心。多沟通，多理解。",
            ],
            "很差": [
                f"感情运势不佳，{zodiac}的您需要充分发挥{mbti}的理性特质，冷静面对感情问题。给自己一些时间思考。",
                f"感情运低迷，作为{zodiac}的您，配合{mbti}的特点，近期在感情方面需要格外谨慎。避免冲动决定。",
            ],
        },
        "事业运": {
            "极佳": [
                f"事业运势极佳！{zodiac}的您和{mbti}的特质相结合，近期在工作方面会有很好的机会。可能获得晋升或新的项目机会。",
                f"事业运旺盛！作为{zodiac}的您，配合{mbti}的性格特点，近期在工作方面会有突破。积极主动，展现能力。",
            ],
            "良好": [
                f"事业运势不错，{zodiac}和{mbti}的组合让您在工作方面有独特的优势。继续保持努力，会有不错的回报。",
                f"事业运平稳上升，{zodiac}的您具有{mbti}的特质，在工作方面会有不错的进展。把握机会，展现才华。",
            ],
            "一般": [
                f"事业运势平稳，{zodiac}的您需要结合{mbti}的特点，在工作方面保持稳定和耐心。继续努力，积累经验。",
                f"事业运一般，作为{zodiac}的您，配合{mbti}的思维方式，近期在工作方面不会有太大变化。保持现状，稳步发展。",
            ],
            "较差": [
                f"事业运势稍显低迷，{zodiac}的您需要利用{mbti}的理性思维，冷静面对工作挑战。寻找新的突破口。",
                f"事业运不太理想，{zodiac}和{mbti}的组合提示您近期在工作方面需要更加努力。保持耐心，等待时机。",
            ],
            "很差": [
                f"事业运势不佳，{zodiac}的您需要充分发挥{mbti}的谨慎特质，避免冒险。积累经验，等待更好的机会。",
                f"事业运低迷，作为{zodiac}的您，配合{mbti}的特点，近期在工作方面需要格外小心。保守应对，稳定发展。",
            ],
        },
        "健康运": {
            "极佳": [
                f"健康运势极佳！{zodiac}的您和{mbti}的特质相结合，近期身体状况很好。继续保持健康的生活方式，多运动，注意饮食。",
                f"健康运旺盛！作为{zodiac}的您，配合{mbti}的性格特点，近期身体状况非常不错。继续保持，注意休息。",
            ],
            "良好": [
                f"健康运势不错，{zodiac}和{mbti}的组合让您在健康方面有良好的基础。继续保持规律的生活，适度运动。",
                f"健康运平稳上升，{zodiac}的您具有{mbti}的特质，身体状况良好。注意饮食均衡，保持心情愉快。",
            ],
            "一般": [
                f"健康运势平稳，{zodiac}的您需要结合{mbti}的特点，在健康方面保持注意。注意休息，避免过度劳累。",
                f"健康运一般，作为{zodiac}的您，配合{mbti}的思维方式，近期身体状况平稳。保持现状，注意保养。",
            ],
            "较差": [
                f"健康运势稍显低迷，{zodiac}的您需要利用{mbti}的理性思维，重视健康问题。注意休息，适当调整生活方式。",
                f"健康运不太理想，{zodiac}和{mbti}的组合提示您近期在健康方面需要更加注意。多休息，避免熬夜。",
            ],
            "很差": [
                f"健康运势不佳，{zodiac}的您需要充分发挥{mbti}的谨慎特质，重视身体健康。及时就医，注意休息。",
                f"健康运低迷，作为{zodiac}的您，配合{mbti}的特点，近期在健康方面需要格外注意。保持规律作息，注意饮食。",
            ],
        },
    }
    
    if fortune_type in descriptions and level in descriptions[fortune_type]:
        options = descriptions[fortune_type][level]
        return random.choice(options)
    else:
        return f"{fortune_type}运势{level}，分数为{score}分。"


def get_fortune_prediction(zodiac, mbti):
    """
    生成运势预测
    
    参数:
        zodiac: 星座
        mbti: MBTI类型
    
    返回:
        包含各种运势预测的字典
    """
    # 设置随机种子，使同一天的运势相对稳定
    today = datetime.now().strftime("%Y-%m-%d")
    random.seed(f"{today}{zodiac}{mbti}")
    
    fortunes = {}
    
    for fortune_type in FORTUNE_TYPES:
        score = generate_fortune_score()
        level, level_desc = get_fortune_level(score)
        description = get_fortune_description(fortune_type, score, level, zodiac, mbti)
        
        fortunes[fortune_type] = {
            "score": score,
            "level": level,
            "level_desc": level_desc,
            "description": description
        }
    
    return fortunes


def format_fortune_prediction(fortunes):
    """
    格式化运势预测结果，返回用于显示的字符串
    
    参数:
        fortunes: 运势预测字典
    
    返回:
        格式化的运势预测字符串
    """
    result = "【运势预测】\n\n"
    
    for fortune_type, fortune_info in fortunes.items():
        result += f"━━━ {fortune_type} ━━━\n"
        result += f"运势等级：{fortune_info['level']} ({fortune_info['score']}分)\n"
        result += f"{fortune_info['level_desc']}\n"
        result += f"\n详细分析：\n{fortune_info['description']}\n\n"
    
    return result

