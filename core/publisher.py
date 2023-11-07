import json
from logging import getLogger

from aio_pika import Message, connect
import settings

logger = getLogger(__name__)


async def publish(message) -> None:
    connection = await connect(settings.RABBITMQ_URL)
    channel = await connection.channel()
    queue = await channel.declare_queue("first")
    async with connection:
        await channel.default_exchange.publish(
            Message(json.dumps(message).encode('utf-8')),
            routing_key=queue.name,
        )
        logger.info(f"publish {message}")
