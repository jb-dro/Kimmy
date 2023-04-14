import tkinter as tk
import random, os
import split_button

random.seed(42)  # Set random seed for reproducibility
score = 0  # Set initial score to 0

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

root = tk.Tk()
root.title("Split Button App")
root.attributes("-fullscreen", True)  # Set to full screen

root_button = split_button.SplitButton(root, "horizontal")

# # add score box to the top right corner
# score_box = tk.Label(root, text="Score: ", font=("Helvetica", 16))
# score_box.pack(side=tk.TOP, anchor=tk.NE)

# add exit button to the top right corner
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(side=tk.TOP, anchor=tk.NE)

root.mainloop()
