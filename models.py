from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    '''Model for users account data and match history'''

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    email = db.Column(
        db.String,
        nullable=False,
        unique=True
    )

    username = db.Column(
        db.String,
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.String,
        nullable=False
    )

    # player_icon = db.Column(

    # )

    matches_played_vs_cpu = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    wins_vs_cpu = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    loses_vs_cpu = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    ties_vs_cpu = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    matches_player_vs_player = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    wins_vs_player = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    loses_vs_player = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    ties_vs_player = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )


class Match(db.Model):
    '''Model for information on each individual match'''

    __tablename__ = 'matches'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    player_1_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )

    player_1_is_human = db.Column(
        db.Boolean,
    )

    player_1_score = db.Column(
        db.Integer,
        default=0
    )

    player_2_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        default=0
    )

    player_2_is_human = db.Column(
        db.Boolean,
    )

    player_2_score = db.Column(
        db.Integer,
        default=0
    )

    match_datetime = db.Column(
        db.DateTime
    )

    users = db.relationship('User')
