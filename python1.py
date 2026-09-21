# Mad Libs Generator
# Phase 1 - Basic Version

print("===================================")
print("       MAD LIBS STORY GENERATOR")
print("===================================")

print("\nEnter the following words to create your story:\n")

# Taking input from the user
name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")
place = input("Enter a place: ")

# Creating the story
story = f"""
Once upon a time, there was a person named {name}.

{name} was a very {adjective} person who loved their {noun}.
One day, {name} decided to {verb} {adverb}.

While doing this, {name} suddenly reached a strange place called
{place}.

Everyone there was surprised to see {name}.
After a lot of fun and adventure, {name} returned home happily.

And that was the most memorable day of {name}'s life!
"""

# Displaying the generated story
print("\n===================================")
print("          YOUR MAD LIBS STORY")
print("===================================")

print(story)

print("===================================")
print("       THANK YOU FOR PLAYING!")
print("===================================")