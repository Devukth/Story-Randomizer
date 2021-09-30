import random

print("Story Randomizer")
startup = ["Once upon a time, ", "Yesterday, ", "In the medieval ages, ", "Few days ago, ", "In the future, "]
character = ["a king", "a talking frog", "a robot"]
name = ["John", "Fred", "Frank", "Sarah", "Jacob"]
place = ["a kingdom", "a factory", "a pond", "a city"]
went = ["a river", "the sea", "the sky", "the ground"]
aftermath = ["floated away but they came back.", "sunk down", "shut down the factory."]
print (
    random.choice(startup)
    + "there was "
    + random.choice(character)
    + " whose name was "
    + random.choice(name)
    + " who lived in "
    + random.choice(place)
    + "."
    + " They went into "
    + random.choice(went)
    + " and then they "
    + random.choice(aftermath)
)