import tkinter as tk
import ttkbootstrap as ttk
import requestsHandler
import ankiCardsHandler

class OptionsWindow(tk.Toplevel):
    searchedWord = ''

    def __init__(self, sentences: list, searchedWord: str):
        tk.Toplevel.__init__(self)
        self.geometry("700x400")
        self.searchedWord = searchedWord
        self._build_choices(sentences)

    def _create_canvas_with_scrollbar(self, rootFrame: ttk.Frame) -> ttk.Canvas:
        canvas = ttk.Canvas(master = rootFrame)
        canvas.pack(side = "left", fill = "both", expand = True)
        scrollbar = tk.Scrollbar(master = rootFrame, orient = tk.VERTICAL, command = canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        return canvas

    def _create_dictionary_panel(self, word: str):
        dictionaryFrame = ttk.Frame(master = self, height = 5, width = 10)
        dictionaryFrame.pack(expand = True, side = "left")

        wordBase, wordMeanings = requestsHandler.get_word_data(word)

        wordLabel = ttk.Label(master = dictionaryFrame, text = wordBase)
        wordLabel.pack()
        
        meaningsLabel = ttk.Label(master = dictionaryFrame, text = ankiCardsHandler.format_back(wordMeanings))
        meaningsLabel.pack()

    def _build_choices(self, sentences: list):
        buttonStyle = ttk.Style()
        buttonStyle.configure("Big.TButton", padding = (15, 4))

        self._create_dictionary_panel(self.searchedWord)

        rootFrame = ttk.Frame(master = self)
        rootFrame.pack(fill = "both", expand = True, side = "right", anchor = "e") # TODO: fix alignment
        scrollCanvas = self._create_canvas_with_scrollbar(rootFrame)

        contentFrame = ttk.Frame(scrollCanvas)
        contentFrame.pack(expand = True)
        scrollCanvas.create_window((0, 0), window = contentFrame, anchor = "nw")

        for i in range(len(sentences)): # maybe use enumerate instead
            optionFrame = ttk.Frame(contentFrame)
            optionFrame.pack(side = "top", padx = 15, pady = 15)

            labelBackground = ttk.Frame(master = optionFrame)
            labelBackground.pack(side = "left", padx = 10, fill = "y")

            textWidget = ttk.Text(labelBackground, wrap = "word", height = 2.5, width = 40)
            textWidget.insert("1.0", sentences[i])
            textWidget.pack()

            buttonFrame = ttk.Frame(optionFrame, height = 2.4)
            buttonFrame.pack(side = "left", padx = 10)

            chooseButton = ttk.Button(master = buttonFrame, 
                                      text = "Add", 
                                      style = "Big.TButton", 
                                      name = str(i), # i = position of the phrase in the list
                                      width = 6
                                      )
            chooseButton.config(command = lambda id=chooseButton.winfo_name(): self.add_card(self.searchedWord, sentences[int(id)]))
            chooseButton.pack(pady = (0, 5))
            editButton = ttk.Button(master = buttonFrame, text = "Editar", style = "Big.TButton", width = 6)
            editButton.pack()
    
    def reinitialize(self, searchedWord: str, sentences: list):
        self.searchedWord = searchedWord
        children = self.winfo_children()
        for child in children:
            child.destroy()
        self._build_choices(sentences)

    def add_card(self, searchedWord: str, chosenSentence: str):
        ankiCardsHandler.add_card_to_txt(searchedWord, chosenSentence)

def main():
    word, meanings = requestsHandler.get_word_data("devrait")
    print(word)
    print(ankiCardsHandler.format_back(meanings))

if __name__ == "__main__":
    main()