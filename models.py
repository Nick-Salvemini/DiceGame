from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# users

# id
# email
# username
# password
# player_icon
# matches_played_vs_cpu
# wins_vs_cpu
# loses_vs_cpu
# ties_vs_cpu
# matches_player_vs_player
# wins_vs_player
# loses_vs_player
# ties_vs_player

# matches

# player_1_id
# player_1_is_human
# player_1_score
# player_2_id
# player_2_is_human
# player_2_score
# match_datetime