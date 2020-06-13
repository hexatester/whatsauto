from .base import BaseClient
from dataclasses import dataclass
from collections import namedtuple

Reply = namedtuple('Reply', ['message', 'sticker'])


@dataclass
class BaseMessage:
    time: str
    date: str
    reply: Reply


class StatusMessage:
    text: str


@dataclass
class Message(BaseMessage):
    text: str
    reply: Reply


@dataclass
class Sticker(BaseMessage):
    name: str
    creator: str


class ConversationUi(BaseClient):
    def search(self, message):
        pass
