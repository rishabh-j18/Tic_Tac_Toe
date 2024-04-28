from tkinter import *
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title('Tic Tac Toe')

        self.player1_name = StringVar()
        self.player2_name = StringVar()
        self.winner_name = StringVar()  # Variable to store the winner's name
        self.clicked = True
        self.count = 0
        self.winner = False

        self.create_player_name_frame()

    def create_player_name_frame(self):
        self.player_name_frame = Frame(self.root)
        self.player_name_frame.pack()

        player1_label = Label(self.player_name_frame, text="Player 1 Name:")
        player1_label.grid(row=0, column=0, padx=10, pady=5)
        player1_entry = Entry(self.player_name_frame, textvariable=self.player1_name)
        player1_entry.grid(row=0, column=1, padx=10, pady=5)

        player2_label = Label(self.player_name_frame, text="Player 2 Name:")
        player2_label.grid(row=1, column=0, padx=10, pady=5)
        player2_entry = Entry(self.player_name_frame, textvariable=self.player2_name)
        player2_entry.grid(row=1, column=1, padx=10, pady=5)

        start_button = Button(self.player_name_frame, text="Start Game", command=self.start_game,foreground="white", background="red")
        start_button.grid(row=2, columnspan=2, padx=10, pady=5)

    def create_game_frame(self):
        self.game_frame = Frame(self.root)
        self.game_frame.pack()

        self.player1_label = Label(self.game_frame, text=f'Player 1: {(self.player1_name.get())}', foreground="blue", font=("Helvetica", 10))
        self.player1_label.pack(side=LEFT, padx=10, pady=5)

        self.player2_label = Label(self.game_frame, text=f'Player 2: {self.player2_name.get()}', foreground="red", font=("Helvetica", 10))
        self.player2_label.pack(side=RIGHT, padx=20, pady=5)

        self.winner_label = Label(self.game_frame, textvariable=self.winner_name, foreground="green", font=("Helvetica", 10))
        self.winner_label.pack(padx=10, pady=5)

        self.create_buttons()
        
        self.play_again_button = Button(self.game_frame, text="Play Again", command=self.play_again, foreground="white", background="green")
        self.play_again_button.pack(side=LEFT, padx=10, pady=10)
        
        self.restart_button = Button(self.game_frame, text="Restart Game", command=self.restart_game, foreground="white", background="blue")
        self.restart_button.pack(side=LEFT, padx=10)

        self.end_button=Button(self.game_frame,text="Quit", command=self.quit_game,foreground="white", background="red")
        self.end_button.pack(side=RIGHT,padx=10,pady=5)

    def create_buttons(self):
        self.buttons = []
        for i in range(3):
            frame = Frame(self.game_frame)
            frame.pack()
            for j in range(3):
                button = Button(frame, text=" ", font=("Helvetica, 20"), height=3, width=7, bg="White")
                button.pack(side=LEFT)
                button.config(command=lambda current_button=button: self.button_clicked(current_button))
                self.buttons.append(button)

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=DISABLED)

    def check_winner(self):
        patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for pattern in patterns:
            if self.buttons[pattern[0]]["text"] == self.buttons[pattern[1]]["text"] == self.buttons[pattern[2]]["text"] != " ":
                for i in pattern:
                    self.buttons[i].config(bg="#80ffaa")
                self.winner = True
                if self.buttons[pattern[0]]["text"] == "X":
                    self.winner_name.set(f"{self.player1_name.get()} is the Winner!")
                else:
                    self.winner_name.set(f"{self.player2_name.get()} is the Winner!")
                self.disable_buttons()

    def check_draw(self):
        if self.count == 9 and not self.winner:
            self.winner_name.set("It's a Draw!")

    def button_clicked(self, button):
        if button["text"] == " " and self.clicked:
            button["text"] = "X"
            self.clicked = False
            self.count += 1
        elif button["text"] == " " and not self.clicked:
            button["text"] = "O"
            self.clicked = True
            self.count += 1
        else:
            messagebox.showerror("Tic Tac Toe", "Please select another box.")
            return
        self.check_winner()
        self.check_draw()

    def start_game(self):
        if self.player1_name.get() == "" or self.player2_name.get() == "":
            messagebox.showerror("Tic Tac Toe", "Please enter player names.")
        else:
            self.player_name_frame.destroy()
            self.create_game_frame()
            messagebox.showinfo("Tic Tac Toe", f"Let's start the game between {self.player1_name.get()} and {self.player2_name.get()}!")

    def play_again(self):
        for button in self.buttons:
            button["text"] = " "
            button.config(bg="White", state=NORMAL)
        self.winner_name.set("")
        self.count = 0
        self.winner = False

    def restart_game(self):
        self.game_frame.forget()
        self.play_again()
        self.create_player_name_frame()
    def quit_game(self):
        self.root.destroy()

root = Tk()
game = TicTacToe(root)
root.mainloop()
