"""Entrypoint for the ATO organization service."""

from api import create_app

app = create_app()


def main() -> int:
    """Validate that the service application can be imported."""
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
