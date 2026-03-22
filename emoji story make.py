import tkinter as tk
from tkinter import messagebox, filedialog
import random

# Dictionary of words → list of possible emojis
emoji_dict = {
    "happy": ["😄", "😊", "😁"],
    "sad": ["😢", "😭", "😔"],
    "love": ["❤️", "😍", "💖"],
    "heart": ["❤️", "💓", "💗"],
    "cat": ["🐱", "😺", "🐈"],
    "dog": ["🐶", "🐕", "🐾"],
    "food": ["🍔", "🍕", "🍟", "🍝"],
    "pizza": ["🍕", "🍕🍕"],
    "party": ["🎉", "🥳", "🎊"],
    "birthday": ["🎂", "🎉", "🎁"],
    "sun": ["☀️", "🌞"],
    "moon": ["🌙", "🌚"],
    "star": ["⭐", "🌟"],
    "sleep": ["😴", "💤"],
    "laugh": ["😂", "🤣", "😆"],
    "cry": ["😭", "😢"],
    "music": ["🎵", "🎶", "🎧"],
    "dance": ["💃", "🕺", "🎶"],
    "coffee": ["☕", "🥤"],
    "rain": ["🌧️", "🌦️", "☔"],
    "fire": ["🔥", "💥"],
    "book": ["📚", "📖"],
    "car": ["🚗", "🚘", "🏎️"],
}

# Function to generate emoji story
def generate_emoji_story():
    user_text = text_entry.get("1.0", tk.END).strip().lower()
    if not user_text:
        messagebox.showwarning("Warning", "Please enter a story first!")
        return

    words = user_text.split()
    emoji_story = []

    for word in words:
        if word in emoji_dict:
            emoji_story.append(random.choice(emoji_dict[word]))
        else:
            emoji_story.append(word)

    story = " ".join(emoji_story)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, story)

# Function to save story as text file
def save_story():
    story = output_text.get("1.0", tk.END).strip()
    if not story:
        messagebox.showwarning("Warning", "No story to save!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
        title="Save Emoji Story"
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(story)
        messagebox.showinfo("Saved", f"Story saved successfully at:\n{file_path}")

# Tkinter GUI setup
root = tk.Tk()
root.title("Advanced Emoji Story Maker 😎")
root.geometry("650x500")

# Labels
tk.Label(root, text="Enter your story:", font=("Arial", 14)).pack(pady=10)

# Text entry
text_entry = tk.Text(root, height=6, font=("Arial", 12))
text_entry.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Generate Emoji Story", font=("Arial", 12), command=generate_emoji_story).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Save Story", font=("Arial", 12), command=save_story).grid(row=0, column=1, padx=10)

# Output area
tk.Label(root, text="Emoji Story:", font=("Arial", 14)).pack(pady=10)
output_text = tk.Text(root, height=8, font=("Arial", 12))
output_text.pack(pady=5)

root.mainloop()