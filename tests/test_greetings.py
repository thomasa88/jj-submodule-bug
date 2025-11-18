from src.greetings import GreetingGenerator


def test_generate_default():
    g = GreetingGenerator(seed=0)
    msg = g.generate_greeting(name="Alice", occasion="birthday", tone="friendly")
    assert "Alice" in msg
    assert "birthday" in msg


def test_time_of_day_playful():
    g = GreetingGenerator(seed=1)
    msg = g.generate_greeting(name="Bob", occasion="party", tone="playful")
    assert any(word in msg.lower() for word in ["party", "party"])
