from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    """Cinema hall where movies are shown."""

    def __init__(self, number: int) -> None:
        """Initialize a cinema hall with a number."""
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        customers: list[Customer],
        cleaning_staff: Cleaner,
    ) -> None:
        """Run a movie session with customers and cleaning."""
        print(f"\"{movie_name}\" started in hall number {self.number}.")
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f"\"{movie_name}\" ended.")
        cleaning_staff.clean_hall(hall_number=self.number)
