print("--------------- Welcome to Mood2Emoji ----------------")
print("Choose your mood:")
print("good, bad, sad, angry, focus, normal, happy, romantic")
print("------------------------------------------------------")

mood = input("Enter your mood: ").lower()

if mood == "good":
    print("😉 ☺️ 😎")
elif mood == "bad":
    print("🤕 🙅🏻‍♀️ 👎🏻")
elif mood == "sad":
    print("😔 😓 😞")
elif mood == "angry":
    print("😡 😤 🤬")
elif mood == "focus":
    print("👩🏻‍💻 📚")
elif mood == "normal":
    print("🙂 😐 🤗")
elif mood == "happy":
    print("😁 😀 😝")
elif mood == "romantic":
    print("😘 😍 🥰")
else:
    print("Invalid mood ❌ Please try again.")
