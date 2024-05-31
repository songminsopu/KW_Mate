import random
import string

from app.models import User
import app


n = 20

for i in range(n):
    std_id = str(random.choice(list(range(1, n))))
    pw = ''.join([str(random.choice(string.ascii_uppercase + string.digits)) for _ in range(4)])
    name = 'user ' + ''.join([str(random.choice(string.ascii_uppercase + string.digits)) for _ in range(4)])
    age = str(random.choice(list(range(19,25))))
    insta = ''.join([str(random.choice(string.ascii_uppercase + string.digits)) for _ in range(7)])
    kakao = ''.join([str(random.choice(string.ascii_uppercase + string.digits)) for _ in range(7)])
    gender = random.choice(['male', 'female'])

    menu = random.choice(['c', 'j', 'k', 'w'])  # chinese, japanese, korean, western
    talking = random.choice(['little', 'lot'])  # talking
    description = ''.join([str(random.choice(string.ascii_uppercase + string.digits)) for _ in range(4)])

    user = User(
        std_id=std_id,
        pw=pw,
        name=name,
        age=age,
        insta=insta,
        kakao=kakao,
        gender=gender
    )
    app.db.session.add(user)
    app.db.session.commit()
app.db.session.remove()

