""" alchemy"""
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Define the database connection URL
DATABASE_URL = "postgresql://postgres:postgres@localhost/shiva"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a base class for declarative models
Base = declarative_base()

class Match(Base):
    """ class for create matches table"""
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)
    season = Column(Integer)
    city = Column(String)
    date = Column(Date)
    team1 = Column(String)
    team2 = Column(String)
    toss_winner = Column(String)
    toss_decision = Column(String)
    result = Column(String)
    dl_applied = Column(Integer)
    winner = Column(String)
    win_by_runs = Column(Integer)
    win_by_wickets = Column(Integer)
    player_of_match = Column(String)
    venue = Column(String)
    umpire1 = Column(String)
    umpire2 = Column(String)
    umpire3 = Column(String)

    deliveries = relationship("Delivery", back_populates="match")

class Delivery(Base):
    """ class to create deliveries table"""
    __tablename__ = 'deliveries'
    id = Column(Integer,autoincrement=True,primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'))
    inning = Column(Integer, primary_key=True)
    batting_team = Column(String)
    bowling_team = Column(String)
    over = Column(Integer)
    ball = Column(Integer)
    batsman = Column(String)
    non_striker = Column(String)
    bowler = Column(String)
    is_super_over = Column(Integer)
    wide_runs = Column(Integer)
    bye_runs = Column(Integer)
    legbye_runs = Column(Integer)
    noball_runs = Column(Integer)
    penalty_runs = Column(Integer)
    batsman_runs = Column(Integer)
    extra_runs = Column(Integer)
    total_runs = Column(Integer)
    player_dismissed = Column(String)
    dismissal_kind = Column(String)
    fielder = Column(String)

    match = relationship("Match", back_populates="deliveries")

class Umpire(Base):
    """ class to create umpires table"""
    __tablename__ = 'umpires'
    id = Column(Integer,autoincrement=True,primary_key=True)
    umpire = Column(String)
    country = Column(String)


# Create tables in the database
Base.metadata.create_all(engine)
