# Q14. Delete File Safely
# Question
# Write a Python program that:
# Deletes the file backup.txt
# Deletes it only if the file exists
# Prints:
# "File Deleted" → if deletion is successful
# "File Not Found" → if the file does not exist
# 📌 Conditions
# Use the os module
# Do not throw an error if file is missing
# Check existence before deleting
import os
if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("File Deleted")
else:
    print("File Not Found")