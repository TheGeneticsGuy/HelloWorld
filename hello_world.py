## Basic Hello World Program to more advance!

import webbrowser
import os
import sys
import time

print()
print("Hello World!")
print()

error_message = "Please try again. Enter 'y' for yes or 'n` for no."
error_table = ["y", "n"]

# Variables
name = ""

# Let's take this to the next level!
def hello_world( repeat_adventure ):
    global name

    while True:
        response = ""
        if not repeat_adventure:
            response = input("Do you want to go on a Hello World adventure? (y/n): ").lower()
        else:
            response = input(f"Great work, {name}, do you want to go on ANOTHER Hello World adventure? (y/n): ").lower()
        if response in error_table:
            break
        print(error_message)

    if response == 'y':
        print()
        print("Fantastic! This adventure is going to be led by you.\nPlease help choose your destination.")
        print()
        if name == "":
            name = get_name()
        print()

        while True:
            response = input(f"{name}, would you like to visit Hello World on the web? (y/n): ").lower()
            if response in error_table:
                break
            print(error_message)

        # Webpage Response!
        if response == 'y':
            print()
            print(f'It\'s been nice knowing you {name}. Send you off to the Cosmos of the web.')
            build_webpage(name)
            print()
            hello_world( True ) # Start Over!

        else:
            # Thinking animation that leads to 2 responses
            print()
            print(f'That\'s ok, {name}, you\'re the boss!')
            print()
            thinking_animatioin()


    else:
        print("Keeping it classic. I like it! Until next time!")

    print() # Just an added end of program spacing

# Method:           get_name()
# What it Does:     For flavor, allows the user to input their name and returns a validated name
# Purpose:          Just to make this Hello World a little more interesting than normal.
def get_name():
    while True:
        name = input("Before we continue, please state your first name: ").strip().capitalize()     # Removing white space, and ensuring proper noun is capitalized

        if not name:
            print("Error: Please enter a valid name.")
            continue

        # Normal names, or a name with a hyphen or apsotraphe, like Mary-Jane or something like that is only input acceptable.
        if all(char.isalpha() or char in " -'" for char in name):
            return name
        else:
            print(f"Error: {name} is not a valid format. Please only include normal characters and try again.")


# Method:           build_webpage()
# What it Does:     Builds a webpage in HTML, stylized, for fun, so you can nav to it
# Purpose:          Take the Hello World concept to the next level!
def build_webpage( name=""):

    # In case for some reason name got lost in use of function
    # Shouldn't happen, but good practice I think.
    if name == "":
        name = 'friend'

    html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello World Galaxy</title>
            <style>
                body {{
                    background: #0a0a23;
                    color: #ffffff;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 50px;
                }}
                h1 {{
                    font-size: 48px;
                    animation: glow 2s ease-in-out infinite alternate;
                }}
                @keyframes glow {{
                    from {{ text-shadow: 0 0 10px #fff, 0 0 20px #00f, 0 0 30px #0ff; }}
                    to {{ text-shadow: 0 0 20px #fff, 0 0 30px #00f, 0 0 40px #0ff; }}
                }}
            </style>
        </head>
        <body>
            <h1>Hello World from the Cosmos!</h1>
            <p>Welcome, {name}!</p>
        </body>
        </html>
    """

    # Ok, to open the HTML content on a web browser, we have to write to a file.
    with open("hello_world.html", "w") as f:
        f.write(html_content)

    # Now, we open it.
    webbrowser.open("file://" + os.path.realpath("hello_world.html"))
    print("Launching the Hello World webpage!")

def thinking_animatioin():
    print('Thinking of what to do next' , end='' , flush=True) # Essentially we are printing a message, but not going to a new line.
    for _ in range ( 10 ):
        time.sleep(0.25)
        print(".", end="", flush=True) # Again, not moving to the next line yet.add()
    print("hmmm", end='' , flush=True)
    for _ in range ( 8 ):
        time.sleep(0.25)
        print(".", end="", flush=True) # Again, not moving to the next line yet.add()
    print("I got it!!!")
    time.sleep(1)
    print()

# Start the program
hello_world( False )