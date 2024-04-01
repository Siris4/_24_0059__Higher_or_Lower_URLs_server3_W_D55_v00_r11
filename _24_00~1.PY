
from flask import Flask
import random

# Get user input
# user_chosen_number = int(input("Choose a number between 0 and 9: "))
# print(f"You chose {user_chosen_number}.")

number_randomly_chosen = random.randint(0, 9)
# TODO: Toggle this on or off, depending on if you want to see the hint:
# print(f"The random number generated is: {number_randomly_chosen}\n")

app = Flask(__name__)
n = ""

# template: @app.route("/username/<name>/<int:number>")
# try: @app.route(f"/<int:{user_chosen_number}>")
@app.route("/<int:n>")
def hello_world(n):     #removed: now from return statement
    if n == number_randomly_chosen:
        return f"""<h1 style="color: blue;">Congratulations!!! You guessed the number correctly!!!</h1>  
            <img src='https://media.giphy.com/media/s2qXK8wAvkHTO/giphy.gif?cid=790b76119tee2ufyi7hejsqj376rv2egrhk24dpkibobvw4e&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=800>"""
    elif n > number_randomly_chosen:
        return f"""<h1 style="color: green;">Sorry, you guessed a number that is too high</h1>  
                    <img src='https://media4.giphy.com/media/3orieYSIw6FQMsmFQQ/200.webp?cid=ecf05e475nc1axp3injdyo0q7m9s6rqimymj0hdo0isf9q4k&ep=v1_gifs_search&rid=200.webp&ct=g' width=800>"""
    elif n < number_randomly_chosen:
        return f"""<h1 style="color: red;">Womp, you guessed a number that is too low</h1>  
                    <img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGpvN2VtaHU3YjdkOTN0YW53MmhpcmNha3llc3h4eW1xZmNhZzQ1ciZlcD12MV9naWZzX3NlYXJjaCZjdD1n/aztdjHO5QbjLa/200.webp' width=800>"""


    else:
        print("Sorry, your guess is incorrect.")

    return f"""<h1>On server page: Guess a number between 0 and 9 </h1>  
    <img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW9xc3NoM2NjN3hxMzAzd20wd29pc3BtNzc1cmN6dDJtZGxjNTQxayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PK1YQhAoBOpP2/200.webp' width=400>"""



# remove below if unneeded:
if __name__ == "__main__":
    app.run(debug=True)   # can toggle this: True or False, depending on your needs

