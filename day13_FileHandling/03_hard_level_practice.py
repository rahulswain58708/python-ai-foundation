# Q11. Count Words in a File
# Question
# Write a Python program that:
# Opens the file intro.txt
# Counts the total number of words in the file
# Prints the total word count
# 📌 Conditions
# Use read mode
# Do not use file pointer (seek, tell)
# Use basic string methods
with open("intro.txt","r") as file:
    lines = file.read()
    words = lines.split()
    total_word = len(words)
    print(f"total words = {total_word}")
# Q12. Search Word in a File
# Question
# Write a Python program that:
# Opens the file intro.txt
# Takes a word from the user
# Checks whether that word exists in the file or not
# Prints:
# "Word Found" → if the word exists
# "Word Not Found" → if the word does not exist
with open("intro.txt","r") as file:
    word = input("Enter a Word:- ")
    lines = file.read()
    words = lines.split()
    if word in words:
        print("Word Found")
    else:
        print("Word Not Found")