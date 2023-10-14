import tkinter as tk
from tkinter import messagebox
import random

# Define a list of questions and answers.
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "correct_answer": "Mars",
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_answer": "Blue Whale",
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["Beijing", "Tokyo", "Seoul", "Shanghai"],
        "correct_answer": "Tokyo",
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Methane"],
        "correct_answer": "Carbon Dioxide",
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        self.score = 0
        self.current_question = 0
        
        self.question_label = tk.Label(root, text="",fg="white",bg="black", font=("Helvetica", 23))
        self.question_label.pack(pady=30)
        
        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        
        for i in range(4):
            radio_btn = tk.Radiobutton(root, text="", variable=self.radio_var,font=16, value=i)
            self.radio_buttons.append(radio_btn)
            radio_btn.pack(pady=10)
        
        self.next_button = tk.Button(root, text="Next", font=5,command=self.next_question)
        self.next_button.pack(pady=20)
        
        self.show_question()
    
    def show_question(self):
        if self.current_question < len(questions):
            q = questions[self.current_question]
            self.question_label.config(text=q["question"])
            options = q["options"]
            for i in range(4):
                self.radio_buttons[i].config(text=options[i])
            self.radio_var.set(None)
        else:
            self.show_result()
    
    def next_question(self):
        if self.current_question < len(questions):
            user_answer = self.radio_var.get()
            if user_answer is not None:
                user_answer = int(user_answer)
                q = questions[self.current_question]
                if q["options"][user_answer] == q["correct_answer"]:
                    self.score += 1
                self.current_question += 1
                self.show_question()
        else:
            self.show_result()
    
    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"You got {self.score}/{len(questions)} questions correct!")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="grey")
    app = QuizApp(root)
    root.mainloop()
