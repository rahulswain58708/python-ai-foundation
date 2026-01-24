#Q15.Take a string and print each word on a new line.
s = input("Enter a string:")
words = s.split()
for word in words:
    print(word)
# #Q16.Take a sentence and print how many words it has.
sentence = input("Enter a sentence:")
words = sentence.split()
count = 0
for word in words:
    count +=1
print(count)
#Q17.Take a string and find the largest word.
s2 = input("Enter a string:") #Hii iam Rahul
words = s2.split() #sentence break word
max_word = words[0] #assume max word = Hii
for word in words:
    if len(word) > len(max_word):
        max_word = word
print(f"Max_Word = {max_word}") #output:- Rahul
#Q18.Take a string and remove duplicate characters, while keeping the original order.
s3 = input("Enter a string:")
result = ""
for char in s3:
    if char not in result:
        result += char
print(result)
