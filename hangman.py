import tkinter as tk
from tkinter import messagebox
import random

# -----------------------------
# WORD LIST
# -----------------------------
WORDS = [
    "python", "computer", "hangman", "developer",
    "programming", "keyboard", "internet",
    "science", "artificial", "intelligence",
    "database", "network", "software"
]

# -----------------------------
# GAME SETTINGS
# -----------------------------
MAX_CHANCES = 6

# -----------------------------
# MAIN WINDOW
# -----------------------------
root = tk.Tk()
root.title("🎮 Hangman Game")
root.geometry("950x650")
root.config(bg="#1e1e2f")
root.resizable(False, False)

# -----------------------------
# VARIABLES
# -----------------------------
score = 0
word = ""
guessed_letters = []
remaining_chances = MAX_CHANCES

# -----------------------------
# FUNCTIONS
# -----------------------------
def start_new_game():
    global word, guessed_letters, remaining_chances

    word = random.choice(WORDS).upper()
    guessed_letters = []
    remaining_chances = MAX_CHANCES

    update_display()
    draw_hangman()

    result_label.config(text="")
    guess_entry.delete(0, tk.END)


def update_display():
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    word_label.config(text=display_word)

    guessed_label.config(
        text="Guessed Letters: " + " ".join(guessed_letters)
    )

    chances_label.config(
        text=f"Remaining Chances: {remaining_chances}"
    )

    score_label.config(
        text=f"Score: {score}"
    )


def draw_hangman():
    canvas.delete("all")

    # Gallows
    canvas.create_line(50, 350, 250, 350, width=5, fill="white")
    canvas.create_line(100, 350, 100, 50, width=5, fill="white")
    canvas.create_line(100, 50, 220, 50, width=5, fill="white")
    canvas.create_line(220, 50, 220, 90, width=5, fill="white")

    mistakes = MAX_CHANCES - remaining_chances

    # Head
    if mistakes >= 1:
        canvas.create_oval(190, 90, 250, 150, width=4, outline="white")

    # Body
    if mistakes >= 2:
        canvas.create_line(220, 150, 220, 240, width=4, fill="white")

    # Left arm
    if mistakes >= 3:
        canvas.create_line(220, 180, 180, 210, width=4, fill="white")

    # Right arm
    if mistakes >= 4:
        canvas.create_line(220, 180, 260, 210, width=4, fill="white")

    # Left leg
    if mistakes >= 5:
        canvas.create_line(220, 240, 180, 290, width=4, fill="white")

    # Right leg
    if mistakes >= 6:
        canvas.create_line(220, 240, 260, 290, width=4, fill="white")


def guess_letter():
    global remaining_chances, score

    guess = guess_entry.get().upper()

    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning(
            "Invalid Input",
            "Please enter ONE alphabet letter."
        )
        return

    if guess in guessed_letters:
        messagebox.showinfo(
            "Already Guessed",
            "You already guessed that letter."
        )
        return

    guessed_letters.append(guess)

    if guess not in word:
        remaining_chances -= 1

    update_display()
    draw_hangman()

    guess_entry.delete(0, tk.END)

    # WIN CONDITION
    won = True
    for letter in word:
        if letter not in guessed_letters:
            won = False
            break

    if won:
        score += 10
        update_display()

        result_label.config(
            text="🎉 YOU WON!",
            fg="#00ff99"
        )

        messagebox.showinfo(
            "Victory!",
            f"You guessed the word: {word}"
        )

    # LOSE CONDITION
    elif remaining_chances == 0:
        result_label.config(
            text=f"💀 YOU LOST! Word was: {word}",
            fg="#ff4d4d"
        )

        messagebox.showerror(
            "Game Over",
            f"The correct word was: {word}"
        )


# -----------------------------
# TITLE
# -----------------------------
title_label = tk.Label(
    root,
    text="🎮 HANGMAN GAME",
    font=("Helvetica", 28, "bold"),
    bg="#1e1e2f",
    fg="#00e6e6"
)
title_label.pack(pady=15)

# -----------------------------
# MAIN FRAME
# -----------------------------
main_frame = tk.Frame(root, bg="#1e1e2f")
main_frame.pack(fill="both", expand=True)

# -----------------------------
# LEFT FRAME (Canvas)
# -----------------------------
left_frame = tk.Frame(main_frame, bg="#1e1e2f")
left_frame.pack(side="left", padx=30)

canvas = tk.Canvas(
    left_frame,
    width=320,
    height=400,
    bg="#2b2b40",
    highlightthickness=0
)
canvas.pack()

# -----------------------------
# RIGHT FRAME (Controls)
# -----------------------------
right_frame = tk.Frame(main_frame, bg="#1e1e2f")
right_frame.pack(side="right", padx=40)

word_label = tk.Label(
    right_frame,
    text="",
    font=("Consolas", 28, "bold"),
    bg="#1e1e2f",
    fg="white"
)
word_label.pack(pady=20)

guess_entry = tk.Entry(
    right_frame,
    font=("Helvetica", 22),
    width=5,
    justify="center",
    bg="#2b2b40",
    fg="white",
    insertbackground="white"
)
guess_entry.pack(pady=10)

guess_button = tk.Button(
    right_frame,
    text="Guess",
    font=("Helvetica", 16, "bold"),
    bg="#00b894",
    fg="white",
    activebackground="#00d2a0",
    width=12,
    relief="flat",
    command=guess_letter
)
guess_button.pack(pady=15)

guessed_label = tk.Label(
    right_frame,
    text="Guessed Letters:",
    font=("Helvetica", 14),
    bg="#1e1e2f",
    fg="#f5f5f5",
    wraplength=350,
    justify="left"
)
guessed_label.pack(pady=10)

chances_label = tk.Label(
    right_frame,
    text="Remaining Chances:",
    font=("Helvetica", 16, "bold"),
    bg="#1e1e2f",
    fg="#ffd166"
)
chances_label.pack(pady=10)

score_label = tk.Label(
    right_frame,
    text="Score: 0",
    font=("Helvetica", 18, "bold"),
    bg="#1e1e2f",
    fg="#00ffcc"
)
score_label.pack(pady=10)

result_label = tk.Label(
    right_frame,
    text="",
    font=("Helvetica", 20, "bold"),
    bg="#1e1e2f"
)
result_label.pack(pady=20)

# -----------------------------
# BOTTOM BUTTONS
# -----------------------------
bottom_frame = tk.Frame(root, bg="#1e1e2f")
bottom_frame.pack(pady=20)

new_game_button = tk.Button(
    bottom_frame,
    text="🔄 New Game",
    font=("Helvetica", 14, "bold"),
    bg="#0984e3",
    fg="white",
    width=14,
    relief="flat",
    command=start_new_game
)
new_game_button.grid(row=0, column=0, padx=15)

exit_button = tk.Button(
    bottom_frame,
    text="❌ Exit",
    font=("Helvetica", 14, "bold"),
    bg="#d63031",
    fg="white",
    width=14,
    relief="flat",
    command=root.destroy
)
exit_button.grid(row=0, column=1, padx=15)

# -----------------------------
# START GAME
# -----------------------------
start_new_game()

root.mainloop()