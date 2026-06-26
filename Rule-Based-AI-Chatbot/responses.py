def get_response(user):

    if user in ["hello", "hi", "hey"]:
        return "Hello! Welcome."

    elif user == "how are you":
        return "I'm fine. Thank you!"

    elif user == "what is your name":
        return "I am a Rule-Based AI Chatbot."

    elif user == "who created you":
        return "I was created using Python."

    elif user == "what is ai":
        return "Artificial Intelligence enables machines to imitate human intelligence."

    elif user == "machine learning":
        return "Machine Learning is a branch of Artificial Intelligence."

    elif user == "python":
        return "Python is an easy and powerful programming language."

    elif user == "what can you do":
        return "I can answer predefined questions."

    elif user == "help":
        return """
Available Commands

hello
hi
how are you
what is ai
machine learning
python
what is your name
who created you
what can you do
exit
"""

    elif user == "bye":
        return "Goodbye! Have a wonderful day."

    else:
        return "Sorry, I don't understand that."
