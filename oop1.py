#using classes



#using functions
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    return input("What's your name? ")


def get_house():
    return input("What's your house? ")


if __name__ == "__main__":
    main() 