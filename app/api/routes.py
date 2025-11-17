# API路由
from flask import Blueprint, request, jsonify
import os
import json

# 导入业务逻辑模块
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from modules.zodiac import get_zodiac, format_zodiac_analysis
from modules.mbti import format_mbti_analysis, get_all_mbti_types
from modules.fortune import get_fortune_prediction, format_fortune_prediction
from modules.chat_assistant import ChatAssistant
from database.db_manager import DatabaseManager

api_bp = Blueprint('api', __name__)

# 初始化数据库
db_manager = DatabaseManager()

# 初始化聊天助手
chat_assistant = ChatAssistant(api_type='free_api')

@api_bp.route('/analyze', methods=['POST'])
def analyze():
    """分析接口"""
    try:
        data = request.json
        name = data.get('name', '').strip()
        birthday = data.get('birthday', '').strip()
        mbti = data.get('mbti', '').strip()
        
        if not name:
            return jsonify({'success': False, 'error': '请输入姓名！'}), 400
        
        if not birthday:
            return jsonify({'success': False, 'error': '请输入生日！'}), 400
        
        if not mbti:
            return jsonify({'success': False, 'error': '请选择MBTI类型！'}), 400
        
        # 获取星座
        zodiac = get_zodiac(birthday)
        if not zodiac:
            return jsonify({'success': False, 'error': '无法判断星座，请检查生日输入！'}), 400
        
        # 获取分析结果
        zodiac_analysis = format_zodiac_analysis(zodiac)
        mbti_analysis = format_mbti_analysis(mbti)
        fortune_prediction_dict = get_fortune_prediction(zodiac, mbti)
        fortune_prediction = format_fortune_prediction(fortune_prediction_dict)
        
        # 保存到数据库
        user_id = db_manager.add_user(name, birthday, zodiac, mbti)
        analysis_result = {
            "zodiac_analysis": zodiac_analysis,
            "mbti_analysis": mbti_analysis,
            "fortune_prediction": fortune_prediction_dict
        }
        history_id = db_manager.add_analysis_history(user_id, analysis_result)
        
        # 返回结果
        result = {
            'success': True,
            'data': {
                'name': name,
                'zodiac': zodiac,
                'zodiac_analysis': zodiac_analysis,
                'mbti_analysis': mbti_analysis,
                'fortune_prediction': fortune_prediction,
                'history_id': history_id
            }
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'success': False, 'error': f'分析失败：{str(e)}'}), 500

@api_bp.route('/feedback', methods=['POST'])
def submit_feedback():
    """提交反馈接口"""
    try:
        data = request.json
        history_id = data.get('history_id')
        feedback = data.get('feedback', '').strip()
        
        if not history_id:
            return jsonify({'success': False, 'error': '缺少历史记录ID！'}), 400
        
        if not feedback:
            return jsonify({'success': False, 'error': '请输入反馈内容！'}), 400
        
        db_manager.add_feedback(history_id, feedback)
        
        return jsonify({'success': True, 'message': '反馈已提交，感谢您的反馈！'})
        
    except Exception as e:
        return jsonify({'success': False, 'error': f'提交失败：{str(e)}'}), 500

@api_bp.route('/history', methods=['GET'])
def get_history():
    """获取历史记录接口"""
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
        
        return jsonify({'success': True, 'data': formatted_history})
        
    except Exception as e:
        return jsonify({'success': False, 'error': f'获取历史记录失败：{str(e)}'}), 500

@api_bp.route('/history/<int:history_id>', methods=['GET'])
def get_history_detail(history_id):
    """获取历史记录详情接口"""
    try:
        record = db_manager.get_history_by_id(history_id)
        
        if not record:
            return jsonify({'success': False, 'error': '历史记录不存在！'}), 404
        
        return jsonify({'success': True, 'data': record})
        
    except Exception as e:
        return jsonify({'success': False, 'error': f'获取历史记录失败：{str(e)}'}), 500

@api_bp.route('/mbti/types', methods=['GET'])
def get_mbti_types():
    """获取MBTI类型列表接口"""
    try:
        mbti_types = get_all_mbti_types()
        return jsonify({'success': True, 'data': mbti_types})
    except Exception as e:
        return jsonify({'success': False, 'error': f'获取MBTI类型失败：{str(e)}'}), 500

@api_bp.route('/chat', methods=['POST'])
def chat():
    """聊天接口"""
    try:
        data = request.json
        message = data.get('message', '').strip()
        
        if not message:
            return jsonify({'success': False, 'error': '请输入消息！'}), 400
        
        # 获取AI回复
        response = chat_assistant.chat(message)
        
        return jsonify({
            'success': True,
            'data': {
                'response': response
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': f'聊天失败：{str(e)}'}), 500

@api_bp.route('/chat/clear', methods=['POST'])
def clear_chat():
    """清空聊天记录接口"""
    try:
        chat_assistant.clear_history()
        return jsonify({'success': True, 'message': '聊天记录已清空'})
    except Exception as e:
        return jsonify({'success': False, 'error': f'清空失败：{str(e)}'}), 500

