import random
import time

easy_mode = [
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

def get_random_words(mode):
    random_number = random.randint(0, 6)
    if mode == "easy":
        return easy_mode[random_number]
    elif mode == "medium":
        return medium_mode[random_number]
    elif mode == "hard":
        return hard_mode[random_number]
    else:
        return "Invalid difficulty level"

def words_per_minute(text, elapsed_time):
    word_count = len(text.split())
    wpm = (word_count / elapsed_time) * 60
    return wpm

def word_accuracy(random_words, input_text):
    random_words_list = random_words.split()
    input_words = input_text.split()
    min_len = min(len(random_words_list), len(input_words))
    correct_count = sum(1 for r, i in zip(random_words_list[:min_len], input_words[:min_len]) if r == i)
    accuracy = (correct_count / len(random_words_list)) * 100
    return accuracy

def typing_speed_test(mode):
    random_words = get_random_words(mode)
    print("Type the following:", random_words)
    
    start_time = time.time()
    user_input = input("Your typing: ")
    ending_time = time.time()
    
    elapsed_time = ending_time - start_time
    wpm = words_per_minute(user_input, elapsed_time)
    accuracy = word_accuracy(random_words, user_input)
    
    print(f"Words per minute: {wpm:.2f}\nWord accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    difficulty_level = input("Select difficulty (easy, medium, or hard): ")
    typing_speed_test(difficulty_level)
