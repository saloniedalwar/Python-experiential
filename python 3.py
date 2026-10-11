import random
import textwrap

# ==========================================
# MAD LIBS STORY GENERATOR
# Phase 1 + Phase 2 | Complete Project
# ==========================================

# Terminal colours
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"


# ---------- Display Functions ----------

def show_title():
    print("\n" + CYAN + "=" * 52 + RESET)
    print(BOLD + MAGENTA + "       MAD LIBS STORY GENERATOR" + RESET)
    print(CYAN + "          Create Your Own Adventure!" + RESET)
    print(CYAN + "=" * 52 + RESET)


def show_menu():
    print("\n" + YELLOW + "MAIN MENU" + RESET)
    print("1. Generate a Basic Story (Phase 1)")
    print("2. Generate a Random Story (Phase 2)")
    print("3. Choose Your Favourite Story")
    print("4. About This Project")
    print("5. Exit")


# ---------- Input Validation ----------

def get_input(prompt):
    while True:
        answer = input(prompt).strip()

        if answer:
            return answer

        print(RED + "Input cannot be empty. Please try again." + RESET)


def get_number():
    while True:
        answer = get_input("Enter a number: ")

        try:
            number = int(answer)

            if number > 0:
                return number

            print(RED + "Please enter a number greater than zero." + RESET)

        except ValueError:
            print(RED + "Invalid input! Please enter a whole number." + RESET)


# ---------- Collect User Words ----------

def get_words():
    print("\n" + CYAN + "-" * 52 + RESET)
    print(BOLD + "ENTER YOUR WORDS" + RESET)
    print("Use your imagination and make the story funny!")
    print(CYAN + "-" * 52 + RESET)

    words = {}

    words["name"] = get_input("Enter a name: ")
    words["adjective"] = get_input("Enter an adjective (e.g. funny): ")
    words["noun"] = get_input("Enter a noun (e.g. book): ")
    words["verb"] = get_input("Enter a verb (e.g. dance): ")
    words["adverb"] = get_input("Enter an adverb (e.g. quickly): ")
    words["place"] = get_input("Enter a place: ")
    words["animal"] = get_input("Enter an animal: ")
    words["food"] = get_input("Enter a food: ")
    words["emotion"] = get_input("Enter an emotion: ")
    words["number"] = get_number()

    return words


# ---------- Story Templates ----------

def basic_story(words):
    return (
        f"One {words['adjective']} day, {words['name']} went to "
        f"{words['place']} carrying a magical {words['noun']}.\n\n"
        f"Suddenly, a {words['animal']} appeared and started to "
        f"{words['verb']} {words['adverb']}!\n\n"
        f"{words['name']} felt {words['emotion']} and offered it "
        f"some {words['food']}.\n\n"
        f"After eating {words['number']} pieces, the {words['animal']} "
        f"became the most famous animal in {words['place']}!"
    )


def story_one(words):
    return (
        f"THE CRAZY SCHOOL DAY\n\n"
        f"One morning, {words['name']} arrived at school in a "
        f"{words['adjective']} mood.\n\n"
        f"The teacher brought a giant {words['noun']} into the classroom. "
        f"Suddenly, a {words['animal']} entered and began to "
        f"{words['verb']} {words['adverb']}!\n\n"
        f"Everyone felt {words['emotion']}. To solve the problem, "
        f"{words['name']} offered the animal some {words['food']}.\n\n"
        f"The animal was so happy that it invited everyone to "
        f"{words['place']} for {words['number']} days of celebration!"
    )


def story_two(words):
    return (
        f"THE MAGICAL ADVENTURE\n\n"
        f"{words['name']} discovered a {words['adjective']} "
        f"{words['noun']} near {words['place']}.\n\n"
        f"When {words['name']} touched it, a talking {words['animal']} "
        f"appeared and asked everyone to {words['verb']} "
        f"{words['adverb']}.\n\n"
        f"Although {words['name']} felt {words['emotion']}, "
        f"the animal shared some {words['food']}.\n\n"
        f"Together, they travelled through {words['place']} and found "
        f"{words['number']} hidden treasures!"
    )


def story_three(words):
    return (
        f"THE FUNNIEST RESTAURANT\n\n"
        f"{words['name']} opened a {words['adjective']} restaurant "
        f"in {words['place']}.\n\n"
        f"The restaurant's manager was a {words['animal']} that knew "
        f"how to {words['verb']} {words['adverb']}!\n\n"
        f"The special dish was {words['food']} served inside a giant "
        f"{words['noun']}.\n\n"
        f"At first, the customers felt {words['emotion']}, but they "
        f"ordered {words['number']} plates and loved every bite!"
    )


# ---------- Story Generation ----------

def generate_random_story(words):
    stories = [story_one, story_two, story_three]
    selected_story = random.choice(stories)

    print("\n" + MAGENTA + "A random story has been selected!" + RESET)
    return selected_story(words)


def choose_story(words):
    print("\nChoose a story:")
    print("1. The Crazy School Day")
    print("2. The Magical Adventure")
    print("3. The Funniest Restaurant")

    while True:
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            return story_one(words)
        elif choice == "2":
            return story_two(words)
        elif choice == "3":
            return story_three(words)
        else:
            print(RED + "Invalid choice. Please enter 1, 2, or 3." + RESET)


# ---------- Print Story ----------

def display_story(story):
    print("\n" + GREEN + "=" * 52 + RESET)
    print(BOLD + YELLOW + "             YOUR GENERATED STORY" + RESET)
    print(GREEN + "=" * 52 + RESET)

    print(textwrap.fill(story, width=65))

    print("\n" + GREEN + "=" * 52 + RESET)


# ---------- Project Information ----------

def about_project():
    print("\n" + CYAN + "ABOUT THIS PROJECT" + RESET)
    print("Project Name : Mad Libs Story Generator")
    print("Language     : Python")
    print("Phase 1      : Basic story generation")
    print("Phase 2      : Random stories and story selection")
    print("\nPython concepts used:")
    print("- Functions")
    print("- Dictionaries")
    print("- Conditional statements")
    print("- Loops")
    print("- User input and validation")
    print("- Random module")
    print("- String formatting")


# ---------- Main Program ----------

def main():
    show_title()

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            words = get_words()
            story = basic_story(words)
            display_story(story)

        elif choice == "2":
            words = get_words()
            story = generate_random_story(words)
            display_story(story)

        elif choice == "3":
            words = get_words()
            story = choose_story(words)
            display_story(story)

        elif choice == "4":
            about_project()

        elif choice == "5":
            print("\n" + MAGENTA +
                  "Thank you for using Mad Libs Story Generator!" +
                  RESET)
            print(GREEN + "Keep imagining. Keep creating!" + RESET)
            break

        else:
            print(RED + "Invalid choice! Please enter 1 to 5." + RESET)

        input("\nPress Enter to return to the main menu...")


# Start the program
if __name__ == "__main__":
    main()