class Customer:
    """Customer who watches movies and buys food."""

    def __init__(self, name: str, food: str) -> None:
        """Initialize a customer with name and food preference."""
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """Print that the customer is watching a movie."""
        print(f'{self.name} is watching "{movie}".')
