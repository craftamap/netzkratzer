""" This file is a simple demonstration of various options of the  requests library. It also shows basic functionality
for the furl library
"""

import requests
import furl


def get_one():
    """This function does a simple get request and prints the result, once in
    utf-8, once in bytes"""
    response = requests.get("https://httpbin.org/get")
    print(response.text)
    print(response.content)


def get_two():
    """This function does a get request with query parameters"""
    response = requests.get("https://httpbin.org/get?foo=bar&hello=world")
    print(response.json()["args"])


def get_three():
    """This function does a get request with query parameters,but using the
    furl library to build the url"""
    url = furl.furl("http://httpbin.org")
    url.schema = "https"
    url: furl = url / "set" / "to" / "something"
    print(url.path.segments)

    url.set(path="get")
    url.set(
        args={
            "foo": "bar",
            "hello": "world",
        }
    )


def post_one():
    response = requests.post(
        "https://httpbin.org/post",
        {
            "foo": "bar",
            "hello": "world",
        },
    )
    print(response.json())


def post_two():
    response = requests.post(
        "https://httpbin.org/post",
        json={
            "foo": "bar",
            "hello": "world",
        },
    )
    print(response.json())


def auth():
    response = requests.get("https://httpbin.org/basic-auth/admin/admin", auth=("admin", "admin"))
    print(response.status_code)
    response = requests.get("https://httpbin.org/basic-auth/admin/admin", auth=("admin", "invalidpassword"))
    print(response.status_code)


def headers():
    response = requests.get(
        "https://httpbin.org/headers",
        headers={
            "X-HACKERSPACE": "OLA",
        },
    )
    print(response.json())


def main():
    print("GET ONE")
    get_one()
    print("GET TWO")
    get_two()
    print("GET THREE")
    get_three()
    print("POST ONE")
    post_one()
    print("POST TWO")
    post_two()
    print("AUTH")
    auth()
    print("HEADERS")
    headers()


if __name__ == "__main__":
    main()
