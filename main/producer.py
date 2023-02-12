# amqps://mmbswtkj:86-N4IDgbgw8rOZOsWzJd1tTCA27weth@beaver.rmq.cloudamqp.com/mmbswtkj
import pika, json

params = pika.URLParameters('amqps://mmbswtkj:86-N4IDgbgw8rOZOsWzJd1tTCA27weth@beaver.rmq.cloudamqp.com/mmbswtkj')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='log', body=json.dumps(body), properties=properties)