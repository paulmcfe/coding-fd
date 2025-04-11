import requests

# Get a random joke
response = requests.get("https://official-joke-api.appspot.com/random_joke")

# Check the status code
if response.status_code == 200:
    print("I was able to connect to the API no problem.")
else:
    print("Something went wrong. This is not a joke.")
