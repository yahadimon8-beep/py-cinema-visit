from app.people.customer import Customer


class CinemaBar:
    """Cinema bar that sells products to customers."""

    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        """Sell a product to a customer."""
        print(f"Cinema bar sold {product} to {customer.name}.")
