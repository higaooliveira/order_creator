from mongoengine import *


class Product(EmbeddedDocument):
    sku = StringField()
    name = StringField()
    quantity = IntField()
    price = DecimalField()
