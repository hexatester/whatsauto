#!/usr/bin/env python
"""Class for representing a Sticker in chat"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from whatsauto import WhatsAutoObject


@dataclass
class Sticker(WhatsAutoObject):
    time: Optional[datetime] = None
