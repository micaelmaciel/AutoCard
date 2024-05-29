import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
import requestsHandler
from optionsWindow import OptionsWindow


def _on_choice_window_closed():
    global optionsWindow
    optionsWindow.destroy()
    optionsWindow = None

def search_word():
    global optionsWindow
    searchResult = requestsHandler.get_sentences(word.get())
    if optionsWindow == None:
        optionsWindow = OptionsWindow(searchResult, word.get())
        optionsWindow.protocol("WM_DELETE_WINDOW", _on_choice_window_closed)
    else:
        optionsWindow.reinitialize(word.get(), searchResult)


optionsWindow: OptionsWindow = None

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
window = ctk.CTk()
window.title("Anki Card Generator")
window.geometry("400x250")

searchFrame = ctk.CTkFrame(master = window, fg_color=None)
searchFrame.pack(pady = 20)

word = ctk.StringVar()
wordField = ctk.CTkEntry(master = searchFrame, textvariable = word)
wordField.pack(side = "left", padx = 10)

searchButton = ctk.CTkButton(master = searchFrame, text = "Pesquisar", command = search_word)
searchButton.pack(side = "left")

window.mainloop()
