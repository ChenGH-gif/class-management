from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    student_id = db.Column(db.String(20), unique=True, nullable=True)
    gender = db.Column(db.String(10), default='未知')
    group = db.Column(db.String(20), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    total_score = db.Column(db.Float, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    scores = db.relationship('ScoreRecord', backref='student', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'student_id': self.student_id,
            'gender': self.gender,
            'group': self.group,
            'phone': self.phone,
            'notes': self.notes,
            'total_score': self.total_score,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class ScoreRecord(db.Model):
    __tablename__ = 'score_records'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    score_type = db.Column(db.String(50), nullable=False)  # 奖励/扣分
    category = db.Column(db.String(50), nullable=True)  # 学习/纪律/活动等
    score = db.Column(db.Float, nullable=False)  # 分数
    reason = db.Column(db.Text, nullable=True)
    operator = db.Column(db.String(50), default='系统')
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'student_name': self.student.name if self.student else '',
            'score_type': self.score_type,
            'category': self.category,
            'score': self.score,
            'reason': self.reason,
            'operator': self.operator,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
