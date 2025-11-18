"""Lightweight greeting message generator used by the project.

Provides a small, deterministic (by default) GreetingGenerator that can
produce friendly, formal, or playful greetings for a given name and
occasion. No external dependencies.
"""
from __future__ import annotations

from datetime import datetime
import random
from typing import Optional


class GreetingGenerator:
    """Generate short greeting messages.

    Methods
    - generate_greeting(name, occasion, tone) -> str
    """

    def __init__(self, seed: Optional[int] = None):
        # Seed for reproducible output during tests
        self._rand = random.Random(seed)

    def generate_greeting(self, name: Optional[str] = None, occasion: Optional[str] = None, tone: str = "friendly") -> str:
        """Return a greeting string tailored to the inputs.

        Args:
            name: optional recipient name
            occasion: optional occasion (e.g., "birthday", "new year")
            tone: one of "friendly", "formal", "playful"

        Returns:
            A short greeting message.
        """
        now = datetime.now()
        time_of_day = _time_of_day(now.hour)

        # Base templates by tone
        templates = {
            "friendly": [
                "Good {time}, {name}! Hope you're having a lovely {occasion}.",
                "Hey {name}! {time_cap} — wishing you a great {occasion}.",
                "{time_cap}, {name}! Sending warm {occasion} wishes.",
            ],
            "formal": [
                "Good {time}, {name}. Best wishes for the {occasion}.",
                "{time_cap}. Dear {name}, please accept my {occasion} greetings.",
            ],
            "playful": [
                "Yo {name}! {time_cap} — {occasion} incoming 🎉",
                "Hello {name}! Ready for a {occasion}? {time_cap}!",
            ],
        }

        if tone not in templates:
            tone = "friendly"

        tpl = self._rand.choice(templates[tone])

        name_text = name or "friend"
        occasion_text = occasion or "day"
        time_cap = time_of_day.capitalize()

        return tpl.format(time=time_of_day, time_cap=time_cap, name=name_text, occasion=occasion_text)


def _time_of_day(hour: int) -> str:
    if 5 <= hour < 12:
        return "morning"
    if 12 <= hour < 17:
        return "afternoon"
    if 17 <= hour < 22:
        return "evening"
    return "night"
