from sqlalchemy import Column, Integer, String, Enum, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Monitoring(Base):
    __tablename__ = 'monitoring'
    id = Column(Integer, primary_key=True)
    roomId = Column(String, nullable=False)
    monitoring_type = Column(Enum('tms_monitoring', 'cluster_monitoring'), nullable=False)
    enabled = Column(Boolean, default=False)
