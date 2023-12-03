# utils.py
from sqlalchemy import create_engine, select, and_
from sqlalchemy.orm import sessionmaker

from .models import Base, Monitoring


def init_db(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)


def is_monitoring_enabled(name, room_id):
    stmt = select(Monitoring).where(and_(Monitoring.monitoring_type == name, Monitoring.roomId == room_id))
    row = db_session.execute(stmt).fetchone()
    if not row:
        return False
    return row[Monitoring.enabled]


Session = init_db("sqlite:///botmate.db")
db_session = Session()
