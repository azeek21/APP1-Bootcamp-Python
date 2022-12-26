import requests
import json


if __name__ == "__main__":

    endpoints = [
        "http://127.0.0.1:8888/?species=Time%20Lord",
        "http://127.0.0.1:8888/?species=Nothing",
        "http://127.0.0.1:8888/?species=Slitheen",
        "http://127.0.0.1:8888/?specie",
        "http://127.0.0.1:8888/?species=Human"
    ]

    parse = lambda x: requests.get(x).json()

    for endpoint in endpoints:
        print(parse(endpoint))
