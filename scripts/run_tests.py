"""Run simple test functions from the tests package.

This runner imports any callables starting with `test_` from test modules
under `tests` and executes them, printing PASS/FAIL.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import tests.test_greetings as t


def main():
    failed = False
    for name in dir(t):
        if name.startswith("test_"):
            fn = getattr(t, name)
            try:
                fn()
                print(f"PASS {name}")
            except AssertionError as e:
                print(f"FAIL {name}: {e}")
                failed = True
            except Exception as e:
                print(f"ERROR {name}: {e}")
                failed = True

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
