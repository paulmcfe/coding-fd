# Bring in requests for API calls
import requests

# Define the CatFactCard class
class CatFactCard:
    # Initializer
    def __init__(self, name):
        self.name = name
        self.fact = self.get_fact()

    # Get a random cat fact
    def get_fact(self):

        # Store the Cat Facts API URL
        url = "https://catfact.ninja/fact"

        # Try to get a fact from the API
        try:
            response = requests.get(url)

            # Check for an error
            response.raise_for_status()

            # If we're good, get the response
            data = response.json()

            # Send back the returned cat fact
            return data['fact']
        
        # Did an error occur?
        except:
            # If so, send back a message
            return "Sorry, couldn't fetch a fact right now."

    # Display the card's data
    def show(self):
        print(f"{self.name} says:")
        print(f"\"{self.fact}\"")
        print()

# Create some cat fact cards
cat1_card = CatFactCard("Whiskers")
cat2_card = CatFactCard("Peanuts")
cat3_card = CatFactCard("Slyvester")

# Display the cards
cat1_card.show()
cat2_card.show()
cat3_card.show()
