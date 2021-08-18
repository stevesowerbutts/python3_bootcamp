import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice


ascii_art = figlet_format("DAD JOKES 3000")
print(colored(ascii_art, color="red"))

url = "http://www.icanhazdadjoke.com/search"

def dad_joke(topic):
    response = requests.get(url,
                headers={"Accept": "application/json"},
                params={"term":topic})
    data = response.json()
    results = data["results"]
    total_jokes = data["total_jokes"]
    if total_jokes == 0:
        print(f"Sorry, I dont have any jokes about {topic}! Please try again.")
    else:
        print(f"I've got {total_jokes} jokes about {topic}. Here is one: ")
        print(choice(results)["joke"])

topic = input("Let me tell you a joke! Give me a topic: ")
dad_joke(topic)
