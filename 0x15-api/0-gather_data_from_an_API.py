#!/usr/bin/python3
"""for a given employee ID, returns information about his/her TODO list"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    dos = requests.get(url + "dos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in dos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(dos)))
    [print("\t {}".format(c)) for c in completed]
