# 主路由 - 纯Python后端渲染
from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import sys
import os

# 导入业务逻辑模块
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from modules.zodiac import get_zodiac, format_zodiac_analysis
from modules.mbti import format_mbti_analysis
from modules.fortune import get_fortune_prediction, format_fortune_prediction
from modules.fengshui import get_fengshui_analysis, format_fengshui_analysis
from modules.compatibility import analyze_combined_compatibility, format_compatibility_analysis
from modules.visualization import create_compatibility_chart, create_fortune_chart
from modules.mental_health import analyze_mental_health, format_mental_health_analysis
from modules.recommendation import get_recommendations, format_recommendations
from modules.action_plan import generate_action_plan, format_action_plan
from modules.divination import calculate_bazi, analyze_bazi, format_bazi_analysis, analyze_tarot_reading, format_tarot_reading
from modules.chat_assistant import ChatAssistant
from database.db_manager import DatabaseManager

main_bp = Blueprint('main', __name__)

# 初始化数据库
db_manager = DatabaseManager()

# 初始化聊天助手
chat_assistant = ChatAssistant(api_type='free_api')

@main_bp.route('/')
def index():
    """主页 - 分析预测"""
    return render_template('analyze.html', active_tab='analyze')

@main_bp.route('/analyze', methods=['GET', 'POST'])
def analyze():
    """分析预测页面"""
    if request.method == 'POST':
        try:
            name = request.form.get('name', '').strip()
            birthday = request.form.get('birthday', '').strip()
            mbti = request.form.get('mbti', '').strip()
            birth_hour = request.form.get('birth_hour', '').strip()
            residence_direction = request.form.get('residence_direction', '').strip()
            house_orientation = request.form.get('house_orientation', '').strip()
            enable_bazi = request.form.get('enable_bazi') == '1'
            enable_tarot = request.form.get('enable_tarot') == '1'
            
            if not name:
                return render_template('analyze.html', active_tab='analyze', error='请输入姓名！')
            
            if not birthday:
                return render_template('analyze.html', active_tab='analyze', error='请输入生日！')
            
            if not mbti:
                return render_template('analyze.html', active_tab='analyze', error='请选择MBTI类型！')
            
            # 获取星座
            zodiac = get_zodiac(birthday)
            if not zodiac:
                return render_template('analyze.html', active_tab='analyze', error='无法判断星座，请检查生日输入！')
            
            # 获取分析结果
            zodiac_analysis = format_zodiac_analysis(zodiac)
            mbti_analysis = format_mbti_analysis(mbti)
            fortune_prediction_dict = get_fortune_prediction(zodiac, mbti)
            fortune_prediction = format_fortune_prediction(fortune_prediction_dict)
            
            # 风水分析
            fengshui_analysis_text = ""
            fengshui_analysis_dict = None
            if residence_direction or house_orientation:
                try:
                    birth_hour_int = int(birth_hour) if birth_hour else None
                    fengshui_analysis_dict = get_fengshui_analysis(
                        residence_direction=residence_direction,
                        house_orientation=house_orientation,
                        birth_hour=birth_hour_int,
                        zodiac=zodiac
                    )
                    fengshui_analysis_text = format_fengshui_analysis(fengshui_analysis_dict)
                except Exception as e:
                    # 风水分析失败不影响其他分析
                    pass
            
            # 创建运势图表
            fortune_chart_html = create_fortune_chart(fortune_prediction_dict)
            
            # 心理健康分析
            mental_health_data = analyze_mental_health(mbti)
            mental_health_analysis = ""
            if mental_health_data:
                mental_health_analysis = format_mental_health_analysis(mental_health_data)
            
            # 生成个性化推荐
            recommendations = get_recommendations(fortune_prediction_dict)
            recommendations_text = format_recommendations(recommendations)
            
            # 生成行动计划
            action_plan = generate_action_plan(fortune_prediction_dict, zodiac, mbti)
            action_plan_text = format_action_plan(action_plan)
            
            # 八字分析
            bazi_analysis_text = ""
            bazi_data = None
            if enable_bazi:
                try:
                    birth_hour_int = int(birth_hour) if birth_hour else None
                    bazi_data = calculate_bazi(birthday, birth_hour_int)
                    if bazi_data:
                        bazi_analysis = analyze_bazi(bazi_data)
                        if bazi_analysis:
                            bazi_analysis_text = format_bazi_analysis(bazi_analysis)
                except Exception as e:
                    pass
            
            # 塔罗牌占卜
            tarot_reading_text = ""
            tarot_data = None
            if enable_tarot:
                try:
                    tarot_data = analyze_tarot_reading(3)
                    if tarot_data:
                        tarot_reading_text = format_tarot_reading(tarot_data)
                except Exception as e:
                    pass
            
            # 保存到数据库
            user_id = db_manager.add_user(name, birthday, zodiac, mbti)
            analysis_result = {
                "zodiac_analysis": zodiac_analysis,
                "mbti_analysis": mbti_analysis,
                "fortune_prediction": fortune_prediction_dict,
                "fengshui_analysis": fengshui_analysis_dict,
                "mental_health_analysis": mental_health_data,
                "recommendations": recommendations,
                "action_plan": action_plan,
                "bazi_analysis": bazi_data,
                "tarot_reading": tarot_data
            }
            history_id = db_manager.add_analysis_history(user_id, analysis_result)
            
            # 返回结果
            result = {
                'name': name,
                'zodiac': zodiac,
                'zodiac_analysis': zodiac_analysis,
                'mbti_analysis': mbti_analysis,
                'fortune_prediction': fortune_prediction,
                'fengshui_analysis': fengshui_analysis_text,
                'mental_health_analysis': mental_health_analysis,
                'recommendations': recommendations_text,
                'action_plan': action_plan_text,
                'bazi_analysis': bazi_analysis_text,
                'tarot_reading': tarot_reading_text,
                'fortune_chart_html': fortune_chart_html,
                'history_id': history_id
            }
            
            return render_template('analyze.html', active_tab='analyze', result=result)
            
        except Exception as e:
            return render_template('analyze.html', active_tab='analyze', error=f'分析失败：{str(e)}')
    
    return render_template('analyze.html', active_tab='analyze')

@main_bp.route('/feedback/<int:history_id>', methods=['POST'])
def feedback(history_id):
    """提交反馈"""
    try:
        feedback_text = request.form.get('feedback', '').strip()
        
        if not feedback_text:
            return redirect(url_for('main.index'))
        
        db_manager.add_feedback(history_id, feedback_text)
        return redirect(url_for('main.index'))
        
    except Exception as e:
        return redirect(url_for('main.index'))

@main_bp.route('/history')
def history():
    """历史记录页面"""
    try:
        history_list = db_manager.get_all_history()
        
        # 格式化历史记录
        formatted_history = []
        for record in history_list:
            formatted_history.append({
                'id': record['id'],
                'name': record['name'],
                'zodiac': record.get('zodiac', ''),
                'mbti': record.get('mbti', ''),
                'created_at': record['created_at']
            })
        
        # 获取成功/错误消息
        success_message = request.args.get('success', '')
        error_message = request.args.get('error', '')
        
        return render_template('history.html', 
                             active_tab='history', 
                             history_list=formatted_history,
                             success_message=success_message,
                             error_message=error_message)
        
    except Exception as e:
        return render_template('history.html', active_tab='history', history_list=[], error_message=str(e))

@main_bp.route('/history/<int:history_id>')
def view_history(history_id):
    """查看历史记录详情"""
    try:
        record = db_manager.get_history_by_id(history_id)
        
        if not record:
            return redirect(url_for('main.history'))
        
        analysis_result = record.get('analysis_result', {})
        
        # 格式化运势预测
        fortune_text = ''
        if analysis_result.get('fortune_prediction'):
            if isinstance(analysis_result['fortune_prediction'], str):
                fortune_text = analysis_result['fortune_prediction']
            else:
                fortune_text = format_fortune_prediction(analysis_result['fortune_prediction'])
        
        # 格式化风水分析
        fengshui_text = ''
        if analysis_result.get('fengshui_analysis'):
            if isinstance(analysis_result['fengshui_analysis'], str):
                fengshui_text = analysis_result['fengshui_analysis']
            elif isinstance(analysis_result['fengshui_analysis'], dict):
                fengshui_text = format_fengshui_analysis(analysis_result['fengshui_analysis'])
        
        # 格式化心理健康分析
        mental_health_text = ''
        if analysis_result.get('mental_health_analysis'):
            if isinstance(analysis_result['mental_health_analysis'], str):
                mental_health_text = analysis_result['mental_health_analysis']
            elif isinstance(analysis_result['mental_health_analysis'], dict):
                try:
                    mental_health_text = format_mental_health_analysis(analysis_result['mental_health_analysis'])
                except:
                    mental_health_text = ''
        
        # 格式化推荐和行动计划
        recommendations_text = ''
        if analysis_result.get('recommendations'):
            if isinstance(analysis_result['recommendations'], str):
                recommendations_text = analysis_result['recommendations']
            elif isinstance(analysis_result['recommendations'], dict):
                try:
                    recommendations_text = format_recommendations(analysis_result['recommendations'])
                except:
                    recommendations_text = ''
        
        action_plan_text = ''
        if analysis_result.get('action_plan'):
            if isinstance(analysis_result['action_plan'], str):
                action_plan_text = analysis_result['action_plan']
            elif isinstance(analysis_result['action_plan'], dict):
                try:
                    action_plan_text = format_action_plan(analysis_result['action_plan'])
                except:
                    action_plan_text = ''
        
        # 格式化八字和塔罗牌
        bazi_text = ''
        if analysis_result.get('bazi_analysis'):
            if isinstance(analysis_result['bazi_analysis'], str):
                bazi_text = analysis_result['bazi_analysis']
            elif isinstance(analysis_result['bazi_analysis'], dict):
                try:
                    bazi_analysis = analyze_bazi(analysis_result['bazi_analysis'])
                    if bazi_analysis:
                        bazi_text = format_bazi_analysis(bazi_analysis)
                except:
                    bazi_text = ''
        
        tarot_text = ''
        if analysis_result.get('tarot_reading'):
            if isinstance(analysis_result['tarot_reading'], str):
                tarot_text = analysis_result['tarot_reading']
            elif isinstance(analysis_result['tarot_reading'], dict):
                try:
                    tarot_text = format_tarot_reading(analysis_result['tarot_reading'])
                except:
                    tarot_text = ''
        
        # 创建运势图表
        fortune_chart_html = None
        if analysis_result.get('fortune_prediction'):
            if isinstance(analysis_result['fortune_prediction'], dict):
                try:
                    fortune_chart_html = create_fortune_chart(analysis_result['fortune_prediction'])
                except:
                    fortune_chart_html = None
        
        result = {
            'name': record['name'],
            'zodiac_analysis': analysis_result.get('zodiac_analysis', ''),
            'mbti_analysis': analysis_result.get('mbti_analysis', ''),
            'fortune_prediction': fortune_text,
            'fengshui_analysis': fengshui_text,
            'mental_health_analysis': mental_health_text,
            'recommendations': recommendations_text,
            'action_plan': action_plan_text,
            'bazi_analysis': bazi_text,
            'tarot_reading': tarot_text,
            'fortune_chart_html': fortune_chart_html,
            'history_id': history_id
        }
        
        return render_template('analyze.html', active_tab='analyze', result=result)
        
    except Exception as e:
        return redirect(url_for('main.history', error=f'查看历史记录失败：{str(e)}'))

@main_bp.route('/history/<int:history_id>/delete', methods=['POST'])
def delete_history(history_id):
    """删除历史记录"""
    try:
        # 检查记录是否存在
        record = db_manager.get_history_by_id(history_id)
        if not record:
            return redirect(url_for('main.history', error='记录不存在！'))
        
        # 删除记录
        success = db_manager.delete_history(history_id)
        
        if success:
            return redirect(url_for('main.history', success='记录删除成功！'))
        else:
            return redirect(url_for('main.history', error='删除失败：记录不存在或已被删除！'))
        
    except Exception as e:
        return redirect(url_for('main.history', error=f'删除记录失败：{str(e)}'))

@main_bp.route('/chat', methods=['GET', 'POST'])
def chat():
    """心理聊天页面"""
    # 初始化聊天消息列表
    if 'chat_messages' not in session:
        session['chat_messages'] = []
        session['chat_initialized'] = False
    
    messages = session.get('chat_messages', [])
    
    if request.method == 'POST':
        try:
            user_message = request.form.get('message', '').strip()
            
            if not user_message:
                return render_template('chat.html', active_tab='chat', messages=messages)
            
            # 添加用户消息
            from datetime import datetime
            messages.append({
                'sender': 'user',
                'content': user_message,
                'time': datetime.now().strftime('%H:%M')
            })
            
            # 获取AI回复
            response = chat_assistant.chat(user_message)
            
            # 添加AI回复
            messages.append({
                'sender': 'assistant',
                'content': response,
                'time': datetime.now().strftime('%H:%M')
            })
            
            # 保存到session
            session['chat_messages'] = messages
            session.modified = True
            
            return render_template('chat.html', active_tab='chat', messages=messages)
            
        except Exception as e:
            return render_template('chat.html', active_tab='chat', messages=messages, error=str(e))
    
    # 初始化欢迎消息
    if not session.get('chat_initialized', False):
        messages.insert(0, {
            'sender': 'assistant',
            'content': '你好！我是你的心理聊天助手。有什么想聊的吗？我会认真倾听的。',
            'time': '系统'
        })
        session['chat_messages'] = messages
        session['chat_initialized'] = True
        session.modified = True
    
    return render_template('chat.html', active_tab='chat', messages=messages)

@main_bp.route('/chat/clear')
def clear_chat():
    """清空聊天记录"""
    session['chat_messages'] = []
    session['chat_initialized'] = False
    session.modified = True
    return redirect(url_for('main.chat'))

@main_bp.route('/compatibility', methods=['GET', 'POST'])
def compatibility():
    """匹配度分析页面"""
    if request.method == 'POST':
        try:
            name1 = request.form.get('name1', '').strip()
            birthday1 = request.form.get('birthday1', '').strip()
            mbti1 = request.form.get('mbti1', '').strip()
            name2 = request.form.get('name2', '').strip()
            birthday2 = request.form.get('birthday2', '').strip()
            mbti2 = request.form.get('mbti2', '').strip()
            
            if not name1 or not birthday1 or not mbti1:
                return render_template('compatibility.html', active_tab='compatibility', error='请填写第一人的完整信息！')
            
            if not name2 or not birthday2 or not mbti2:
                return render_template('compatibility.html', active_tab='compatibility', error='请填写第二人的完整信息！')
            
            # 获取星座
            zodiac1 = get_zodiac(birthday1)
            zodiac2 = get_zodiac(birthday2)
            
            if not zodiac1 or not zodiac2:
                return render_template('compatibility.html', active_tab='compatibility', error='无法判断星座，请检查生日输入！')
            
            # 分析匹配度
            compatibility_result = analyze_combined_compatibility(zodiac1, mbti1, zodiac2, mbti2)
            
            if not compatibility_result:
                return render_template('compatibility.html', active_tab='compatibility', error='匹配度分析失败！')
            
            # 格式化分析结果
            detailed_analysis = format_compatibility_analysis(compatibility_result, analysis_type="combined")
            
            # 创建图表 - 使用综合匹配数据
            combined_match_data = {
                '情感匹配': compatibility_result.get('情感匹配', {}),
                '生活匹配': compatibility_result.get('生活匹配', {}),
                '事业匹配': compatibility_result.get('事业匹配', {})
            }
            chart_html = create_compatibility_chart(combined_match_data)
            
            # 组织结果数据
            result = {
                'name1': name1,
                'name2': name2,
                'zodiac1': zodiac1,
                'zodiac2': zodiac2,
                'mbti1': mbti1,
                'mbti2': mbti2,
                'combined_result': {
                    'combined_match': compatibility_result.get('综合匹配', {}),
                    'emotion_match': compatibility_result.get('情感匹配', {}),
                    'life_match': compatibility_result.get('生活匹配', {}),
                    'career_match': compatibility_result.get('事业匹配', {})
                },
                'detailed_analysis': detailed_analysis,
                'chart_html': chart_html
            }
            
            return render_template('compatibility.html', active_tab='compatibility', result=result)
            
        except Exception as e:
            return render_template('compatibility.html', active_tab='compatibility', error=f'分析失败：{str(e)}')
    
    return render_template('compatibility.html', active_tab='compatibility')
