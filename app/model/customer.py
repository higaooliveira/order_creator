from mongoengine import *

from app.model.address import Address


class Customer(DynamicEmbeddedDocument):
    id = StringField()
    name = StringField()
    email = StringField()
    address = EmbeddedDocumentField(Address)
