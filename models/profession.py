from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class Profession(Base):
  __tablename__ = "profession"

  id = Column(Integer, primary_key=True)
  name = Column(String)

  customers = relationship("Customer", back_populates="profession", cascade="all, delete")
