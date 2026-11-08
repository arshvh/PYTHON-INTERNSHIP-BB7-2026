file = open("my_story.txt", "r")

for line in file:
    print(line.strip(), "-", len(line.strip()), "characters")

file.close()