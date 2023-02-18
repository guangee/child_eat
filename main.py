import pika
import keyboard
import os

hostname = 'localhost'
port = 5672
credentials = pika.PlainCredentials(username='admin', password='1234567890Aa')
parameters = pika.ConnectionParameters(host=hostname, port=port, credentials=credentials)


def on_keyboard(x):
    if x.event_type == 'down':
        if x.name == 'up':
            os.system('mplayer /root/drink.mp3')
        if x.name == 'down':
            os.system('mplayer /root/finish.mp3')
        connection = pika.BlockingConnection(parameters=parameters)
        channel = connection.channel()
        channel.queue_declare(queue='test')
        channel.basic_publish(exchange='', routing_key='test', body=x.name)
        print(x.name)
        connection.close()


if __name__ == '__main__':
    print("start success")
    keyboard.hook(on_keyboard)
    keyboard.wait()
