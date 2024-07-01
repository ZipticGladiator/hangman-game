import random

#create a wordlist to randomly select from
wordlist = [
    "vanilla", "elderberry", "wolfberry", "yangmei", "blueberry", "tamarind",
    "jackfruit", "lime", "cherry", "kumquat", "voavanga", "mulberry", "apricot",
    "strawberry", "uva", "huckleberry", "watermelon", "quararibea", "cantaloupe",
    "ziziphus", "grape", "quince", "guava", "imbe", "mango"
]

#if user selects an alphabet that is in the selected word,
# return the letter in its correct position
#end the game when all letters are guessed, or when user has guesses len(word) + 2 chances