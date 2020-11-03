from mongoengine import *


class Address(EmbeddedDocument):
    street = StringField()
    number = IntField()
    neighborhood = StringField()
    zipcode = StringField()
    city = StringField()
    state = StringField()
    country = StringField()
