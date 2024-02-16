import tkinter as tk
from tkinter import filedialog


def load_deck_and_find_matches():
    # Load banlist
    with open('banlist.txt', 'r') as f:
        banlist = f.read().splitlines()

    # Load deck file
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as f:
            deck = f.read().splitlines()
            deck = [e[2:] for e in deck]

        # Find matches between banlist and deck
        matches = set(banlist) & set(deck)
        if matches:
            matches = '\n'.join(matches)
        else:
            matches = 'No banned cards found!'
        display_matches(matches)


def display_matches(matches):
    matches_text.delete(1.0, tk.END)
    matches_text.insert(tk.END, matches)


# Create main window
root = tk.Tk()
root.title("Deck Checker")

# Create button to load deck and find matches
load_button = tk.Button(root, text="Load deck and find banned cards", command=load_deck_and_find_matches)
load_button.pack()

# Create text widget to display matches
matches_text = tk.Text(root, wrap="word")
matches_text.pack(expand=True, fill="both")

root.mainloop()
