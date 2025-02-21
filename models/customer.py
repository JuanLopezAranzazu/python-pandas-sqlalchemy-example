from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
import enum

class GenderEnum(enum.Enum):
  Female = "Female",
  Male = "Male"

class Customer(Base):
  __tablename__ = "customer"

  id = Column(Integer, primary_key=True)
  gender = Column(Enum(GenderEnum))
  age = Column(Integer)
  annual_income = Column(Integer)
  spending_score = Column(Integer)
  work_experience = Column(Integer)
  family_size = Column(Integer)
  profession_id = Column(Integer, ForeignKey("profession.id"))

  profession = relationship("Profession", back_populates="customers")
