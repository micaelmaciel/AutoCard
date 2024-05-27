import tkinter as tk
import ttkbootstrap as ttk
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
window = ttk.Window(themename = "darkly")
window.title("Anki Card Generator")
window.geometry("400x250")

searchFrame = ttk.Frame(master = window)
searchFrame.pack(pady = 20)

word = tk.StringVar()
wordField = ttk.Entry(master = searchFrame, textvariable = word)
wordField.pack(side = "left", padx = 10)

searchButton = ttk.Button(master = searchFrame, text = "Pesquisar", command = search_word)
searchButton.pack(side = "left")

window.mainloop()
