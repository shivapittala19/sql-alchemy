from models import Match, Delivery, Umpire,engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()

class IPLdata:
    def runs_scored_by_team():
        #   Total runs scored by team
        return session.query(
            Delivery.batting_team,
            func.sum(Delivery.total_runs)
            ).group_by(Delivery.batting_team).all()

    def rcb_batsman():
        #  Top batsman for Royal Challengers Bangalore
        return   session.query(
            Delivery.batsman,func.sum(Delivery.batsman_runs))\
            .filter(Delivery.batting_team == 'Royal Challengers Bangalore')\
            .group_by(Delivery.batsman).order_by(func.sum(Delivery.batsman_runs).desc())\
            .limit(10).all()

    def matches_played_per_year():
        # Number of matches played per year for all the years in IPL
        return  session.query(Match.season,func.count(Match.season))\
            .group_by(Match.season)\
            .order_by(Match.season).all()

    def matches_won_per_team():
        # Number of matches won per team per year in IPL
        return  session.query(Match.season, Match.winner,func.count(Match.winner))\
            .group_by(Match.winner,Match.season)\
            .order_by(Match.season).all()

    def extra_runs_conceded():
        # Extra runs conceded per team in the year 2016
        return  session.query(Delivery.bowling_team,func.sum(Delivery.extra_runs))\
            .join(Match,Delivery.match_id == Match.id)\
            .filter(Match.season == 2016)\
            .group_by(Delivery.bowling_team)\
            .order_by(Delivery.bowling_team).all()

session.close()
