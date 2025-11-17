# 数据库管理模块
import sqlite3
import json
import os
from datetime import datetime
import os

# 数据库路径配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATABASE_DIR, exist_ok=True)
DATABASE_PATH = os.path.join(DATABASE_DIR, "fortune_telling.db")


class DatabaseManager:
    """数据库管理类，负责所有数据库操作"""
    
    def __init__(self, db_path=None):
        """初始化数据库连接"""
        if db_path is None:
            # 在Android上，使用应用数据目录
            try:
                from android.storage import primary_external_storage_path
                android_path = primary_external_storage_path()
                db_dir = os.path.join(android_path, 'fortunetelling')
                os.makedirs(db_dir, exist_ok=True)
                self.db_path = os.path.join(db_dir, 'fortune_telling.db')
            except ImportError:
                # 非Android环境，使用默认路径
                self.db_path = DATABASE_PATH
                # 确保目录存在
                os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        else:
            self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        """获取数据库连接"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # 使查询结果可以通过列名访问
        return conn
    
    def init_database(self):
        """初始化数据库，创建表结构"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # 创建用户表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birthday TEXT NOT NULL,
                zodiac TEXT NOT NULL,
                mbti TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        ''')
        
        # 创建分析历史表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analysis_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                analysis_result TEXT NOT NULL,
                feedback TEXT,
                created_at TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_user(self, name, birthday, zodiac, mbti):
        """添加用户"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO users (name, birthday, zodiac, mbti, created_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, birthday, zodiac, mbti, created_at))
        
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return user_id
    
    def get_user(self, user_id):
        """根据ID获取用户信息"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return dict(row)
        return None
    
    def add_analysis_history(self, user_id, analysis_result, feedback=None):
        """添加分析历史记录"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 将分析结果转换为JSON字符串存储
        analysis_json = json.dumps(analysis_result, ensure_ascii=False)
        
        cursor.execute('''
            INSERT INTO analysis_history (user_id, analysis_result, feedback, created_at)
            VALUES (?, ?, ?, ?)
        ''', (user_id, analysis_json, feedback, created_at))
        
        history_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return history_id
    
    def get_all_history(self, user_id=None):
        """获取所有历史记录，如果指定user_id则只获取该用户的记录"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if user_id:
            cursor.execute('''
                SELECT h.*, u.name, u.birthday, u.zodiac, u.mbti
                FROM analysis_history h
                JOIN users u ON h.user_id = u.id
                WHERE h.user_id = ?
                ORDER BY h.created_at DESC
            ''', (user_id,))
        else:
            cursor.execute('''
                SELECT h.*, u.name, u.birthday, u.zodiac, u.mbti
                FROM analysis_history h
                JOIN users u ON h.user_id = u.id
                ORDER BY h.created_at DESC
            ''')
        
        rows = cursor.fetchall()
        conn.close()
        
        # 将查询结果转换为字典列表
        history_list = []
        for row in rows:
            record = dict(row)
            # 解析JSON字符串
            try:
                if isinstance(record['analysis_result'], str):
                    record['analysis_result'] = json.loads(record['analysis_result'])
            except (json.JSONDecodeError, TypeError):
                # 如果解析失败，保持原样或设为空字典
                if not isinstance(record['analysis_result'], dict):
                    record['analysis_result'] = {}
            history_list.append(record)
        
        return history_list
    
    def add_feedback(self, history_id, feedback):
        """添加反馈信息（与update_feedback功能相同，保持API一致性）"""
        self.update_feedback(history_id, feedback)
    
    def update_feedback(self, history_id, feedback):
        """更新反馈信息"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE analysis_history
            SET feedback = ?
            WHERE id = ?
        ''', (feedback, history_id))
        
        conn.commit()
        conn.close()
    
    def delete_history(self, history_id):
        """删除历史记录"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # 检查记录是否存在
            cursor.execute('SELECT id FROM analysis_history WHERE id = ?', (history_id,))
            if cursor.fetchone() is None:
                conn.close()
                return False
            
            # 删除记录
            cursor.execute('DELETE FROM analysis_history WHERE id = ?', (history_id,))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            # 如果连接已打开，确保关闭
            try:
                conn.close()
            except:
                pass
            raise e
    
    def get_user_by_name(self, name):
        """根据姓名获取用户信息（获取最新的一条）"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM users
            WHERE name = ?
            ORDER BY created_at DESC
            LIMIT 1
        ''', (name,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return dict(row)
        return None
    
    def get_history_by_id(self, history_id):
        """根据ID获取历史记录详情"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT h.*, u.name, u.birthday, u.zodiac, u.mbti
            FROM analysis_history h
            JOIN users u ON h.user_id = u.id
            WHERE h.id = ?
        ''', (history_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            record = dict(row)
            # 解析JSON字符串
            try:
                record['analysis_result'] = json.loads(record['analysis_result'])
            except (json.JSONDecodeError, TypeError):
                # 如果已经是字典，直接使用
                if isinstance(record['analysis_result'], dict):
                    pass
                else:
                    record['analysis_result'] = {}
            return record
        return None

