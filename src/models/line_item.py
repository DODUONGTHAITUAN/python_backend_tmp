from src import db
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    func,
    ForeignKey,
)

from .order import Order
from .product import Product

# Define class
class LineItem(db.Model):
    __tablename__ = "LineItem"

    # Define Columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    orderID = Column(Integer, ForeignKey(Order.id))
    productID = Column(Integer, ForeignKey(Product.id))
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    # Constructor
    def __init__(self):
        pass
