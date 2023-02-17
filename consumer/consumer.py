import pika, json
from rich.pretty import  pretty_repr
from datetime import datetime

params = pika.URLParameters('amqps://mmbswtkj:86-N4IDgbgw8rOZOsWzJd1tTCA27weth@beaver.rmq.cloudamqp.com/mmbswtkj')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='log')

def callback(ch, method, properties, body):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Received at:", current_time)
    data = json.loads(body)
    print(pretty_repr(data))

channel.basic_consume(queue='log', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()