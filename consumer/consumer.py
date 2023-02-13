import pika, json
from rich.pretty import  pretty_repr

params = pika.URLParameters('amqps://mmbswtkj:86-N4IDgbgw8rOZOsWzJd1tTCA27weth@beaver.rmq.cloudamqp.com/mmbswtkj')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='log')

def callback(ch, method, properties, body):
    print('Received in ...')
    data = json.loads(body)
    print(pretty_repr(data))

    # if properties.content_type == 'product_created':
    #     product = Product(id=data['id'], title=data['title'], image=data['image'])
    #     db.session.add(product)
    #     db.session.commit()
    #     print('Product Created')

    # elif properties.content_type == 'product_updated':
    #     product = Product.query.get(data['id'])
    #     product.title = data['title']
    #     product.image = data['image']
    #     db.session.commit()
    #     print('Product Updated')

    # elif properties.content_type == 'product_deleted':
    #     product = Product.query.get(data)
    #     db.session.delete(product)
    #     db.session.commit()
    #     print('Product Deleted')


channel.basic_consume(queue='log', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()