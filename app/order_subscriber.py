import pika
from mongoengine import connect

from app.model.order import Order

connect("order_register")


def order_creator(channel, method, properties, body):
    try:
        order = Order.from_json(body)
        order.save()
        print("[x] Received message to create order to user: {}".format(order.customer.email))
    except Exception as ex:
        print(f"An error occurred while trying to save your order in db {ex}")


def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='createOrder')
    channel.basic_consume('createOrder', order_creator, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
