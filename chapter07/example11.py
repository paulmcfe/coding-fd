import requests

# Get a random joke
response = requests.get("https://official-joke-api.appspot.com/random_joke")

# Check the status code
if response.status_code == 200:

    # Convert the JSON to a dictionary
    joke = response.json()

    print("Here's a joke for you:")

    # Print the joke setup
    print(joke['setup'])

    # Wait for the user to press Enter
    input("...")

    # Print the joke punchline
    print(joke['punchline'])
else:
    print("Something went wrong. This is not a joke.")
