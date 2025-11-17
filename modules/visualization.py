# 可视化分析模块
import plotly.graph_objs as go
import plotly.offline as pyo

def create_compatibility_chart(compatibility_result):
    """
    创建匹配度分析图表
    
    参数:
        compatibility_result: 匹配度分析结果字典，包含情感匹配、生活匹配、事业匹配
    
    返回:
        HTML格式的图表
    """
    if not compatibility_result:
        return None
    
    try:
        # 提取数据 - 兼容不同的数据结构
        if isinstance(compatibility_result, dict):
            emotion_score = compatibility_result.get('情感匹配', {}).get('score', 50) if isinstance(compatibility_result.get('情感匹配'), dict) else 50
            life_score = compatibility_result.get('生活匹配', {}).get('score', 50) if isinstance(compatibility_result.get('生活匹配'), dict) else 50
            career_score = compatibility_result.get('事业匹配', {}).get('score', 50) if isinstance(compatibility_result.get('事业匹配'), dict) else 50
        else:
            emotion_score = 50
            life_score = 50
            career_score = 50
        
        # 创建柱状图（更简单直观）
        fig = go.Figure()
        
        dimensions = ['情感匹配', '生活匹配', '事业匹配']
        scores = [emotion_score, life_score, career_score]
        
        # 根据分数设置颜色
        colors = []
        for score in scores:
            if score >= 85:
                colors.append('#4CAF50')  # 绿色
            elif score >= 70:
                colors.append('#8BC34A')  # 浅绿色
            elif score >= 50:
                colors.append('#FFC107')  # 黄色
            else:
                colors.append('#FF9800')  # 橙色
        
        fig.add_trace(go.Bar(
            x=dimensions,
            y=scores,
            marker_color=colors,
            text=[f"{score}分" for score in scores],
            textposition='auto',
            textfont=dict(size=14, color='white', family='Microsoft YaHei')
        ))
        
        fig.update_layout(
            title=dict(text='匹配度分析图', font=dict(family='Microsoft YaHei', size=18)),
            xaxis_title='匹配维度',
            yaxis_title='匹配分数',
            yaxis=dict(range=[0, 100]),
            font=dict(family='Microsoft YaHei', size=14),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        # 转换为HTML
        chart_html = pyo.plot(fig, output_type='div', include_plotlyjs='cdn', config={'displayModeBar': False})
        return chart_html
    except Exception as e:
        print(f"创建图表失败: {e}")
        return None


def create_fortune_chart(fortune_data):
    """
    创建运势预测图表
    
    参数:
        fortune_data: 运势预测数据
    
    返回:
        HTML格式的图表
    """
    if not fortune_data:
        return None
    
    # 提取数据
    fortune_types = []
    scores = []
    levels = []
    
    for fortune_type, fortune_info in fortune_data.items():
        fortune_types.append(fortune_type)
        scores.append(fortune_info.get('score', 50))
        levels.append(fortune_info.get('level', '一般'))
    
    # 创建柱状图
    fig = go.Figure()
    
    # 根据等级设置颜色
    colors = []
    for level in levels:
        if level == '极佳':
            colors.append('#4CAF50')
        elif level == '良好':
            colors.append('#8BC34A')
        elif level == '一般':
            colors.append('#FFC107')
        elif level == '较差':
            colors.append('#FF9800')
        else:
            colors.append('#F44336')
    
    fig.add_trace(go.Bar(
        x=fortune_types,
        y=scores,
        marker_color=colors,
        text=[f"{score}分" for score in scores],
        textposition='auto',
    ))
    
    fig.update_layout(
        title='运势预测分析图',
        xaxis_title='运势类型',
        yaxis_title='运势分数',
        yaxis=dict(range=[0, 100]),
        font=dict(family='Microsoft YaHei', size=14)
    )
    
    # 转换为HTML
    chart_html = pyo.plot(fig, output_type='div', include_plotlyjs='cdn')
    return chart_html


def create_personality_chart(zodiac_analysis, mbti_analysis):
    """
    创建性格分析图表
    
    参数:
        zodiac_analysis: 星座分析结果
        mbti_analysis: MBTI分析结果
    
    返回:
        HTML格式的图表
    """
    # 这里可以创建性格特征的对比图
    # 暂时返回空
    return None

