from example_package.example import add_one, add_two


def main():
    print("hello world!")
    print(f"1 add_one is: {add_one(1)}")
    print_more_stuff()
    print(f"3 add_two is: {add_two(3)}")

def print_more_stuff():
    print("This is more stuff")

if __name__ == "__main__":
    main()