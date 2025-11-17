# 星座分析模块
import json
from datetime import datetime
from config import ZODIAC_DATA_PATH


def load_zodiac_data():
    """加载星座数据"""
    try:
        with open(ZODIAC_DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"错误：找不到星座数据文件 {ZODIAC_DATA_PATH}")
        return {}
    except json.JSONDecodeError:
        print(f"错误：星座数据文件格式错误 {ZODIAC_DATA_PATH}")
        return {}


def get_zodiac(birthday):
    """
    根据生日判断星座
    
    参数:
        birthday: 生日字符串，格式为 "YYYY-MM-DD" 或 "MM-DD"
    
    返回:
        星座名称，如果无法判断则返回None
    """
    try:
        # 处理不同的日期格式
        if len(birthday) == 10:  # YYYY-MM-DD
            month_day = birthday[5:]
        elif len(birthday) == 5:  # MM-DD
            month_day = birthday
        else:
            return None
        
        month, day = map(int, month_day.split('-'))
        
        # 星座日期范围
        zodiac_dates = [
            (1, 20, "摩羯座", "水瓶座"),
            (2, 19, "水瓶座", "双鱼座"),
            (3, 21, "双鱼座", "白羊座"),
            (4, 20, "白羊座", "金牛座"),
            (5, 21, "金牛座", "双子座"),
            (6, 22, "双子座", "巨蟹座"),
            (7, 23, "巨蟹座", "狮子座"),
            (8, 23, "狮子座", "处女座"),
            (9, 23, "处女座", "天秤座"),
            (10, 24, "天秤座", "天蝎座"),
            (11, 23, "天蝎座", "射手座"),
            (12, 22, "射手座", "摩羯座"),
        ]
        
        # 判断星座
        for m, d, prev_zodiac, next_zodiac in zodiac_dates:
            if month == m:
                if day >= d:
                    return next_zodiac
                else:
                    return prev_zodiac
        
        # 处理12月22日到1月19日的摩羯座
        if month == 12 and day >= 22:
            return "摩羯座"
        elif month == 1 and day < 20:
            return "摩羯座"
        
        return None
    except (ValueError, IndexError):
        return None


def get_zodiac_analysis(zodiac):
    """
    获取星座性格分析
    
    参数:
        zodiac: 星座名称
    
    返回:
        包含星座详细信息的字典，如果星座不存在则返回None
    """
    zodiac_data = load_zodiac_data()
    
    if zodiac in zodiac_data:
        return zodiac_data[zodiac]
    else:
        return None


def format_zodiac_analysis(zodiac):
    """
    格式化星座分析结果，返回用于显示的字符串
    
    参数:
        zodiac: 星座名称
    
    返回:
        格式化的分析结果字符串
    """
    analysis = get_zodiac_analysis(zodiac)
    
    if not analysis:
        return f"未找到 {zodiac} 的相关信息"
    
    result = f"【{analysis['name']}】\n\n"
    result += f"日期范围：{analysis['date_range']}\n"
    result += f"星座属性：{analysis['element']}\n\n"
    result += f"性格描述：\n{analysis['description']}\n\n"
    
    result += "性格特质：\n"
    for trait in analysis['personality_traits']:
        result += f"• {trait}\n"
    
    result += "\n优点：\n"
    for strength in analysis['strengths']:
        result += f"✓ {strength}\n"
    
    result += "\n缺点：\n"
    for weakness in analysis['weaknesses']:
        result += f"✗ {weakness}\n"
    
    return result

