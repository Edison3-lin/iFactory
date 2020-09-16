#!/usr/bin/env python
import pika
def MQ_send(message):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='Edison')

        channel.basic_publish(exchange='', routing_key='Edison', body=message)
        print(" [x] Sent ''%s'' "%message)
        connection.close()
        return True
        
    except:
        return False    