from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.db.models.base import Base

class JobStatus(str, enum.Enum):
    pending = "pending"
    running = "running"
    completed = "completed"
    failed = "failed"

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    prompt = Column(String)
    job_uuid = Column(String, unique=True)
    status = Column(Enum(JobStatus), default=JobStatus.pending)
    error_message = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow())

    user = relationship("User", backref="jobs")
