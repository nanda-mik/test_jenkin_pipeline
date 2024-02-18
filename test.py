import requests

def func():
    url_map = {
        "TEST_API": "https://reqres.in/api/users?page=2"
    }

    token = "Au token"

    url = url_map.get("TEST_API")
    res = requests.request(
        "GET",
        url,
        headers={
            "Authorization": token
        }
    )

    response = res.json()
    print(response.get('data'))

func()
