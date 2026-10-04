import tkinter as tk
from tkinter import scrolledtext


# ==========================================================
# KNOWLEDGE BASE
# ==========================================================

knowledge_base = {

    "hello":
        "Hello! How can I help you?",

    "hi":
        "Hi! Nice to meet you.",

    "hey":
        "Hey! How can I help you?",

    "what is ai":
        "AI stands for Artificial Intelligence. "
        "It enables computers to perform tasks that normally "
        "require human intelligence.",

    "what is artificial intelligence":
        "Artificial Intelligence is a technology that enables "
        "computers to perform tasks that normally require "
        "human intelligence.",

    "what is python":
        "Python is a popular programming language used for "
        "AI, web development, automation, and many other applications.",

    "what is machine learning":
        "Machine Learning is a branch of AI where computers "
        "learn patterns from data and make predictions.",

    "what is chatbot":
        "A chatbot is a computer program that communicates "
        "with users through text or voice.",

    "what is dbms":
        "DBMS stands for Database Management System. "
        "It is used to store, manage, and retrieve data.",

    "what is html":
        "HTML stands for HyperText Markup Language. "
        "It is used to create the structure of web pages.",

    "what is css":
        "CSS stands for Cascading Style Sheets. "
        "It is used to style web pages.",

    "what is sql":
        "SQL stands for Structured Query Language. "
        "It is used to communicate with databases.",

    "who are you":
        "I am a simple knowledge-based chatbot created using Python.",

    "what is your name":
        "My name is SmartBot.",

    "how are you":
        "I am fine! Thank you for asking.",

    "what can you do":
        "I can answer questions that are available in my knowledge base.",

    "thank you":
        "You're welcome!",

    "thanks":
        "You're welcome!",

    "bye":
        "Goodbye! Have a nice day!"
}


# ==========================================================
# GET CHATBOT ANSWER
# ==========================================================

def get_answer(user_input):

    # Convert input to lowercase
    user_input = user_input.lower().strip()

    # Check exact question
    if user_input in knowledge_base:
        return knowledge_base[user_input]

    # Check whether a known question exists
    # inside the user's sentence
    for question in knowledge_base:

        if question in user_input:
            return knowledge_base[question]

    # If question is not available
    return "Sorry, I don't know the answer to that question."


# ==========================================================
# SEND MESSAGE
# ==========================================================

def send_message():

    # Get text from input box
    user_input = entry.get().strip()

    # Do nothing if empty
    if user_input == "":
        return

    # Enable chat box
    chat_box.config(state=tk.NORMAL)

    # Display user's message
    chat_box.insert(
        tk.END,
        "You: " + user_input + "\n",
        "user"
    )

    # Get chatbot answer
    answer = get_answer(user_input)

    # Display chatbot answer
    chat_box.insert(
        tk.END,
        "SmartBot: " + answer + "\n\n",
        "bot"
    )

    # Disable chat box again
    chat_box.config(state=tk.DISABLED)

    # Clear input box
    entry.delete(0, tk.END)

    # Scroll to latest message
    chat_box.see(tk.END)


# ==========================================================
# ENTER KEY
# ==========================================================

def press_enter(event):

    send_message()


# ==========================================================
# CLEAR CHAT
# ==========================================================

def clear_chat():

    chat_box.config(state=tk.NORMAL)

    chat_box.delete("1.0", tk.END)

    chat_box.insert(
        tk.END,
        "SmartBot: Chat cleared. Hello again! How can I help you?\n\n",
        "bot"
    )

    chat_box.config(state=tk.DISABLED)


# ==========================================================
# MAIN WINDOW
# ==========================================================

root = tk.Tk()

root.title("SmartBot - AI Chatbot")

root.geometry("750x650")

root.configure(bg="#101820")

root.resizable(True, True)


# ==========================================================
# TITLE
# ==========================================================

title = tk.Label(
    root,
    text="SMARTBOT",
    font=("Arial", 28, "bold"),
    bg="#101820",
    fg="#00D9FF"
)

title.pack(pady=(20, 5))


# ==========================================================
# SUBTITLE
# ==========================================================

subtitle = tk.Label(
    root,
    text="Simple Knowledge-Based Chatbot",
    font=("Arial", 12),
    bg="#101820",
    fg="white"
)

subtitle.pack(pady=(0, 15))


# ==========================================================
# CHAT DISPLAY
# ==========================================================

chat_box = scrolledtext.ScrolledText(
    root,
    font=("Arial", 12),
    bg="#17232F",
    fg="white",
    insertbackground="white",
    wrap=tk.WORD
)

chat_box.pack(
    padx=20,
    pady=10,
    fill=tk.BOTH,
    expand=True
)


# Make chat box read-only
chat_box.config(state=tk.DISABLED)


# ==========================================================
# MESSAGE COLORS
# ==========================================================

chat_box.tag_config(
    "user",
    foreground="#00D9FF"
)

chat_box.tag_config(
    "bot",
    foreground="#00FF88"
)


# ==========================================================
# INPUT FRAME
# ==========================================================

input_frame = tk.Frame(
    root,
    bg="#101820"
)

input_frame.pack(
    fill=tk.X,
    padx=20,
    pady=15
)


# ==========================================================
# INPUT BOX
# ==========================================================

entry = tk.Entry(
    input_frame,
    font=("Arial", 14),
    bg="#17232F",
    fg="white",
    insertbackground="white"
)

entry.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    ipady=10
)


# ==========================================================
# SEND BUTTON
# ==========================================================

send_button = tk.Button(
    input_frame,
    text="SEND",
    font=("Arial", 12, "bold"),
    bg="#00D9FF",
    fg="black",
    command=send_message,
    cursor="hand2"
)

send_button.pack(
    side=tk.RIGHT,
    padx=(10, 0),
    ipadx=20,
    ipady=8
)


# ==========================================================
# CLEAR BUTTON
# ==========================================================

clear_button = tk.Button(
    root,
    text="CLEAR CHAT",
    font=("Arial", 10, "bold"),
    bg="#FF5555",
    fg="white",
    command=clear_chat,
    cursor="hand2"
)

clear_button.pack(
    pady=(0, 15)
)


# ==========================================================
# ENTER KEY SUPPORT
# ==========================================================

entry.bind(
    "<Return>",
    press_enter
)


# ==========================================================
# WELCOME MESSAGE
# ==========================================================

chat_box.config(state=tk.NORMAL)

chat_box.insert(
    tk.END,
    "SmartBot: Hello! 👋\n"
    "I am SmartBot, a simple knowledge-based chatbot.\n\n"
    "You can ask me things like:\n"
    "• What is AI?\n"
    "• What is Python?\n"
    "• What is DBMS?\n"
    "• What is HTML?\n"
    "• What is SQL?\n\n",
    "bot"
)

chat_box.config(state=tk.DISABLED)


# ==========================================================
# START PROGRAM
# ==========================================================

root.mainloop()
