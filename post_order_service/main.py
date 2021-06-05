"""post_order_service main module"""
import asyncio
from typing import Optional

import aio_pika
from fastapi import FastAPI
from pydantic import BaseModel


class Order(BaseModel):
    product_code: str
    qty: Optional[int] = 1


app = FastAPI()

@app.post("/orders/")
async def create_order(order: Order):
    loop = asyncio.get_event_loop()
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/", loop=loop
    )

    routing_key = "test_queue"

    channel = await connection.channel()    # type: aio_pika.Channel

    await channel.default_exchange.publish(
        aio_pika.Message(
            body='Hello {}'.format(routing_key).encode()
        ),
        routing_key=routing_key
    )

    await connection.close()
    return order