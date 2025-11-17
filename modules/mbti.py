# MBTI性格分析模块
import json
from config import MBTI_DATA_PATH


def load_mbti_data():
    """加载MBTI数据"""
    try:
        with open(MBTI_DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"错误：找不到MBTI数据文件 {MBTI_DATA_PATH}")
        return {}
    except json.JSONDecodeError:
        print(f"错误：MBTI数据文件格式错误 {MBTI_DATA_PATH}")
        return {}


def get_mbti_analysis(mbti_type):
    """
    获取MBTI性格分析
    
    参数:
        mbti_type: MBTI类型，如 "INTJ", "ENFP" 等
    
    返回:
        包含MBTI详细信息的字典，如果类型不存在则返回None
    """
    mbti_data = load_mbti_data()
    mbti_type = mbti_type.upper()  # 转换为大写
    
    if mbti_type in mbti_data:
        return mbti_data[mbti_type]
    else:
        return None


def get_compatibility(mbti_type):
    """
    获取MBTI类型的相容性信息
    
    参数:
        mbti_type: MBTI类型
    
    返回:
        相容性字典，包含best、good、average、poor四个级别
    """
    analysis = get_mbti_analysis(mbti_type)
    
    if analysis and 'compatibility' in analysis:
        return analysis['compatibility']
    else:
        return None


def format_mbti_analysis(mbti_type):
    """
    格式化MBTI分析结果，返回用于显示的字符串
    
    参数:
        mbti_type: MBTI类型
    
    返回:
        格式化的分析结果字符串
    """
    analysis = get_mbti_analysis(mbti_type)
    
    if not analysis:
        return f"未找到 {mbti_type} 的相关信息"
    
    result = f"【{analysis['name']} - {analysis['full_name']}】\n\n"
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
    
    # 添加相容性信息
    compatibility = get_compatibility(mbti_type)
    if compatibility:
        result += "\n相容性分析：\n"
        result += f"最佳配对：{', '.join(compatibility['best'])}\n"
        result += f"良好配对：{', '.join(compatibility['good'])}\n"
        result += f"一般配对：{', '.join(compatibility['average'])}\n"
        result += f"较差配对：{', '.join(compatibility['poor'])}\n"
    
    return result


def get_all_mbti_types():
    """获取所有MBTI类型列表"""
    mbti_data = load_mbti_data()
    return list(mbti_data.keys())

