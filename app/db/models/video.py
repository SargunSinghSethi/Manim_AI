from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.models.base import Base

class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    job_id = Column(String, unique=True)
    title = Column(String)
    video_url = Column(String)  # S3 URL or local path
    created_at = Column(DateTime, default=datetime.utcnow())

    user = relationship("User", backref="videos")
