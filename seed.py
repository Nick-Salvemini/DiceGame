from models import db, User, Match
import app
from sqlalchemy import text

# db.drop_all()
# db.create_all()

Match.query.delete()
User.query.delete()

# sql = text('DROP users CASCADE')
# db.engine.execute(sql)


u1 = User(
    email='test1@gmail.com',
    username='testuser1',
    password='password1',
    matches_played_vs_cpu=1,
    loses_vs_cpu=1,
    matches_player_vs_player=2,
    loses_vs_player=2
)

u2 = User(
    email='test2@gmail.com',
    username='testuser2',
    password='password2',
    matches_played_vs_cpu=1,
    wins_vs_cpu=1,
    matches_player_vs_player=2,
    wins_vs_player=2,
)

u3 = User(
    email='test3@gmail.com',
    username='testuser3',
    password='password3',
    matches_played_vs_cpu=1,
    ties_vs_cpu=1,
    matches_player_vs_player=2,
    wins_vs_player=1,
    loses_vs_player=1,
)

test_users = [u1, u2, u3]

db.session.add(test_users)
db.session.commit()

m1 = Match(
    player_1_id=u1.id,
    player_1_is_human=True,
    player_1_score=30,
    player_2_is_human=False,
    player_2_score=40
)

m2 = Match(
    player_1_id=u2.id,
    player_1_is_human=True,
    player_1_score=41,
    player_2_is_human=False,
    player_2_score=29
)

m3 = Match(
    player_1_id=u3.id,
    player_1_is_human=True,
    player_1_score=36,
    player_2_is_human=False,
    player_2_score=36
)

m4 = Match(
    player_1_id=u1.id,
    player_1_is_human=True,
    player_1_score=32,
    player_2_id=u2.id,
    player_2_is_human=True,
    player_2_score=43
)

m5 = Match(
    player_1_id=u1.id,
    player_1_is_human=True,
    player_1_score=41,
    player_2_id=u3.id,
    player_2_is_human=True,
    player_2_score=42
)

m6 = Match(
    player_1_id=u2.id,
    player_1_is_human=True,
    player_1_score=39,
    player_2_id=u3.id,
    player_2_is_human=True,
    player_2_score=35
)

test_matches = [m1, m2, m3, m4, m5, m6]

db.session.add(test_matches)
db.session.commit()
