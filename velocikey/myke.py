#mag import ka
import random
import time
#difficulty at yung words nila mismo
asy_mode = [
    "I am happy.",
    "The sun is bright.",
    "It is a cat.",
    "She is nice.",
    "He can run fast.",
    "The sky is blue.",
    "They play games."
]

medium_mode = [
    "The quick brown fox jumps over the lazy dog.",
    "A beautiful sunset painted the sky with vivid colors.",
    "In the heart of the city, people hurriedly go about their day.",
    "She enjoys playing the piano and composing her own music.",
    "The conference room was filled with professionals from diverse backgrounds.",
    "Navigating through a bustling market can be a challenging task.",
    "The ancient castle stands atop the hill, overlooking the village."
]

hard_mode = [
    "The intricacies of quantum mechanics continue to baffle scientists.",
    "Navigating through a labyrinthine network of code is a developer's challenge.",
    "Amidst the cacophony of a crowded city, finding inner peace is a quest.",
    "The symphony's crescendo echoed through the concert hall, leaving the audience in awe.",
    "Solving complex mathematical proofs requires precision and dedication.",
    "Mastering a foreign language involves grasping its nuances and idiomatic expressions.",
    "In the depths of the ocean, unknown species await discovery by intrepid explorers."
]

#(def)difficulty select
def get_random_words (mode) :
    random_number = random.randint(0,6)
    if mode == "easy":
        return easy_mode [random_number]
    elif mode == "medium":
        return medium_mode [random_number]
    elif mode == "hard":
        return hard_mode [random_number]
    else:
        return "Invalid difficulty"

#(def)words per minute
def words_per_minute (text, elapsed_time) :
    word_count = len(text.split())
    wpm = (word_count / elapsed_time) * 60
    return wpm
#(def)word accuracy

#(def)magtytype ka ng words

#start program
