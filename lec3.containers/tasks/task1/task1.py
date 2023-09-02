from firelink import *


def main():
    print(
        f"Select a website to open : [ {', '.join(list(favourite_websites.keys()))} ]")
    website_name = input().lower().strip()

    firefox(favourite_websites[website_name])


if __name__ == '__main__':
    main()
