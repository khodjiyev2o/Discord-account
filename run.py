from main.account_creator import Creator
import random
import string
from random_username.generate import generate_username
def random_char(char_num):
       return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))

username  = generate_username(1)
email = random_char(7)+"@gmail.com"

with Creator() as bot:
        bot.land_first_page()
        bot.registration(
                email=input("Enter your email:"),
                username=input("Enter your username:"),
        )

        bot.getting_token()
        #bot.login_with_token()        