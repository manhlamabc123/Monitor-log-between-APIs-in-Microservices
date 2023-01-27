# amqps://mmbswtkj:86-N4IDgbgw8rOZOsWzJd1tTCA27weth@beaver.rmq.cloudamqp.com/mmbswtkj
import pika

params = pika.URLParameters('amqps://mmbswtkj:86-N4IDgbgw8rOZOsWzJd1tTCA27weth@beaver.rmq.cloudamqp.com/mmbswtkj')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')