import requestsHandler
from os import path

class BasicCard():
    front = ""
    back = ""

    def __init__(self, front: str, back: str):
        self.front = front
        self.back = back

def format_back(wordMeanings: list) -> str: # TODO: change name to something more general
    back = ""
    if len(wordMeanings) == 0:
        print("No meanings found")
        return ""
    else:
        for i in range(len(wordMeanings)):
            if i <= 3:
                if i == len(wordMeanings) - 1:
                    back += wordMeanings[i] + "." # period if last word
                else:
                    back += wordMeanings[i] + ", "
            else:
                break
    return back

def create_card(sentence: str, word: str, wordMeanings: list) -> BasicCard: # TODO: change this to the constructor of BasicCard
    back = f"{word}: {format_back(wordMeanings)}" 
    return BasicCard(sentence, back)

def add_card_to_txt(searchedWord: str, chosenSentence: str):
    defaultHeaders = "#separator:|\n#html:true\n"

    baseWord, wordMeanings = requestsHandler.get_word_data(searchedWord)
    card = create_card(chosenSentence, baseWord, wordMeanings)

    firstLine = ""

    if not path.exists("./Cards.txt"):
        file = open("Cards.txt", "w")
        file.close()

    with open("Cards.txt", "r", encoding = "utf-8") as file:
        firstLine = file.readline().strip()

    with open("Cards.txt", "a", newline="", encoding = "utf-8") as file:
        if firstLine:
            file.write("\n")
        else:
            file.write(defaultHeaders)
        file.write(card.front + "|" + card.back)
        print("Added successfully!")

def main():
    add_card_to_txt("Devrait", "Mes devoirs sont ennuyant.")

if __name__ == "__main__":
    main()
