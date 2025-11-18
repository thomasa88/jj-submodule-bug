"""Main entrypoint for the sample project.

This script keeps compatibility with the example submodules while also
demonstrating the local greeting generator.
"""

from submodule_a import greet as greet_a
from submodule_b import greet as greet_b
from .greetings import GreetingGenerator


def main():
    print("Main project starting...")
    # Existing submodule greetings (if available)
    try:
        print(greet_a())
    except Exception:
        print("(submodule_a greeting unavailable)")

    try:
        print(greet_b())
    except Exception:
        print("(submodule_b greeting unavailable)")

    # Use the new local generator for a sample message
    gen = GreetingGenerator()
    print(gen.generate_greeting(name="Developer", occasion="project demo", tone="friendly"))


if __name__ == "__main__":
    main()
