import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)

current_player = "X"
winner = False
buttons = []

def check_winner():
    global winner

    combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in combos:
        a, b, c = combo

        if (buttons[a]["text"] == buttons[b]["text"]
                == buttons[c]["text"] != ""):
            winner = True

            for i in combo:
                buttons[i].config(bg="green", fg="white")

            messagebox.showinfo(
                "Tic-Tac-Toe",
                f"Player {buttons[a]['text']} wins!"
            )
            return True

    return False

def toggle_player():
    global current_player

    current_player = "O" if current_player == "X" else "X"
    turn_label.config(text=f"Player {current_player}'s turn")

def button_click(index):
    if buttons[index]["text"] != "" or winner:
        return

    buttons[index].config(text=current_player)

    if check_winner():
        turn_label.config(text=f"Player {current_player} wins!")
        return

    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "Game Draw!")
        turn_label.config(text="Game Draw!")
        return

    toggle_player()

def restart_game():
    global current_player, winner

    current_player = "X"
    winner = False

    for button in buttons:
        button.config(text="", bg="white", fg="black")

    turn_label.config(text="Player X's turn")

turn_label = tk.Label(
    root, text="Player X's turn",
    font=("Arial", 16)
)
turn_label.grid(row=0, column=0, columnspan=3, pady=10)

for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 24, "bold"),
        width=5,
        height=2,
        bg="white",
        command=lambda i=i: button_click(i)
    )
    button.grid(
        row=(i // 3) + 1,
        column=i % 3,
        padx=3,
        pady=3
    )
    buttons.append(button)

restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 12),
    command=restart_game
)
restart_button.grid(
    row=4, column=0, columnspan=3, pady=10
)

root.mainloop()