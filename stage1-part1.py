""" In this file, we use the https://jsonplaceholder.typicode.com json
placeholder to show the basic capability of the requests library of getting a
resource via get
"""

import requests
import typing


def get_all_users() -> typing.List[typing.Any]:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if not response.ok:
        raise Exception(response.status_code)

    users = response.json()

    if not isinstance(users, list):
        raise Exception("users is not instance of list")

    return users


def main():
    users = get_all_users()
    for x in users:
        print(x.get("name"))


if __name__ == "__main__":
    main()