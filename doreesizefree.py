import os
import tkinter as tk
from tkinter import filedialog

def get_folder_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_folder_size(entry.path)
            print("hello")
            print("this is flash man")
    return total

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_size = get_folder_size(folder_selected)
    size_var.set(f'Folder size: {folder_size} bytes')

window = tk.Tk()

size_var = tk.StringVar(window)

browse_btn = tk.Button(window, text="Browse", command=browse_folder)
browse_btn.pack()

size_label = tk.Label(window, textvariable=size_var)
size_label.pack()

window.mainloop()
