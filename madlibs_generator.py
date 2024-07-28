with open("mad_libs_story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1  # says start of word is -1

target_start, target_end = "<", ">"

for i, char in enumerate(story):  # enumerate give access to position(index) and element at position
    if char == target_start:  # if character in element is target_start, mark by indicating in variable,
        start_of_word = i  # mark by indicating in variable

    if char == target_end and start_of_word != -1:  # ending bracket found and starting bracket found
        word = story[start_of_word: i + 1]  # slice operator
        words.add(word)  # appending to set variable words
        start_of_word = -1  # resetting counter

# print(words)

answers = {}

for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word]) # generate new lines of string, must have a variable to it

print(story)
