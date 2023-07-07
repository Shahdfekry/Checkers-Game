import tkinter as tk



class CheckersGameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Checkers Game")

        # Create the difficulty level selection frame
        difficulty_frame = tk.Frame(self.root)
        difficulty_label = tk.Label(difficulty_frame, text="Difficulty Level")
        difficulty_label.pack(side=tk.TOP, pady=30)

        # Create the difficulty level buttons
        self.difficulty_var = tk.StringVar()
        self.alg_var=tk.StringVar()
        easy_button = tk.Radiobutton(difficulty_frame, text="Easy", variable=self.difficulty_var, value="easy")
        easy_button.pack(side=tk.TOP, padx=10)
        medium_button = tk.Radiobutton(difficulty_frame, text="Medium", variable=self.difficulty_var, value="medium")
        medium_button.pack(side=tk.TOP, padx=10)
        hard_button = tk.Radiobutton(difficulty_frame, text="Hard", variable=self.difficulty_var, value="hard")
        hard_button.pack(side=tk.TOP, padx=10)

        alg_label = tk.Label(difficulty_frame, text="Your color is brown , choose algorithm:")
        alg_label.pack(side=tk.TOP, pady=30)
        Alpha_button = tk.Radiobutton(difficulty_frame, text="AlphaBeta", variable=self.alg_var, value="alphabeta")
        Alpha_button.pack(side=tk.TOP, padx=10)
        minimax_button = tk.Radiobutton(difficulty_frame, text="Minimax", variable=self.alg_var, value="minimax")
        minimax_button.pack(side=tk.TOP, padx=10)


        # Create the start game button
        start_button = tk.Button(self.root, text="Start Game", command=self.combined)

        # Pack the frames and buttons
        difficulty_frame.pack(side=tk.TOP)
        start_button.pack(side=tk.TOP, pady=10)

        self.root.mainloop()
    def combined (self):
        self.getalgorithm()
        self.start_game()
        self.root.destroy()

    def getalgorithm(self):
        algorithm = self.alg_var.get()

        if algorithm=="minimax":
            return "minimax"
        elif algorithm=="alphabeta":
            return "alphabeta"



    def start_game(self):
        # Retrieve the selected difficulty level
        global depth
        difficulty_level = self.difficulty_var.get()

        if difficulty_level == "easy":
            depth = 2
        elif difficulty_level == "medium":
            depth = 3
        elif difficulty_level == "hard":
            depth = 4

        alg = self.getalgorithm()
        return depth, alg

        # Start the game with the selected difficulty level
        # Code for starting the game goes here
        pass
