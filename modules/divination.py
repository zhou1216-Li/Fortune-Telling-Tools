# 多命理学分析模块
"""
支持多种命理学分析方法：八字、塔罗牌等
"""

import random
from datetime import datetime

# 八字天干
TIAN_GAN = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]

# 八字地支
DI_ZHI = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

# 五行
WU_XING = ["金", "木", "水", "火", "土"]

# 天干五行对应
TIAN_GAN_WUXING = {
    "甲": "木", "乙": "木",
    "丙": "火", "丁": "火",
    "戊": "土", "己": "土",
    "庚": "金", "辛": "金",
    "壬": "水", "癸": "水"
}

# 地支五行对应
DI_ZHI_WUXING = {
    "子": "水", "丑": "土", "寅": "木", "卯": "木",
    "辰": "土", "巳": "火", "午": "火", "未": "土",
    "申": "金", "酉": "金", "戌": "土", "亥": "水"
}

# 塔罗牌数据
TAROT_CARDS = {
    "大阿卡纳": {
        "0.愚者": {"意义": "新的开始", "正位": "冒险、新的开始", "逆位": "鲁莽、冒险"},
        "1.魔术师": {"意义": "创造力", "正位": "创造力、行动力", "逆位": "缺乏创造力、拖延"},
        "2.女祭司": {"意义": "直觉", "正位": "直觉、智慧", "逆位": "缺乏直觉、困惑"},
        "3.皇后": {"意义": "丰饶", "正位": "丰饶、母性", "逆位": "过度依赖、缺乏创造力"},
        "4.皇帝": {"意义": "权威", "正位": "权威、秩序", "逆位": "独裁、缺乏秩序"},
        "5.教皇": {"意义": "传统", "正位": "传统、指导", "逆位": "反传统、缺乏指导"},
        "6.恋人": {"意义": "爱情", "正位": "爱情、选择", "逆位": "爱情困扰、错误选择"},
        "7.战车": {"意义": "胜利", "正位": "胜利、控制", "逆位": "失败、失去控制"},
        "8.力量": {"意义": "力量", "正位": "内在力量、勇气", "逆位": "软弱、缺乏勇气"},
        "9.隐者": {"意义": "寻求", "正位": "寻求真理、内省", "逆位": "孤独、逃避"},
        "10.命运之轮": {"意义": "命运", "正位": "命运转变、机会", "逆位": "坏运气、错过机会"},
        "11.正义": {"意义": "正义", "正位": "正义、平衡", "逆位": "不公正、失衡"},
        "12.倒吊人": {"意义": "牺牲", "正位": "牺牲、等待", "逆位": "无意义的牺牲、拖延"},
        "13.死神": {"意义": "结束", "正位": "结束、转变", "逆位": "抗拒改变、停滞"},
        "14.节制": {"意义": "平衡", "正位": "平衡、调和", "逆位": "失衡、过度"},
        "15.恶魔": {"意义": "束缚", "正位": "束缚、诱惑", "逆位": "解脱、自由"},
        "16.塔": {"意义": "破坏", "正位": "破坏、 revelation", "逆位": "避免灾难、抗拒改变"},
        "17.星星": {"意义": "希望", "正位": "希望、灵感", "逆位": "绝望、缺乏希望"},
        "18.月亮": {"意义": "幻觉", "正位": "幻觉、恐惧", "逆位": " clarity、克服恐惧"},
        "19.太阳": {"意义": "快乐", "正位": "快乐、成功", "逆位": "过度乐观、缺乏成功"},
        "20.审判": {"意义": "复活", "正位": "复活、 judgment", "逆位": "缺乏判断、拖延"},
        "21.世界": {"意义": "完成", "正位": "完成、成功", "逆位": "未完成、缺乏成功"}
    }
}


def calculate_bazi(birthday, birth_hour=None):
    """
    计算八字
    
    参数:
        birthday: 生日（YYYY-MM-DD格式）
        birth_hour: 出生时辰（0-23，可选）
    
    返回:
        八字字典
    """
    try:
        from datetime import datetime
        birth_date = datetime.strptime(birthday, "%Y-%m-%d")
        year = birth_date.year
        month = birth_date.month
        day = birth_date.day
        hour = birth_hour if birth_hour is not None else 12
        
        # 简化版的八字计算（实际八字计算更复杂）
        # 这里使用年份、月份、日期、时辰的简化算法
        
        # 年柱 - 使用公历年份计算
        # 简化算法：1900年为庚子年
        base_year = 1900
        base_gan_index = 6  # 庚
        base_zhi_index = 0  # 子
        
        year_diff = year - base_year
        year_gan_index = (base_gan_index + year_diff) % 10
        year_zhi_index = (base_zhi_index + year_diff) % 12
        year_gan = TIAN_GAN[year_gan_index]
        year_zhi = DI_ZHI[year_zhi_index]
        
        # 月柱（简化）- 根据年干和月份计算
        # 月支：正月寅、二月卯...十二月丑
        month_zhi_index = (month + 1) % 12
        month_zhi = DI_ZHI[month_zhi_index]
        # 月干：根据年干和月份计算（简化算法）
        month_gan_index = (year_gan_index * 2 + month) % 10
        month_gan = TIAN_GAN[month_gan_index]
        
        # 日柱（简化）- 使用简化算法
        # 1900年1月1日为甲子日
        from datetime import date
        base_date = date(1900, 1, 1)
        target_date = date(year, month, day)
        days_diff = (target_date - base_date).days
        day_gan_index = (days_diff + 0) % 10  # 甲为0
        day_zhi_index = (days_diff + 0) % 12  # 子为0
        day_gan = TIAN_GAN[day_gan_index]
        day_zhi = DI_ZHI[day_zhi_index]
        
        # 时柱（简化）
        # 时支：子时(23-1)、丑时(1-3)...亥时(21-23)
        hour_zhi_index = ((hour + 1) // 2) % 12
        hour_zhi = DI_ZHI[hour_zhi_index]
        # 时干：根据日干和时支计算（简化算法：日上起时）
        hour_gan_index = (day_gan_index * 2 + hour_zhi_index) % 10
        hour_gan = TIAN_GAN[hour_gan_index]
        
        # 分析五行
        wuxing_distribution = {}
        for gan in [year_gan, month_gan, day_gan, hour_gan]:
            wuxing = TIAN_GAN_WUXING.get(gan, "")
            if wuxing:
                wuxing_distribution[wuxing] = wuxing_distribution.get(wuxing, 0) + 1
        
        for zhi in [year_zhi, month_zhi, day_zhi, hour_zhi]:
            wuxing = DI_ZHI_WUXING.get(zhi, "")
            if wuxing:
                wuxing_distribution[wuxing] = wuxing_distribution.get(wuxing, 0) + 1
        
        bazi = {
            "year": f"{year_gan}{year_zhi}",
            "month": f"{month_gan}{month_zhi}",
            "day": f"{day_gan}{day_zhi}",
            "hour": f"{hour_gan}{hour_zhi}",
            "wuxing_distribution": wuxing_distribution,
            "day_pillar": f"{day_gan}{day_zhi}",  # 日柱（最重要）
            "day_gan": day_gan,
            "day_zhi": day_zhi
        }
        
        return bazi
    except Exception as e:
        print(f"计算八字失败: {e}")
        import traceback
        traceback.print_exc()
        return None


def analyze_bazi(bazi_data):
    """
    分析八字
    
    参数:
        bazi_data: 八字数据字典
    
    返回:
        八字分析结果
    """
    if not bazi_data:
        return None
    
    analysis = {
        "bazi": bazi_data,
        "wuxing_analysis": "",
        "personality": "",
        "fortune": "",
        "suggestions": []
    }
    
    # 五行分析
    wuxing_dist = bazi_data.get("wuxing_distribution", {})
    dominant_wuxing = max(wuxing_dist, key=wuxing_dist.get) if wuxing_dist else "土"
    
    wuxing_meanings = {
        "金": "刚强、果断、有原则",
        "木": "成长、发展、有活力",
        "水": "智慧、流动、适应性强",
        "火": "热情、积极、有创造力",
        "土": "稳定、务实、可靠"
    }
    
    analysis["wuxing_analysis"] = f"您的八字中{dominant_wuxing}元素较多，性格特点：{wuxing_meanings.get(dominant_wuxing, '')}"
    
    # 日柱分析
    day_gan = bazi_data.get("day_gan", "")
    day_zhi = bazi_data.get("day_zhi", "")
    
    if day_gan:
        gan_meanings = {
            "甲": "阳木，有领导力，积极向上",
            "乙": "阴木，柔韧，善于适应",
            "丙": "阳火，热情，有创造力",
            "丁": "阴火，细腻，有耐心",
            "戊": "阳土，稳重，可靠",
            "己": "阴土，包容，有同理心",
            "庚": "阳金，刚强，有原则",
            "辛": "阴金，精致，有品味",
            "壬": "阳水，智慧，适应性强",
            "癸": "阴水，细腻，有直觉"
        }
        analysis["personality"] = gan_meanings.get(day_gan, "")
    
    # 运势建议
    analysis["suggestions"] = [
        f"根据八字分析，您的五行以{dominant_wuxing}为主，建议：",
        f"1. 发挥{dominant_wuxing}元素的优势",
        f"2. 注意五行平衡，适当补充其他元素",
        f"3. 根据日柱特点，发挥个人优势"
    ]
    
    return analysis


def draw_tarot_card():
    """
    抽取塔罗牌
    
    返回:
        塔罗牌信息字典
    """
    major_arcana = list(TAROT_CARDS["大阿卡纳"].keys())
    card_name = random.choice(major_arcana)
    is_upright = random.choice([True, False])
    
    card_data = TAROT_CARDS["大阿卡纳"][card_name]
    
    return {
        "card_name": card_name,
        "is_upright": is_upright,
        "meaning": card_data["意义"],
        "interpretation": card_data["正位"] if is_upright else card_data["逆位"],
        "direction": "正位" if is_upright else "逆位"
    }


def analyze_tarot_reading(cards_count=3):
    """
    进行塔罗牌占卜
    
    参数:
        cards_count: 抽牌数量（默认3张）
    
    返回:
        塔罗牌占卜结果
    """
    cards = []
    for i in range(cards_count):
        card = draw_tarot_card()
        cards.append(card)
    
    # 根据牌的位置解释
    positions = ["过去", "现在", "未来"][:cards_count]
    
    reading = {
        "cards": cards,
        "positions": positions,
        "overall_meaning": "",
        "suggestions": []
    }
    
    # 综合分析
    upright_count = sum(1 for card in cards if card["is_upright"])
    if upright_count >= cards_count * 0.7:
        reading["overall_meaning"] = "整体运势积极，保持当前方向"
    elif upright_count >= cards_count * 0.3:
        reading["overall_meaning"] = "运势平稳，需要关注变化"
    else:
        reading["overall_meaning"] = "需要关注挑战，保持谨慎"
    
    reading["suggestions"] = [
        "根据塔罗牌指引，保持开放心态",
        "关注当前状况，做好准备",
        "相信自己的直觉",
        "保持积极心态，迎接变化"
    ]
    
    return reading


def format_bazi_analysis(bazi_analysis):
    """
    格式化八字分析结果
    
    参数:
        bazi_analysis: 八字分析字典
    
    返回:
        格式化的字符串
    """
    if not bazi_analysis:
        return "无法进行八字分析"
    
    result = "【八字命理分析】\n\n"
    
    bazi_data = bazi_analysis.get("bazi", {})
    result += f"━━━ 八字 ━━━\n"
    result += f"年柱：{bazi_data.get('year', '')}\n"
    result += f"月柱：{bazi_data.get('month', '')}\n"
    result += f"日柱：{bazi_data.get('day', '')}\n"
    result += f"时柱：{bazi_data.get('hour', '')}\n\n"
    
    result += f"━━━ 五行分布 ━━━\n"
    wuxing_dist = bazi_data.get("wuxing_distribution", {})
    for wuxing, count in wuxing_dist.items():
        result += f"{wuxing}：{count}个\n"
    result += "\n"
    
    result += f"━━━ 性格分析 ━━━\n"
    result += f"{bazi_analysis.get('wuxing_analysis', '')}\n"
    result += f"{bazi_analysis.get('personality', '')}\n\n"
    
    result += f"━━━ 建议 ━━━\n"
    for suggestion in bazi_analysis.get('suggestions', []):
        result += f"{suggestion}\n"
    result += "\n"
    
    return result


def format_tarot_reading(tarot_reading):
    """
    格式化塔罗牌占卜结果
    
    参数:
        tarot_reading: 塔罗牌占卜字典
    
    返回:
        格式化的字符串
    """
    if not tarot_reading:
        return "无法进行塔罗牌占卜"
    
    result = "【塔罗牌占卜】\n\n"
    
    cards = tarot_reading.get("cards", [])
    positions = tarot_reading.get("positions", [])
    
    for i, (card, position) in enumerate(zip(cards, positions)):
        result += f"━━━ {position} ━━━\n"
        result += f"牌名：{card['card_name']}\n"
        result += f"方向：{card['direction']}\n"
        result += f"意义：{card['meaning']}\n"
        result += f"解释：{card['interpretation']}\n\n"
    
    result += f"━━━ 整体分析 ━━━\n"
    result += f"{tarot_reading.get('overall_meaning', '')}\n\n"
    
    result += f"━━━ 建议 ━━━\n"
    for suggestion in tarot_reading.get('suggestions', []):
        result += f"• {suggestion}\n"
    result += "\n"
    
    return result

