import tkinter as tk
import random
import time

class TypingSpeedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Calculator")

        self.create_ui_elements()

        self.typing_start_time = None
        self.typing_end_time = None
        self.generated_sentence = None

    def create_ui_elements(self):
        self.sentence_label = tk.Label(root, text="Type the sentence below:")
        self.sentence_label.pack()

        self.sentence_display = tk.Label(root, text="", font=("Helvetica", 14))
        self.sentence_display.pack()

        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack()

        self.start_button = tk.Button(root, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        # Bind the Enter key to call the update_typing_speed method
        self.text_entry.bind('<Return>', lambda event=None: self.update_typing_speed())

    def generate_sentence(self):
        sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Programming is both fun and challenging.",
            "Practice makes perfect.",
            "Typing speed is crucial in the digital age.",
            "OpenAI's GPT-3 is an impressive language model."
        ]
        self.generated_sentence = random.choice(sentences)
        self.sentence_display.config(text=self.generated_sentence)

    def start_typing_test(self):
        self.generate_sentence()
        self.typing_start_time = time.time()
        self.start_button.config(state=tk.DISABLED)

    def evaluate_typing_speed(self):
        if self.typing_start_time and self.typing_end_time and self.generated_sentence:
            typed_text = self.text_entry.get()
            elapsed_time = self.typing_end_time - self.typing_start_time
            words_per_minute = (len(typed_text.split()) / elapsed_time) * 60

            accuracy = self.calculate_accuracy(typed_text, self.generated_sentence)

            if words_per_minute >= 60 and accuracy >= 0.9:
                result = "Excellent"
            elif words_per_minute >= 40 and accuracy >= 0.7:
                result = "Good"
            else:
                result = "Average"

            return f"Result: {result} (Speed: {words_per_minute:.2f} WPM, Accuracy: {accuracy:.2f})"
        else:
            return "Start typing to get a result."

    def calculate_accuracy(self, typed_text, reference_text):
        correct_characters = sum(1 for a, b in zip(typed_text, reference_text) if a == b)
        total_characters = max(len(typed_text), len(reference_text))
        return correct_characters / total_characters if total_characters > 0 else 0

    def update_typing_speed(self):
        self.typing_end_time = time.time()
        result = self.evaluate_typing_speed()
        self.result_label.config(text=result)
        self.start_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedCalculator(root)
    root.mainloop()
