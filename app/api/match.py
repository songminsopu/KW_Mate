from flask import request, jsonify, Blueprint, session, g
from app.models import User, BlockedList
from app import db
from flask_cors import CORS

import random
import string

bp = Blueprint('match', __name__, url_prefix='/match')
CORS(bp, supports_credentials=True)


@bp.route("/detail/", methods=["POST"])
def detail_match():
    if True or g.user:
        std_id = request.json["std_id"]

        users = User.query.filter(User.active & (User.std_id != std_id)).all()
        user = User.query.filter(User.std_id == std_id).first()

        user.talking = request.json["talking"]  # 유저가 원하는
        user.menu = request.json["menu"]  # 유저가 원하는
        user.description = request.json["description"]  # 간단 소개
        user.active = True
        db.session.commit()

        blocked_lst = BlockedList.query.filter(BlockedList.blocker == std_id).all()
        blocked_users = [bu.blocked_user for bu in blocked_lst]

        age = request.json["age"]  # 유저가 원하는 나이
        gender = request.json["gender"]  # 유저가 원하는 성별

        result = []
        for x in users:
            if x.std_id in blocked_users:  # 차단한 유저 넘기기
                continue
            score = 0

            if x.gender != gender:  # same gender
                score += 1
            if x.menu == user.menu:  # same menu
                score += 1
            if x.talking == user.talking:  # same talking
                score += 1
            if max([age, x.age]) - min(age, x.age) <= 3:  # years apart < 4
                score += 1

            res = score * 25  # temporary, * 25 can be changed when algorithm come to clear
            result.append({
                'std_id': x.std_id,
                'name': x.name,
                'age': x.age,
                'insta': x.insta,
                'kakao': x.kakao,
                'description': x.description,
                'blocked_cnt': x.blocked_cnt,
                'score': res
            })
            result.sort(reverse=True, key=lambda u: u['score'])

        db.session.remove()
        return jsonify({
            "code": 1,
            "matching_list": result
        })
    else:
        return jsonify({
            "code": -1,
            "matching_list": []
        })

@bp.route("/simple/<string:std_id>/<string:menu>", methods=["GET"])
def simple_match(std_id, menu):
    if True or g.user:

        users = User.query.filter(User.active & (User.std_id != std_id) & (User.menu == menu)).all()
        result = []
        blocked_lst = BlockedList.query.filter(BlockedList.blocker == std_id).all()
        blocked_users = [bu.blocked_user for bu in blocked_lst]

        for user in users:
            if user.std_id in blocked_users:
                continue

            result.append({
                'std_id': user.std_id,
                'name': user.name,
                'age': user.age,
                'insta': user.insta,
                'kakao': user.kakao,
                'description': user.description,
                'blocked_cnt': user.blocked_cnt,
            })
        return jsonify({
            "code": 1,
            "matching_list": result
        })
    else:
        return jsonify({
            "code": -1,
            "matching_list": []
        })

@bp.route("/cancel/<string:std_id>", methods=["GET"])
def match_cancel(std_id):
    user = User.query.filter(User.std_id == std_id).first()
    user.active = False
    db.session.commit()
    db.session.remove()
    return jsonify({
        "code": 1,
        "msg": "매칭 종료"
    })

@bp.route("/make_users/", methods=["GET"])
def make_users():
    n = 20

    for i in range(n):
        std_id = str(random.choice(list(range(1, n))))
        pw = ''.join([str(random.choice(string.ascii_uppercase + string.digits)) for _ in range(4)])
        name = 'user ' + ''.join([str(random.choice(string.ascii_uppercase + string.digits)) for _ in range(4)])
        age = str(random.choice(list(range(19, 25))))
        insta = ''.join([str(random.choice(string.ascii_uppercase + string.digits)) for _ in range(7)])
        kakao = ''.join([str(random.choice(string.ascii_uppercase + string.digits)) for _ in range(7)])
        gender = random.choice(['male', 'female'])

        menu = random.choice(['c', 'j', 'k', 'w'])  # chinese, japanese, korean, western
        talking = random.choice(['little', 'lot'])  # talking
        description = ''.join([str(random.choice(string.ascii_uppercase + string.digits)) for _ in range(4)])
        try:
            user = User(
                std_id=std_id,
                pw=pw,
                name=name,
                age=age,
                insta=insta,
                kakao=kakao,
                gender=gender,
                menu=menu,
                talking=talking,
                description=description,
                active=True
            )
            db.session.add(user)
            db.session.commit()
        except:
            continue
    db.session.remove()
    return jsonify({
        "code": 1,
        "msg": "데모 유저 막 만듬"
    })