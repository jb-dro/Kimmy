import tkinter as tk
import random


class SplitButton:
    def __init__(self, master, split_direction):
        self.master = master
        self.split_direction = split_direction
        self.frame = tk.Frame(master)
        self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.button = tk.Button(self.frame, text='Press Me!', command=self.on_button_click)
        self.button.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.set_random_color()  # Set random color for the button

    def set_random_color(self):
        """
        Set a random background color for the button.
        """

        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        self.button.configure(bg=color)

    def on_button_click(self):
        """
        Callback function for button click event.
        """
        self.button.destroy()  # Destroy the original button
        if self.split_direction == "horizontal":
            # Split horizontally
            top_frame = tk.Frame(self.frame)
            top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            bottom_frame = tk.Frame(self.frame)
            bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            button1 = SplitButton(top_frame, "vertical")
            button2 = SplitButton(bottom_frame, "vertical")
        elif self.split_direction == "vertical":
            # Split vertically
            left_frame = tk.Frame(self.frame)
            left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            right_frame = tk.Frame(self.frame)
            right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
            button1 = SplitButton(left_frame, "horizontal")
            button2 = SplitButton(right_frame, "horizontal")
