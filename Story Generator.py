import random

# Lists of story elements
characters = ["a brave knight", "a clever wizard", "a mischievous elf", "a fearsome dragon"]
settings = ["in a dark forest", "in an ancient castle", "in a bustling town", "on a remote island"]
actions = ["fought against", "teamed up with", "tricked", "escaped from"]
objects = ["a magical artifact", "a hidden treasure", "a dangerous curse", "a powerful spellbook"]

# Function to generate a random story
def generate_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    action = random.choice(actions)
    obj = random.choice(objects)

    story = f"One day, {character} {setting}, they {action} {obj}."
    return story

# Generate and print a random story
print(generate_story())
