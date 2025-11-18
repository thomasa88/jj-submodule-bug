"""Main entrypoint for the sample project."""

from submodule_a import greet as greet_a
from submodule_b import greet as greet_b


def main():
    print("Main project starting...")
    print(greet_a())
    print(greet_b())


if __name__ == "__main__":
    main()
