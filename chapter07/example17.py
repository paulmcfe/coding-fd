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
        url = "https://catfact.ninja/fact"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data['fact']
        except:
            return "Sorry, couldn't fetch a fact right now."

    # Display the retrieved fact
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
