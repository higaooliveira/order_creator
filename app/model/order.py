from mongoengine import *

from app.model.customer import Customer
from app.model.product import Product


class Order(DynamicDocument):
    _id = StringField()
    customer = EmbeddedDocumentField(Customer)
    products = EmbeddedDocumentListField(Product)
    totalPrice = DecimalField()
    status = StringField()
