import customtkinter as ctk
import requestsHandler
import ankiCardsHandler

class OptionsWindow(ctk.CTkToplevel):
    searchedWord = ''

    def __init__(self, sentences: list, searchedWord: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("700x400")

        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        self.searchedWord = searchedWord
        self.sentences = sentences
        self.dictionaryPanel = None
        self.scrollFrame = None
        self.optionFrames = []
        self._build_choices(sentences)

    def _create_dictionary_panel(self, word: str):
        if self.dictionaryPanel is not None:
            self.dictionaryPanel.destroy()

        dictionaryFrame = ctk.CTkFrame(master=self)
        dictionaryFrame.grid(row = 0, column = 0, sticky = "")
        dictionaryFrame.grid_columnconfigure(0, minsize = 150, weight = 1)
        dictionaryFrame.grid_rowconfigure(0, weight = 1, minsize = 75)
        dictionaryFrame.grid_rowconfigure(1, weight = 1, minsize = 75)

        wordBase, wordMeanings = requestsHandler.get_word_data(word)

        wordLabel = ctk.CTkLabel(master=dictionaryFrame, text=wordBase)
        wordLabel.grid(row = 0, column = 0, sticky = "s")

        meaningsLabel = ctk.CTkLabel(master=dictionaryFrame, text=ankiCardsHandler.format_back(wordMeanings), wraplength=90)
        meaningsLabel.grid(row = 1, column = 0, sticky = "n")

        self.dictionaryPanel = dictionaryFrame

    def _build_choices(self, sentences: list):
        self._create_dictionary_panel(self.searchedWord)

        if self.scrollFrame is None:
            self.scrollFrame = ctk.CTkScrollableFrame(master=self, width = 400)
            self.scrollFrame.grid(row = 0, column = 1, sticky = "nsew")
            self.scrollFrame.grid_columnconfigure(0, weight = 1)

        for i, sentence in enumerate(sentences):
            if i < len(self.optionFrames):
                textWidget, chooseButton, editButton = self.optionFrames[i]
                textWidget.delete("1.0", "end")
                textWidget.insert("1.0", sentence)
                chooseButton.configure(command=lambda id=sentence: self.add_card(self.searchedWord, id))
            else:
                optionFrame = ctk.CTkFrame(self.scrollFrame, width = 200, height = 61)
                optionFrame.grid(row = i, column = 0, pady = 15)

                textWidget = ctk.CTkTextbox(optionFrame, wrap="word", height=61, width=200)
                textWidget.insert("1.0", sentence)
                textWidget.grid(row = 0, column = 0)

                buttonFrame = ctk.CTkFrame(optionFrame, width=80)
                buttonFrame.grid(row = 0, column = 1, padx = 10)

                chooseButton = ctk.CTkButton(master=buttonFrame, text="Add", width=80)
                chooseButton.configure(command=lambda id=sentence: self.add_card(self.searchedWord, id))
                chooseButton.grid(row = 0, column = 0, pady=(0, 5))

                editButton = ctk.CTkButton(master=buttonFrame, text="Editar", width=80)
                editButton.grid(row = 1, column = 0)

                self.optionFrames.append((textWidget, chooseButton, editButton))

        for i in range(len(sentences), len(self.optionFrames)):
            textWidget, chooseButton, editButton = self.optionFrames[i]
            textWidget.master.pack_forget()
            self.optionFrames[i] = (textWidget, chooseButton, editButton)

    def reinitialize(self, searchedWord: str, sentences: list):
        self.searchedWord = searchedWord
        self.sentences = sentences
        self._build_choices(sentences)

    def add_card(self, searchedWord: str, chosenSentence: str):
        ankiCardsHandler.add_card_to_txt(searchedWord, chosenSentence)

def main():
    word, meanings = requestsHandler.get_word_data("devrait")
    print(word)
    print(ankiCardsHandler.format_back(meanings))

if __name__ == "__main__":
    main()