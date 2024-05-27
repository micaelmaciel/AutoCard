import requestsHandler

class BasicCard():
    front = ""
    back = ""

    def __init__(self, front: str, back: str):
        self.front = front
        self.back = back

def create_card(sentence: str, word: str, wordMeanings: list) -> BasicCard:
    back = f"{word}: "
    if len(wordMeanings) == 0:
        print("Word not found")
    else:
        for i in range(len(wordMeanings)):
            if i <= 3:
                if i == len(wordMeanings) - 1:
                    back += wordMeanings[i] + "." # period if last word
                else:
                    back += wordMeanings[i] + ", "
            else:
                break
    return BasicCard(sentence, back)

def add_card_to_txt(searchedWord: str, chosenSentence: str):
    defaultHeaders = "#separator:|\n#html:true\n"

    wordMeanings = requestsHandler.get_word_meanings(searchedWord)
    card = create_card(chosenSentence, searchedWord, wordMeanings)

    firstLine = ""

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
    add_card_to_txt("Parler", "Je ne sais pas parler avec aucune persone... mais je l'aime même quand.")

if __name__ == "__main__":
    main()
