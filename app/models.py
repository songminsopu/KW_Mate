from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    std_id = db.Column(db.String(200), unique=True, nullable=False)
    pw = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(200), nullable=False)

    # 매칭 후 연락용
    insta = db.Column(db.String(200), nullable=False)
    kakao = db.Column(db.String(200), nullable=False)
    
    # 최초 회원가입 이후에 매칭시 입력될 것들
    menu = db.Column(db.String(200), nullable=True)
    description = db.Column(db.String(200), nullable=True)
    talking = db.Column(db.String(200), nullable=True)

    active = db.Column(db.Boolean, server_default='0', nullable=True)
    blocked_cnt = db.Column(db.Integer, server_default='0', nullable=True)

# class Match(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     std_id = db.Column(db.String(200), db.ForeignKey('user.std_id', ondelete='CASCADE'), unique=True, nullable=False)
#     user = db.relationship('User', backref=db.backref('answer_set', cascade='all, delete-orphan'))
#     name = db.Column(db.String(200), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     description = db.Column(db.String(200), nullable=False)
#     menu = db.Column(db.String(200), nullable=False)
#     blocked_cnt = db.Column(db.Integer, nullable=False)

class BlockedList(db.Model):
    # 외래키 설정 해야 하는데 ㅈㄴ 귀찮다 걍 ㄱㄱ
    id = db.Column(db.Integer, primary_key=True)
    blocker = db.Column(db.String(200), nullable=False)
    blocked_user = db.Column(db.String(200), nullable=False)