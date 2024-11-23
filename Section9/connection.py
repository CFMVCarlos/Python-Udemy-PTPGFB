class Connection:
    def __init__(self, connection_type: str, cost: float) -> None:
        print(f"{connection_type} connection established! (Cost: ${cost}/h)")
        self.connection_type: str = connection_type
        self.cost: float = cost

    def close_connection(self) -> None:
        print(f"Closing {self.connection_type} connection...")


if __name__ == "__main__":
    internet: Connection = Connection("Internet", 2)
    satellite: Connection = Connection("Satellite", 20)

    internet.close_connection()
    satellite.close_connection()
