from aiogram import Dispatcher
from aiogram.types import Message


async def echo(msg: Message):
    # todo: remove echo example:3
    await msg.answer(msg.text)


def register_other_handlers(dp: Dispatcher) -> None:
    # todo: register all other handlers
    dp.register_message_handler(echo, content_types=['text'])