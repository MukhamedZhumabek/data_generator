import logging

from dotenv import dotenv_values

logging.basicConfig(
    level=logging.INFO,
    filename="./log/generator.log",
    format="%(asctime)s - %(levelname)s - %(module)s  - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)

default_rpc = 50
default_duration = 60

# == rabbitmq == #
rabbit_settings = dotenv_values('.env.rabbit')
RABBITMQ_PUBLISH_QUEUE = rabbit_settings['RABBITMQ_PUBLISH_QUEUE']
RABBITMQ_HOST = rabbit_settings['RABBITMQ_HOST']
RABBITMQ_USER = rabbit_settings['RABBITMQ_USER']
RABBITMQ_PASSWORD = rabbit_settings['RABBITMQ_USER']
RABBITMQ_URL = f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}/'
