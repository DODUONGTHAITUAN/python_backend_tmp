from src import db
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Float
from .user import User
from .allcodes import Allcodes


class Order(db.Model):
    __tablename__ = "Order"

    # Define column
    id = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(Integer, ForeignKey(User.id))
    statusID = Column(String(255), ForeignKey(Allcodes.keyMap))
    orderDate = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=True
    )
    totalPrice = Column(Float, nullable=True)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    # Constructor
    def __init__(self):
        pass
