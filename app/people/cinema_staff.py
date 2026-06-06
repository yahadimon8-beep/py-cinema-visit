class Cleaner:
    """Cleaner who cleans cinema halls."""

    def __init__(self, name: str) -> None:
        """Initialize a cleaner with a name."""
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """Clean a cinema hall."""
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
