# 心理聊天助手模块
import requests
import json
import os
try:
    from config import CHAT_API_KEY, CHAT_API_TYPE
except ImportError:
    # Kivy版本可能没有config模块
    CHAT_API_KEY = ""
    CHAT_API_TYPE = "free_api"


class ChatAssistant:
    """心理聊天助手类"""
    
    def __init__(self, api_key=None, api_type='free_api'):
        """
        初始化聊天助手
        
        参数:
            api_key: API密钥（可选，免费模式不需要）
            api_type: API类型 ('free_api', 'openai', 'huggingface', 'mock')
        """
        try:
            self.api_key = api_key or CHAT_API_KEY
            self.api_type = api_type or CHAT_API_TYPE
        except NameError:
            # 如果CHAT_API_KEY未定义（Kivy环境）
            self.api_key = api_key or ""
            self.api_type = api_type or 'free_api'
        self.conversation_history = []
        
    def set_api_key(self, api_key):
        """设置API密钥"""
        self.api_key = api_key
        
    def add_system_message(self, message):
        """添加系统消息（用于设置AI角色）"""
        system_prompt = """你是一位专业的心理咨询师和情感助手。你的任务是：
1. 倾听用户的感受和问题
2. 提供温暖、理解和支持
3. 给予建设性的建议和指导
4. 帮助用户更好地理解自己的情绪
5. 使用温和、鼓励的语气
6. 避免过于专业的术语，使用通俗易懂的语言

请用中文回复，保持友好和专业的平衡。"""
        self.conversation_history = [
            {"role": "system", "content": system_prompt}
        ]
        
    def chat_openai(self, user_message):
        """
        使用OpenAI API进行聊天
        
        参数:
            user_message: 用户消息
        
        返回:
            AI回复
        """
        if not self.api_key:
            return "❌ 未设置API密钥，请在设置中配置OpenAI API Key"
        
        try:
            # 添加用户消息到历史
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # 调用OpenAI API
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
            data = {
                "model": "gpt-3.5-turbo",
                "messages": self.conversation_history,
                "temperature": 0.7,
                "max_tokens": 500
            }
            
            response = requests.post(url, headers=headers, json=data, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                ai_message = result['choices'][0]['message']['content']
                
                # 添加AI回复到历史
                self.conversation_history.append({
                    "role": "assistant",
                    "content": ai_message
                })
                
                return ai_message
            else:
                error_msg = response.json().get('error', {}).get('message', '未知错误')
                return f"❌ API调用失败: {error_msg}"
                
        except requests.exceptions.Timeout:
            return "❌ 请求超时，请稍后重试"
        except requests.exceptions.RequestException as e:
            return f"❌ 网络错误: {str(e)}"
        except Exception as e:
            return f"❌ 发生错误: {str(e)}"
    
    def chat_huggingface(self, user_message):
        """
        使用Hugging Face API进行聊天
        
        参数:
            user_message: 用户消息
        
        返回:
            AI回复
        """
        if not self.api_key:
            return "❌ 未设置API密钥，请在设置中配置Hugging Face API Key"
        
        try:
            # 构建上下文
            context = "你是一位温暖的心理咨询师。"
            if self.conversation_history:
                context += " " + " ".join([msg.get('content', '') for msg in self.conversation_history[-3:]])
            
            prompt = f"{context}\n用户: {user_message}\n助手:"
            
            url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
            headers = {
                "Authorization": f"Bearer {self.api_key}"
            }
            data = {
                "inputs": prompt,
                "parameters": {
                    "max_length": 200,
                    "temperature": 0.7
                }
            }
            
            response = requests.post(url, headers=headers, json=data, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    ai_message = result[0].get('generated_text', '').replace(prompt, '').strip()
                else:
                    ai_message = result.get('generated_text', '').replace(prompt, '').strip()
                
                # 添加对话到历史
                self.conversation_history.append({
                    "role": "user",
                    "content": user_message
                })
                self.conversation_history.append({
                    "role": "assistant",
                    "content": ai_message
                })
                
                return ai_message if ai_message else "抱歉，我没有理解您的意思，能再说一遍吗？"
            else:
                return f"❌ API调用失败: {response.status_code}"
                
        except Exception as e:
            return f"❌ 发生错误: {str(e)}"
    
    def chat_mock(self, user_message):
        """
        模拟聊天（当没有API key时使用）
        
        参数:
            user_message: 用户消息
        
        返回:
            模拟回复
        """
        # 简单的关键词回复
        user_message_lower = user_message.lower()
        
        responses = {
            "你好": "你好！我很高兴能和你聊天。今天感觉怎么样？",
            "不开心": "我理解你的感受。能告诉我发生了什么吗？我会认真倾听的。",
            "焦虑": "焦虑是很正常的情绪反应。我们可以一起探讨一下让你感到焦虑的原因，好吗？",
            "谢谢": "不客气！能帮助到你我很开心。如果还有其他想聊的，随时告诉我。",
            "再见": "再见！记住，我随时都在这里倾听你的声音。保重！"
        }
        
        for keyword, response in responses.items():
            if keyword in user_message_lower:
                return response
        
        # 默认回复
        default_responses = [
            "我理解你的感受。能详细说说吗？",
            "听起来你正在经历一些困扰。我愿意倾听你的故事。",
            "每个人都会遇到困难的时候。你不是一个人，我会陪伴你的。",
            "能告诉我更多细节吗？这样我可以更好地帮助你。",
            "我在这里支持你。让我们一起面对这个问题。"
        ]
        
        import random
        return random.choice(default_responses)
    
    def chat_free_api(self, user_message):
        """
        使用免费AI API进行聊天（无需API Key）
        
        参数:
            user_message: 用户消息
        
        返回:
            AI回复
        """
        try:
            # 构建对话上下文
            if not self.conversation_history:
                self.add_system_message("")
            
            # 添加用户消息
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # 使用免费的AI聊天API（示例：使用公开的AI服务）
            # 注意：这里使用一个免费的AI服务，您可以根据需要替换
            
            # 方案1: 使用Hugging Face的免费推理API（无需API Key的模型）
            url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
            headers = {
                "Content-Type": "application/json"
            }
            
            # 构建输入文本
            context = ""
            for msg in self.conversation_history[-5:]:  # 只使用最近5条消息
                if msg['role'] == 'user':
                    context += f"用户: {msg['content']}\n"
                elif msg['role'] == 'assistant':
                    context += f"助手: {msg['content']}\n"
            
            data = {
                "inputs": context + f"用户: {user_message}\n助手:",
                "parameters": {
                    "max_length": 200,
                    "temperature": 0.7,
                    "return_full_text": False
                }
            }
            
            try:
                response = requests.post(url, headers=headers, json=data, timeout=15)
                
                if response.status_code == 200:
                    result = response.json()
                    if isinstance(result, list) and len(result) > 0:
                        ai_message = result[0].get('generated_text', '').strip()
                        # 清理回复
                        ai_message = ai_message.replace("助手:", "").strip()
                    else:
                        ai_message = result.get('generated_text', '').strip()
                    
                    if not ai_message:
                        # 如果API返回空，使用智能回复
                        return self.get_smart_response(user_message)
                    
                    # 添加AI回复到历史
                    self.conversation_history.append({
                        "role": "assistant",
                        "content": ai_message
                    })
                    
                    return ai_message
                else:
                    # API调用失败，使用智能回复
                    return self.get_smart_response(user_message)
            except:
                # 网络错误，使用智能回复
                return self.get_smart_response(user_message)
                
        except Exception as e:
            # 发生错误，使用智能回复
            return self.get_smart_response(user_message)
    
    def get_smart_response(self, user_message):
        """
        智能回复生成（当API不可用时使用）
        
        参数:
            user_message: 用户消息
        
        返回:
            智能回复
        """
        user_lower = user_message.lower()
        
        # 关键词匹配回复
        responses = {
            "你好": "你好！很高兴和你聊天。今天感觉怎么样？有什么想聊的吗？",
            "不开心": "我理解你的感受。每个人都会有不开心的时候，这是很正常的。能告诉我发生了什么吗？我会认真倾听的。",
            "焦虑": "焦虑是很常见的情绪反应。我们可以一起探讨一下让你感到焦虑的原因，好吗？深呼吸，慢慢来。",
            "压力": "压力确实会让人感到疲惫。试着把问题分解成小步骤，一步一步解决会更容易。",
            "谢谢": "不客气！能帮助到你我很开心。如果还有其他想聊的，随时告诉我。",
            "再见": "再见！记住，我随时都在这里倾听你的声音。保重！",
            "帮助": "我是你的心理聊天助手，可以和你聊天、倾听你的感受、提供建议。有什么想聊的都可以告诉我。",
        }
        
        # 检查关键词
        for keyword, response in responses.items():
            if keyword in user_lower:
                return response
        
        # 情感分析回复
        if any(word in user_lower for word in ["难过", "伤心", "沮丧", "失望"]):
            return "我理解你现在可能感到难过。这种情绪是完全可以理解的。能详细说说发生了什么吗？我会认真听的。"
        
        if any(word in user_lower for word in ["开心", "高兴", "快乐", "兴奋"]):
            return "太好了！听到你感到开心我也很高兴。是什么让你这么开心呢？"
        
        if any(word in user_lower for word in ["担心", "害怕", "恐惧", "紧张"]):
            return "担心是很正常的情绪。让我们一起来面对这个担心，好吗？告诉我你在担心什么？"
        
        # 默认回复
        default_responses = [
            "我理解你的感受。能详细说说吗？这样我可以更好地帮助你。",
            "听起来你正在经历一些困扰。我愿意倾听你的故事，我们一起面对。",
            "每个人都会遇到困难的时候。你不是一个人，我会陪伴你的。",
            "我在这里支持你。让我们一起探讨这个问题，看看能做什么。",
            "你的感受很重要。能告诉我更多细节吗？",
            "我明白这对你来说可能不容易。让我们慢慢来，一步一步解决。"
        ]
        
        import random
        # 根据消息长度选择回复
        if len(user_message) < 10:
            return "我理解你想表达什么。能多说一些吗？这样我可以更好地帮助你。"
        else:
            return random.choice(default_responses)
    
    def chat(self, user_message):
        """
        聊天主方法
        
        参数:
            user_message: 用户消息
        
        返回:
            AI回复
        """
        if not self.conversation_history:
            self.add_system_message("")
        
        # 优先使用免费API（不需要API Key）
        if self.api_type == 'free_api' or not self.api_key:
            return self.chat_free_api(user_message)
        elif self.api_type == 'openai' and self.api_key:
            return self.chat_openai(user_message)
        elif self.api_type == 'huggingface' and self.api_key:
            return self.chat_huggingface(user_message)
        else:
            return self.get_smart_response(user_message)
    
    def clear_history(self):
        """清空对话历史"""
        self.conversation_history = []
    
    def save_conversation(self, filepath):
        """保存对话历史到文件"""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"保存对话失败: {e}")
            return False
    
    def load_conversation(self, filepath):
        """从文件加载对话历史"""
        try:
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    self.conversation_history = json.load(f)
                return True
        except Exception as e:
            print(f"加载对话失败: {e}")
        return False

