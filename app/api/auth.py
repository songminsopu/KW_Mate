from flask import request, jsonify, Blueprint, session, g
from app.models import User
import bcrypt
from app import db
from flask_cors import cross_origin

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/', methods=['POST'])
def singnup():
    try:
        std_id = request.json["std_id"]
        pw = bcrypt.hashpw(request.json['pw'].encode("utf-8"), bcrypt.gensalt())
        name = request.json["name"]
        age = request.json["age"]
        insta = request.json["insta"]
        kakao = request.json["kakao"]
        gender = request.json["gender"]

        user = User(
            std_id=std_id,
            pw=pw,
            name=name,
            age=age,
            insta=insta,
            kakao=kakao,
            gender=gender
        )
        db.session.add(user)
        db.session.commit()
        db.session.remove()

        return jsonify({
            'code': 1,
            'msg': "회원가입 성공",
        })
    except Exception as e:
        return jsonify({
            'code': -1,
            'msg': f"{e}",
        })

@bp.route('/login/', methods=['POST'])
def login():
    error = None
    user = User.query.filter_by(std_id=request.json["std_id"]).first()

    if not user:
        error = "존재하지 않는 사용자입니다."
    elif not bcrypt.checkpw(request.json['pw'].encode('utf-8'), user.pw):
        error = "비밀번호가 올바르지 않습니다."

    if error is None:
        session.clear()
        session['user_id'] = user.id
        return jsonify({
                'code': 1,
                'msg': "로그인 성공",
        })
    else:
        return jsonify({
            'code': -1,
            'msg': error,
        })

@bp.route('/logout/', methods=['GET'])
def logout():
    session.clear()
    return jsonify({
        'code': 1,
        'msg': "로그아웃",
    })
@cross_origin(supports_credentials=True)
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

