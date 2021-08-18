# https://quotes.toscrape.com/
# Grab quotes, name of the person and href to persons bio
# Display a random quote to user and ask who said it. 4 guesses
# After incorrect guess, decrement number of guesses, player gets a hint about the author
# first hint make a request ot the authors bio for DOB and location
# 2nd hint - first letter first name
# 3rd hint - first letter second name
# player loses if run out of guesses, wins if guesses correct name
# Ask if they want to play again, if yes then restart.

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
import sys

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.select(".quote")

while soup.find(class_="next"):
    page = soup.find(class_="next").find("a")["href"]
    response = requests.get(url+page)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes += soup.select(".quote")


def display_hint(guess_count, author, bio_link):
    if guess_count == 0:
        print(f"Sorry, you have run out of guesses. The answer was {author}")
        play_again()
    elif guess_count == 3:
        bio_response = requests.get(url+bio_link)
        bio_soup = BeautifulSoup(bio_response.text, "html.parser")
        dob = bio_soup.find(class_="author-born-date").get_text()
        location = bio_soup.find(class_="author-born-location").get_text()
        print(f"The author was born in {dob}, {location}.")
    elif guess_count == 2:
        first_initial = author.split()[0][0]
        print(f"Here's a hint: The authors first name starts with {first_initial}")
    elif guess_count == 1:
        last_initial = author.split()[-1][0]
        print(f"Here's a hint: The authors last name starts with {last_initial}")

def play_again():
    play_again = input("\nWould you like to play again (y/n)? ")
    if play_again == "y":
        print("Great! Here we go again...\n")
        return quote_game()
    else:
        print("Thanks for playing.")
        sys.exit()



def quote_game():
    quote = choice(quotes)
    text = quote.find(class_="text").get_text()
    author = quote.find(class_="author").get_text()
    bio_link = quote.find("a")["href"]
    guess_count = 4
    print("Here's a quote:\n")
    print(text)
    print(author)
    while guess_count > 0:
        answer = input(f"\nWho said this? Guesses remaining: {guess_count}. ")
        if answer.lower() == author.lower():
            print("You guessed correctly")
            return play_again()
        else:
            guess_count -= 1
            display_hint(guess_count, author, bio_link)

quote_game()
