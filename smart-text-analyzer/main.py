#SmartTextAnalyzer
print("-----------------SmartTextAnalyzer------------------")
# Take input string
text = input("Enter a text:-").lower()
# Text cleaning
clean_text = " ".join(text.split())
while True:
    if text == "":
        print("Please Provide text❌")
        break
    # Ask user  what do you want
    print("What do you want?")
    print("1.Total words")
    print("2.Total character")
    print("3.Vowels count")
    print("4.Longest word")
    print("5.Check specific word exist in text")
    print("6.Remove duplicate character")
    print("7.View text")
    print("8.Exit")
    choice = input("Enter your choice:")
    #Total Words count
    if choice == "1":
        words = clean_text.split()
        total_words = len(words)
        print(f"Total Words = {total_words}")
    #Total character count
    elif choice == "2":
        remove_space = clean_text.replace(" ","")
        total_char = len(remove_space)
        print(f"Total Character = {total_char}")
    #Vowels count
    elif choice == "3":
        remove_space = clean_text.replace(" ","")
        vowels = "aeiou"
        count_vowels = 0
        for char in remove_space:
            if char.isalpha():
                if char in vowels:
                    count_vowels += 1
        print(f"Vowels = {count_vowels}")
    #Longest word
    elif choice == "4":
        words = clean_text.split()
        longest_word = words[0]
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
        print(f"Longest Word:- {longest_word}")
    #specific word exist in text
    elif choice == "5":
        word = input("Enter a word check (exist or not):").lower()
        if word in clean_text.split():
            print(f"{word} is exist.")
        else:
            print(f"{word} is not exist")
    #remove duplicate character
    elif choice == "6":
        result = ""
        for char in clean_text:
            if char not in result:
                result += char
        print(f"After Duplicate Remove:- {result}")
    #view
    elif choice == "7":
        print(f"Text:- {clean_text}")
    elif choice == "8":
        print("Thanks for using good bye👍🤗.")
        break
    else:
        print("Invalid Choice❌")