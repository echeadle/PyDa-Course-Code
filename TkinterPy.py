import tkinter as tk
from tkinter import ttk


class MyFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyDa")
        self.geometry("450x100")

        lbl = ttk.Label(
            self,
            text="Hello I am Pyda the Python Digital Assistant. How can I help you?",
        )
        lbl.pack(pady=5)

        self.txt = ttk.Entry(self, width=50)
        self.txt.pack(pady=5)
        self.txt.bind("<Return>", self.on_enter)
        self.txt.focus_set()

    def on_enter(self, event):
        input_text = self.txt.get()
        input_text = input_text.lower()


if __name__ == "__main__":
    app = MyFrame()
    app.mainloop()
