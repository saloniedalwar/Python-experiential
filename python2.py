import random


# ==========================================
# MAD LIBS GENERATOR
# Phase 2 - 70% Project
# ==========================================


# Function to get non-empty input
def get_input(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value
        else:
            print("Please enter something!")


# Function to collect words from the user
def get_words():

    print("\nEnter the required words:\n")

    words = {}

    words["name"] = get_input("Enter a name: ")
    words["adjective"] = get_input("Enter an adjective: ")
    words["noun"] = get_input("Enter a noun: ")
    words["verb"] = get_input("Enter a verb: ")
    words["adverb"] = get_input("Enter an adverb: ")
    words["place"] = get_input("Enter a place: ")
    words["animal"] = get_input("Enter an animal: ")
    words["food"] = get_input("Enter a food: ")
    words["emotion"] = get_input("Enter an emotion: ")
    words["number"] = get_input("Enter a number: ")

    return words


# ==========================================
# STORY TEMPLATES
# ==========================================

def story_one(words):

    return f"""
Once upon a time, there was a person named {words["name"]}.

{words["name"]} was a very {words["adjective"]} person who
loved their {words["noun"]}.

One day, {words["name"]} decided to {words["verb"]}
{words["adverb"]}.

While travelling to {words["place"]}, {words["name"]}
suddenly saw a {words["animal"]}.

The {words["animal"]} was carrying {words["food"]}!

{words["name"]} felt very {words["emotion"]} and started
laughing.

After having {words["number"]} pieces of {words["food"]},
{words["name"]} finally returned home.

It was the funniest day ever!
"""


def story_two(words):

    return f"""
THE GREAT ADVENTURE

One morning, {words["name"]} woke up feeling very
{words["emotion"]}.

{words["name"]} packed a {words["noun"]} and started
to {words["verb"]} towards {words["place"]}.

On the way, a {words["adjective"]} {words["animal"]}
appeared.

The animal shouted, "Give me some {words["food"]}!"

{words["name"]} was surprised and ran {words["adverb"]}.

After running for {words["number"]} minutes, {words["name"]}
finally reached {words["place"]}.

It was an adventure that {words["name"]} would never forget!
"""


def story_three(words):

    return f"""
A VERY STRANGE DAY

Today, {words["name"]} decided to visit {words["place"]}.

There, {words["name"]} found a {words["adjective"]}
{words["animal"] sitting near a {words["noun"]}.

Suddenly, the animal started to {words["verb"]}
{words["adverb"]}.

Everyone became very {words["emotion"]}.

Then the animal asked for {words["number"]} pieces of
{words["food"]}.

Nobody knew what was happening!

Finally, {words["name"]} went home and decided that
this was the strangest day ever.
"""


# ==========================================
# DISPLAY MENU
# ==========================================

def show_menu():

    print("\n===================================")
    print("       MAD LIBS STORY GENERATOR")
    print("===================================")

    print("1. Generate a Random Story")
    print("2. Choose a Story")
    print("3. Exit")

    print("===================================")


# ==========================================
# GENERATE STORY
# ==========================================

def generate_random_story(words):

    stories = [
        story_one,
        story_two,
        story_three
    ]

    selected_story = random.choice(stories)

    return selected_story(words)


# ==========================================
# CHOOSE STORY
# ==========================================

def choose_story(words):

    print("\nSelect a Story:")
    print("1. The Funny Adventure")
    print("2. The Great Adventure")
    print("3. A Very Strange Day")

    while True:

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            return story_one(words)

        elif choice == "2":
            return story_two(words)

        elif choice == "3":
            return story_three(words)

        else:
            print("Invalid choice! Please enter 1, 2 or 3.")


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    while True:

        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            words = get_words()

            story = generate_random_story(words)

            print("\n===================================")
            print("          YOUR STORY")
            print("===================================")

            print(story)

        elif choice == "2":

            words = get_words()

            story = choose_story(words)

            print("\n===================================")
            print("          YOUR STORY")
            print("===================================")

            print(story)

        elif choice == "3":

            print("\nThank you for using Mad Libs Generator!")
            print("Goodbye!")
            break

        else:

            print("\nInvalid choice!")
            print("Please select 1, 2 or 3.")


# ==========================================
# START PROGRAM
# ==========================================

if __name__ == "__main__":
    main()