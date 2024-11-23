def main() -> None:
    status: int = 200

    match status:
        case 200:
            print("Success!")
        case 404:
            print("Not found!")
        case 500:
            print("Server error!")
        case _:
            print("Unknown status code!")

    print()

    while True:
        user_input: str = input("Enter a command: ")
        command: list[str] = user_input.split()

        match command:
            case "find", *images:
                print(f"Finding images: {images}")
            case "enlarge", image, ammount:
                print(f"Enlarging {image} by {ammount}x")
            case "rename", image, new_name if len(new_name) > 3:
                print(f"'{image}' renamed to '{new_name}'")
            case "download", *images:
                print(f"Downloading images: {images}")
            case "x" | "delete", *images:
                print(f"Deleting images: {images}")
            case _:
                print("Unknown command!")


if __name__ == "__main__":
    main()
