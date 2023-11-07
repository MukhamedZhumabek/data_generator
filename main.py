import asyncio
import sys
from logging import getLogger
from time import perf_counter

import settings
from core.data_generator import get_message
from core.publisher import publish

logger = getLogger(__name__)


async def sender(rpc: int = 50, duration: int = 60):
    current = 1
    while current <= duration:
        logger.info(f'Start data generator with params rpc {rpc} duration {duration}')
        start = perf_counter()
        tasks = []
        for _ in range(rpc):
            task = asyncio.create_task(publish(get_message()))
            tasks.append(task)
        await asyncio.gather(*tasks)
        stop = perf_counter()
        logger.info(f'time: {stop - start}')
        logger.info(f'{current}:{current * rpc}')
        current += 1
        await asyncio.sleep(1)


if __name__ == "__main__":
    rpc = settings.default_rpc
    duration = settings.default_duration

    if len(sys.argv) > 1:
        rpc = int(sys.argv[1])

    if len(sys.argv) > 2:
        duration = int(sys.argv[2])

    asyncio.run(sender(rpc, duration))
