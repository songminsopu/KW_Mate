from flask import request, jsonify, Blueprint, g
from app.models import User, BlockedList
from app import db
from flask_cors import CORS

bp = Blueprint('block', __name__, url_prefix='/block')
CORS(bp, supports_credentials=True)


@bp.route('/', methods=["POST", "DELETE"])
def block():
    if True or g.user:
        blocker = request.json["std_id"]
        blocked_user = request.json["bu_std_id"]
        bu_user = User.query.filter(User.std_id == blocked_user).first()

        if request.method == "POST":
            blocked_lst = BlockedList(
                blocker=blocker,
                blocked_user=blocked_user
            )
            bu_user.blocked_cnt += 1

            db.session.add(blocked_lst)
            db.session.commit()
            db.session.remove()
            return jsonify({
                "code": 1,
                "msg": "차단 완료"
            })
        elif request.method == "DELETE":
            blocked_lst = BlockedList.query.filter(
                (BlockedList.blocker == blocker) & (BlockedList.blocked_user == blocked_user)
            ).first()
            bu_user.blocked_cnt -= 1

            db.session.delete(blocked_lst)
            db.session.commit()
            db.session.remove()
            return jsonify({
                "code": 1,
                "msg": "차단 해제 완료"
            })
    else:
        return jsonify({
            "code": -1,
            "msg": "차단 실패"
        })

@bp.route('/block_users/<string:std_id>', methods=["GET"])
def block_users(std_id):
    if g.user and g.user.std_id == std_id:
        blocked_lst = BlockedList.query.filter(BlockedList.blocker == std_id).all()

        result = []
        for blocked in blocked_lst:
            user = User.query.filter(User.std_id == blocked.blocked_user).first()
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
            "blocked_lst": result
        })
    else:
        return jsonify({
            "code": -1,
            "msg": "조회 실패"
        })