import os
import docx2txt

from tkinter import *

def search_for_text(folder_path, search_text):
    matching_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".docx"):
            file_path = os.path.join(folder_path, filename)
            text = docx2txt.process(file_path)
            if search_text in text:
                matching_files.append(filename)
    return matching_files

def search_for_files():
    folder_path = folder_path_entry.get()
    search_text = search_text_entry.get()
    matching_files = search_for_text(folder_path, search_text)
    result_text.delete(1.0, END)
    if matching_files:
        result_text.insert(END, "Files containing the search text:\n")
        for filename in matching_files:
            result_text.insert(END, f"{filename}\n")
    else:
        result_text.insert(END, "No files containing the search text were found.")

root = Tk()
root.title("Docx Search")
root.geometry("500x500")

folder_path_label = Label(root, text="Folder Path:")
folder_path_label.pack()
folder_path_entry = Entry(root, width=50)
folder_path_entry.pack()

search_text_label = Label(root, text="Search Text:")
search_text_label.pack()
search_text_entry = Entry(root, width=50)
search_text_entry.pack()

search_button = Button(root, text="Search", command=search_for_files)
search_button.pack()

result_text = Text(root, height=20, width=60)
result_text.pack()

root.mainloop()
