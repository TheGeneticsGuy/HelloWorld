## Basic Hello World Program to more advance!

import webbrowser
import os

print("Hello World!")
print()

error_message = "Please try again. Enter 'yes' or 'no'."
error_table = ["yes", "no"]

# Let's take this to the next level!
def hello_world():
    while True:
        response = input("Do you want to go on a Hello World adventure? (yes/no): ").lower()
        if response in error_table:
            break
        print(error_message)

    if response == 'yes':

        name = get_name()

        while True:
            response = input(f"{name}, would you like to visit Hello World on the web? (yes/no): ").lower()
            if response in error_table:
                break
            print(error_message)

        if response == 'yes':
            print(f'It\'s been nice knowing you {name}. Send you off to the Cosmos of the web. Goodbye!')

        else:
            print(f'That\'s ok, {name}, you\'re the boss!')
            print()



    else:
        print("Keeping it classic. I like it! Until next time!")

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
def build_webpage():
    html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello World Galaxy</title>
            <style>
                body {
                    background: #0a0a23;
                    color: #ffffff;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 50px;
                }
                h1 {
                    font-size: 48px;
                    animation: glow 2s ease-in-out infinite alternate;
                }
                @keyframes glow {
                    from { text-shadow: 0 0 10px #fff, 0 0 20px #00f, 0 0 30px #0ff; }
                    to { text-shadow: 0 0 20px #fff, 0 0 30px #00f, 0 0 40px #0ff; }
                }
            </style>
        </head>
        <body>
            <h1>Hello World from the Cosmos!</h1>
            <p>Welcome to the Galaxy of Greetings!</p>
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
    for _ in range ( 1 ):
        time.sleep(0.1)

# Start the program
hello_world()