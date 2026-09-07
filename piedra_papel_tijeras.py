import random
import tkinter as tk
from tkinter import ttk


CHOICES = ("roca", "papel", "tijeras")


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate"

    winning_choices = {
        "roca": "tijeras",
        "papel": "roca",
        "tijeras": "papel",
    }
    if winning_choices[user_choice] == computer_choice:
        return "¡Ganaste!"
    return "¡Perdiste!"


class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, papel o tijeras")
        self.root.geometry("480x430")
        self.root.minsize(420, 390)

        self.user_score = 0
        self.computer_score = 0
        self.draws = 0

        self._configure_style()
        self._build_interface()

    def _configure_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"), foreground="#183153")
        style.configure("Subtitle.TLabel", font=("Segoe UI", 11), foreground="#526477")
        style.configure("Choice.TButton", font=("Segoe UI", 12, "bold"), padding=(14, 12))
        style.configure("Result.TLabel", font=("Segoe UI", 17, "bold"), foreground="#183153")
        style.configure("Score.TLabel", font=("Segoe UI", 11), foreground="#526477")

    def _build_interface(self):
        main = ttk.Frame(self.root, padding=28)
        main.pack(fill="both", expand=True)

        ttk.Label(main, text="Piedra, papel o tijeras", style="Title.TLabel").pack()
        ttk.Label(main, text="Elige una opcion para comenzar la partida", style="Subtitle.TLabel").pack(pady=(6, 24))

        choices_frame = ttk.Frame(main)
        choices_frame.pack(fill="x")
        for choice in CHOICES:
            ttk.Button(
                choices_frame,
                text=choice.capitalize(),
                style="Choice.TButton",
                command=lambda selected=choice: self.play_round(selected),
            ).pack(side="left", expand=True, fill="x", padx=5)

        self.user_choice_label = ttk.Label(main, text="Tu eleccion: -", style="Subtitle.TLabel")
        self.user_choice_label.pack(pady=(30, 4))
        self.computer_choice_label = ttk.Label(main, text="Computadora: -", style="Subtitle.TLabel")
        self.computer_choice_label.pack(pady=4)
        self.result_label = ttk.Label(main, text="Que gane el mejor", style="Result.TLabel")
        self.result_label.pack(pady=18)

        self.score_label = ttk.Label(main, text="Tu: 0    Empates: 0    Computadora: 0", style="Score.TLabel")
        self.score_label.pack()
        ttk.Button(main, text="Reiniciar marcador", command=self.reset_score).pack(pady=24)

    def play_round(self, user_choice):
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        self.user_choice_label.config(text=f"Tu eleccion: {user_choice.capitalize()}")
        self.computer_choice_label.config(text=f"Computadora: {computer_choice.capitalize()}")
        self.result_label.config(text=result)

        if result == "¡Ganaste!":
            self.user_score += 1
        elif result == "¡Perdiste!":
            self.computer_score += 1
        else:
            self.draws += 1
        self._update_score()

    def reset_score(self):
        self.user_score = 0
        self.computer_score = 0
        self.draws = 0
        self.user_choice_label.config(text="Tu eleccion: -")
        self.computer_choice_label.config(text="Computadora: -")
        self.result_label.config(text="Que gane el mejor")
        self._update_score()

    def _update_score(self):
        self.score_label.config(
            text=f"Tu: {self.user_score}    Empates: {self.draws}    Computadora: {self.computer_score}"
        )


def main():
    root = tk.Tk()
    RockPaperScissorsApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()