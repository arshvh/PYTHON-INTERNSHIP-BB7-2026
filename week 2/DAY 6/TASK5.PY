file = open("my_story.txt", "r")

content = file.read()

words = content.split()

total_words = len(words)

file.close()

print("Total number of words:", total_words)