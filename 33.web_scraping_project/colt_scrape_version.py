import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

base_url = "https://quotes.toscrape.com"

def scrape_quotes():
    all_quotes = []
    url = "/page/1/"
    while url:
        res = requests.get(f"{base_url}{url}")
        print(url)
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.select(".quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
            next_btn = soup.find(class_="next")
            url = next_btn.find("a")["href"] if next_btn else None
    return all_quotes

def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote:\n")
    print(quote["text"])
    print(quote["author"])
    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"\nWho said this? Guesses remaining: {remaining_guesses}. ")
        if guess.lower() == quote["author"].lower():
            print("You guessed correctly")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{base_url}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_location = soup.find(class_="author-born-location").get_text()
            print(f"The author was born in {birth_date}, {birth_location}.")
        elif remaining_guesses == 2:
            print(f"Here's a hint: The authors first name starts with {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote['author'].split()[-1][0]
            print(f"Here's a hint: The authors last name starts with {last_initial}")
        else:
            print(f"Sorry, you have run out of guesses. The answer was {quote['author']}")

    again = ''
    while again.lower() not in ('y','yes','n','no'):
        again = input("Would you like to play again (y/n)?")
    if again.lower() in ('y','yes'):
        return start_game(quotes)
    else:
        print("Ok, Goodbye!")

quotes = scrape_quotes()
start_game(quotes)
