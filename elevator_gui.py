import tkinter as tk
from tkinter import messagebox

# Elevator settings
MAX_FLOOR = 10
MIN_FLOOR = 0

current_floor = 0
moving = False

# ----------------------------
# Function to move elevator
# ----------------------------
def move_elevator(destination):
    global current_floor, moving

    if moving:
        return

    try:
        destination = int(destination)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    if destination < MIN_FLOOR or destination > MAX_FLOOR:
        messagebox.showwarning(
            "Invalid Floor",
            f"Building has floors from {MIN_FLOOR} to {MAX_FLOOR}."
        )
        return

    moving = True
    status_label.config(text="Elevator moving...")

    animate_elevator(destination)


# ----------------------------
# Animation Function
# ----------------------------
def animate_elevator(destination):
    global current_floor, moving

    if current_floor == destination:
        status_label.config(
            text=f"Ding! Arrived at floor {destination}"
        )
        moving = False
        return

    if current_floor < destination:
        current_floor += 1
    else:
        current_floor -= 1

    floor_label.config(text=f"Current Floor: {current_floor}")

    # Repeat after 1 second
    root.after(1000, lambda: animate_elevator(destination))


# ----------------------------
# Button click function
# ----------------------------
def go_to_floor():
    destination = floor_entry.get()
    move_elevator(destination)


# ----------------------------
# GUI Window
# ----------------------------
root = tk.Tk()
root.title("Gemini Lift")
root.geometry("500x500")
root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="Gemini Lift",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=15)

# Current floor display
floor_label = tk.Label(
    root,
    text=f"Current Floor: {current_floor}",
    font=("Arial", 16)
)
floor_label.pack(pady=10)

# Input label
input_label = tk.Label(
    root,
    text="Enter Destination Floor:",
    font=("Arial", 12)
)
input_label.pack()

# Floor entry
floor_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center"
)
floor_entry.pack(pady=10)

# Go button
go_button = tk.Button(
    root,
    text="Go",
    font=("Arial", 14),
    bg="green",
    fg="white",
    width=10,
    command=go_to_floor
)
go_button.pack(pady=10)

# Status label
status_label = tk.Label(
    root,
    text="Waiting...",
    font=("Arial", 12),
    fg="blue"
)
status_label.pack(pady=15)

# Exit button
exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 12),
    bg="red",
    fg="white",
    width=10,
    command=root.destroy
)
exit_button.pack(pady=10)

# Start GUI
root.mainloop()