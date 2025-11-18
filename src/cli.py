"""Command-line interface for the greeting generator.

Usage (simple):
    python -m src.cli --name Alice --occasion birthday --tone friendly
"""
from __future__ import annotations

import argparse
from .greetings import GreetingGenerator


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Generate a short greeting message")
    p.add_argument("--name", "-n", help="Recipient name", default=None)
    p.add_argument("--occasion", "-o", help="Occasion (birthday, new year, etc.)", default=None)
    p.add_argument("--tone", "-t", help="Tone: friendly, formal, playful", default="friendly")
    p.add_argument("--seed", type=int, help="Optional integer seed for deterministic output", default=None)
    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    gen = GreetingGenerator(seed=args.seed)
    msg = gen.generate_greeting(name=args.name, occasion=args.occasion, tone=args.tone)
    print(msg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
