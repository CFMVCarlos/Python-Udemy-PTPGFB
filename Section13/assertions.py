def start_program(db: dict[int, str]) -> None:
    assert db, "Database is empty."

    print("Loaded: ", db)
    print("Program started.")


if __name__ == "__main__":
    # db1: dict[int, str] = {}
    db1: dict[int, str] = {0: "a", 1: "b", 2: "c"}
    start_program(db1)
