import requests

try:
    response = requests.get("https://catfact.ninja/fact")

    # Check for an error
    response.raise_for_status()

    data = response.json()
    print(data['fact'])
except requests.exceptions.RequestException:
    print("There was a problem contacting the API.")
