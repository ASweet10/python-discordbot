from random import choice, randint

quotes = [
    "The only thing we have to fear is fear itself",
    "All that is gold does not glitter, not all those who wander are lost",
    "Success consists of going from failure to failure without loss of enthusiasm",
    "Be yourself; everyone else is already taken.",
    "In three words I can sum up everything I've learned about life: it goes on.",
    "To live is the rarest thing in the world. Most people exist, that is all."
]

facts = [
    "Butterflies can taste with their feet.",
    "The moon's gravity is only one-sixth of Earth's gravity.",
    "One million Earths could fit inside the sun.",
    "Neptune's moon Triton is the coldest known object in our solar system, with an average surface temperature of -391° F.",
    "Pizza was invented in Naples, Italy, and was originally a working-class dish.",
    "Italy is home to all three active volcanoes in Europe: Mount Etna, Stromboli, and Mount Vesuvius.",
    "Italians do not consider pineapple to be an acceptable pizza topping."
]

helpOptions = [
    "help/options: see options",
    "!quote: random quote",
    "+quote (quote to add): add new quote",
    "roll (number): Roll (number)-sided die",
    "!fact: random fact",
]

def get_response(user_input):
    lowered = user_input.lower()

    if lowered == '':
        return "Can't be empty!"
    elif 'help' in lowered:
        return "\n".join(helpOptions)
    elif 'hello' in lowered:
        return "Hello"
    elif 'roll' in lowered:
        handleDiceRoll(lowered)
    elif lowered == '!quote':
        return choice(quotes)
    elif lowered == '!fact':
        return choice(facts)
    elif lowered[0:6] == '+quote': # If first 6 characters = +quote
        handleAddNewQuote(lowered)

def handleDiceRoll(roll):
    dieSides = roll[5:]
    if isinstance(dieSides, int):
        return "You rolled a " + randint(1, dieSides)
    else:
        return "Please use this format: roll (number of die sides) ex: roll 6"

def handleAddNewQuote(quoteToAdd):
    newQuote = quoteToAdd[7:] # All text after +quote(space)
    if newQuote != '':
        quotes.append(newQuote)
        return "Quote added!"
    else:
        return "Quote can't be empty!"
