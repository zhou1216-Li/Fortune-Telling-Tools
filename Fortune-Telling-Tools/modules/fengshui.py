# 风水分析模块
import json
import os
from config import BASE_DIR

FENGSHUI_DATA_PATH = os.path.join(BASE_DIR, "modules", "data", "fengshui_data.json")

# 风水方位数据
FENGSHUI_DIRECTIONS = {
    "东": {"五行": "木", "颜色": "绿色", "代表": "成长、发展", "吉利": True},
    "南": {"五行": "火", "颜色": "红色", "代表": "热情、活力", "吉利": True},
    "西": {"五行": "金", "颜色": "白色", "代表": "收获、完成", "吉利": True},
    "北": {"五行": "水", "颜色": "黑色", "代表": "智慧、流动", "吉利": True},
    "东北": {"五行": "土", "颜色": "黄色", "代表": "稳定、基础", "吉利": True},
    "东南": {"五行": "木", "颜色": "绿色", "代表": "财运、事业", "吉利": True},
    "西南": {"五行": "土", "颜色": "黄色", "代表": "健康、稳定", "吉利": True},
    "西北": {"五行": "金", "颜色": "白色", "代表": "贵人、权力", "吉利": True},
    "中": {"五行": "土", "颜色": "黄色", "代表": "中心、平衡", "吉利": True}
}

# 房屋朝向数据
HOUSE_ORIENTATIONS = {
    "正东": {"特点": "朝阳，充满活力", "适合": "年轻人和创业者", "建议": "适合摆放绿色植物"},
    "正南": {"特点": "阳光充足，温暖", "适合": "需要温暖环境的人", "建议": "适合摆放红色装饰"},
    "正西": {"特点": "夕阳，宁静", "适合": "喜欢安静的人", "建议": "适合摆放金属装饰"},
    "正北": {"特点": "阴凉，冷静", "适合": "需要冷静思考的人", "建议": "适合摆放水元素"},
    "东北": {"特点": "稳定，基础", "适合": "需要稳定环境的人", "建议": "适合摆放黄色装饰"},
    "东南": {"特点": "财运，事业", "适合": "追求事业成功的人", "建议": "适合摆放绿色植物和财位"},
    "西南": {"特点": "健康，稳定", "适合": "注重健康的人", "建议": "适合摆放土元素"},
    "西北": {"特点": "贵人，权力", "适合": "追求权力和地位的人", "建议": "适合摆放金属装饰"}
}

# 时辰数据
TIME_PERIODS = {
    "子时": (23, 1, "水", "安静、深沉"),
    "丑时": (1, 3, "土", "稳定、基础"),
    "寅时": (3, 5, "木", "成长、发展"),
    "卯时": (5, 7, "木", "朝气、活力"),
    "辰时": (7, 9, "土", "稳定、积累"),
    "巳时": (9, 11, "火", "热情、积极"),
    "午时": (11, 13, "火", "旺盛、热烈"),
    "未时": (13, 15, "土", "稳定、收获"),
    "申时": (15, 17, "金", "收获、完成"),
    "酉时": (17, 19, "金", "收敛、完成"),
    "戌时": (19, 21, "土", "稳定、休息"),
    "亥时": (21, 23, "水", "深沉、思考")
}


def get_time_period(hour):
    """根据小时获取时辰"""
    hour = int(hour)
    for period, (start, end, element, desc) in TIME_PERIODS.items():
        if start > end:  # 跨天的情况（子时）
            if hour >= start or hour < end:
                return period, element, desc
        else:
            if start <= hour < end:
                return period, element, desc
    return "子时", "水", "安静、深沉"


def get_fengshui_analysis(residence_direction, house_orientation, birth_hour=None, zodiac=None):
    """
    获取风水分析
    
    参数:
        residence_direction: 居住方位（东、南、西、北等）
        house_orientation: 房屋朝向
        birth_hour: 出生时辰（可选）
        zodiac: 星座（可选）
    
    返回:
        风水分析字典
    """
    analysis = {
        "residence_direction": residence_direction,
        "house_orientation": house_orientation,
        "direction_info": {},
        "orientation_info": {},
        "time_info": {},
        "compatibility": {},
        "suggestions": []
    }
    
    # 方位分析
    if residence_direction in FENGSHUI_DIRECTIONS:
        analysis["direction_info"] = FENGSHUI_DIRECTIONS[residence_direction].copy()
    
    # 朝向分析
    if house_orientation in HOUSE_ORIENTATIONS:
        analysis["orientation_info"] = HOUSE_ORIENTATIONS[house_orientation].copy()
    
    # 时辰分析
    if birth_hour is not None:
        period, element, desc = get_time_period(birth_hour)
        analysis["time_info"] = {
            "period": period,
            "element": element,
            "description": desc
        }
    
    # 五行相生相克分析
    direction_element = analysis["direction_info"].get("五行", "")
    orientation_info = analysis["orientation_info"]
    time_element = analysis["time_info"].get("element", "")
    
    # 五行相生关系
    wuxing_relations = {
        "木": {"生": "火", "被生": "水", "克": "土", "被克": "金"},
        "火": {"生": "土", "被生": "木", "克": "金", "被克": "水"},
        "土": {"生": "金", "被生": "火", "克": "水", "被克": "木"},
        "金": {"生": "水", "被生": "土", "克": "木", "被克": "火"},
        "水": {"生": "木", "被生": "金", "克": "火", "被克": "土"}
    }
    
    compatibility = {
        "status": "良好",
        "description": "",
        "suggestions": []
    }
    
    if direction_element and time_element:
        if direction_element == time_element:
            compatibility["status"] = "极佳"
            compatibility["description"] = f"方位五行（{direction_element}）与出生时辰五行（{time_element}）相合，能量和谐统一。"
        elif wuxing_relations.get(direction_element, {}).get("被生") == time_element:
            compatibility["status"] = "极佳"
            compatibility["description"] = f"出生时辰五行（{time_element}）生方位五行（{direction_element}），能量相生，运势旺盛。"
        elif wuxing_relations.get(direction_element, {}).get("生") == time_element:
            compatibility["status"] = "良好"
            compatibility["description"] = f"方位五行（{direction_element}）生出生时辰五行（{time_element}），能量流通，运势平稳。"
        elif wuxing_relations.get(direction_element, {}).get("被克") == time_element:
            compatibility["status"] = "一般"
            compatibility["description"] = f"出生时辰五行（{time_element}）克方位五行（{direction_element}），需要平衡能量。"
            compatibility["suggestions"].append("建议在居住环境中添加调和元素，如摆放五行属土的装饰品。")
        elif wuxing_relations.get(direction_element, {}).get("克") == time_element:
            compatibility["status"] = "需注意"
            compatibility["description"] = f"方位五行（{direction_element}）克出生时辰五行（{time_element}），需要化解冲突。"
            compatibility["suggestions"].append("建议在居住环境中添加相生元素，平衡五行能量。")
    
    analysis["compatibility"] = compatibility
    
    # 综合建议
    suggestions = []
    
    # 方位建议
    if residence_direction in FENGSHUI_DIRECTIONS:
        direction_data = FENGSHUI_DIRECTIONS[residence_direction]
        suggestions.append(f"您的居住方位为{residence_direction}，五行属{direction_data['五行']}，适合使用{direction_data['颜色']}色系装饰。")
    
    # 朝向建议
    if house_orientation in HOUSE_ORIENTATIONS:
        orientation_data = HOUSE_ORIENTATIONS[house_orientation]
        suggestions.append(f"房屋朝向{house_orientation}，{orientation_data['特点']}，{orientation_data['建议']}。")
    
    # 时辰建议
    if birth_hour is not None:
        time_info = analysis["time_info"]
        suggestions.append(f"出生时辰为{time_info['period']}，五行属{time_info['element']}，{time_info['description']}。")
    
    # 星座建议
    if zodiac:
        zodiac_elements = {
            "白羊座": "火", "金牛座": "土", "双子座": "金", "巨蟹座": "水",
            "狮子座": "火", "处女座": "土", "天秤座": "金", "天蝎座": "水",
            "射手座": "火", "摩羯座": "土", "水瓶座": "金", "双鱼座": "水"
        }
        if zodiac in zodiac_elements:
            zodiac_element = zodiac_elements[zodiac]
            if direction_element:
                if zodiac_element == direction_element:
                    suggestions.append(f"您的星座{zodiac}五行属{zodiac_element}，与居住方位五行相合，能量和谐。")
                elif wuxing_relations.get(zodiac_element, {}).get("被生") == direction_element:
                    suggestions.append(f"您的星座{zodiac}五行属{zodiac_element}，被居住方位五行（{direction_element}）所生，运势旺盛。")
    
    # 添加兼容性建议
    if compatibility["suggestions"]:
        suggestions.extend(compatibility["suggestions"])
    
    analysis["suggestions"] = suggestions
    
    return analysis


def format_fengshui_analysis(fengshui_data):
    """
    格式化风水分析结果
    
    参数:
        fengshui_data: 风水分析字典
    
    返回:
        格式化的字符串
    """
    result = "【风水分析】\n\n"
    
    # 方位分析
    if fengshui_data.get("direction_info"):
        dir_info = fengshui_data["direction_info"]
        result += f"━━━ 居住方位 ━━━\n"
        result += f"方位：{fengshui_data['residence_direction']}\n"
        result += f"五行：{dir_info.get('五行', '')}\n"
        result += f"代表：{dir_info.get('代表', '')}\n"
        result += f"适宜颜色：{dir_info.get('颜色', '')}\n\n"
    
    # 朝向分析
    if fengshui_data.get("orientation_info"):
        ori_info = fengshui_data["orientation_info"]
        result += f"━━━ 房屋朝向 ━━━\n"
        result += f"朝向：{fengshui_data['house_orientation']}\n"
        result += f"特点：{ori_info.get('特点', '')}\n"
        result += f"适合：{ori_info.get('适合', '')}\n"
        result += f"建议：{ori_info.get('建议', '')}\n\n"
    
    # 时辰分析
    if fengshui_data.get("time_info"):
        time_info = fengshui_data["time_info"]
        result += f"━━━ 出生时辰 ━━━\n"
        result += f"时辰：{time_info.get('period', '')}\n"
        result += f"五行：{time_info.get('element', '')}\n"
        result += f"特点：{time_info.get('description', '')}\n\n"
    
    # 五行兼容性
    if fengshui_data.get("compatibility"):
        comp = fengshui_data["compatibility"]
        result += f"━━━ 五行兼容性 ━━━\n"
        result += f"状态：{comp.get('status', '')}\n"
        result += f"分析：{comp.get('description', '')}\n\n"
    
    # 综合建议
    if fengshui_data.get("suggestions"):
        result += f"━━━ 综合建议 ━━━\n"
        for i, suggestion in enumerate(fengshui_data["suggestions"], 1):
            result += f"{i}. {suggestion}\n"
        result += "\n"
    
    return result

