from simple_term_menu import TerminalMenu
import os
import random
def clear_view():
    os.system("clear")

def get_languages():
    languages = []
    file_len = 0
    with open("./words.hang", "r") as words_file:
        for num, line in enumerate(words_file,1):
            if "[" in line and "]" in line:
                line = line.rstrip("\n")
                languages.append({"language": line[1:len(line) -1] ,"num":num})
            if file_len < num: file_len = num
             
    language_full_data = []
    for index, lang_data in enumerate(languages):
        if index == len(languages) - 1:
            language_full_data.append(lang_data | {"last_num": file_len})
            continue
        new_lang_data = lang_data | { "last_num": int(languages[index + 1]["num"]) - 1}
        language_full_data.append(new_lang_data)
    return language_full_data

def get_difficulties_in_range(start: int,end: int):
    difficulties = []
    with open("./words.hang", "r") as words_file:
        for index,line in enumerate(words_file,1):
            if index >= start and index <= end:
                if "#" in line:
                    line = line.rstrip("\n")
                    difficulties.append({"difficulty": line[2::], "num": index})

    difficulties =[data | {"last_num": difficulties[index+1]["num"] - 2} if index <= len(difficulties) - 2 else  data | {"last_num": end } for index,data in enumerate(difficulties)]
    return difficulties

def get_word_in_range(start,end):
    words = []
    with open("./words.hang", "r", encoding="utf-8") as word_file:
        for index,line in enumerate(word_file):
            if index >= start and index <= end and "- " in line:
                line = line.rstrip("\n")
                words.append(line[2::])
    selected_word = words[random.randint(0,len(words)) - 1]
    return selected_word


def get_spaced_word(word):
    spaced_word = ""
    for char in word:
        spaced_word += " " + char
    return(spaced_word)

def start_game(language_data,difficulty_data):
    clear_view()
    word = get_word_in_range(difficulty_data["num"],difficulty_data["last_num"])
    word_to_complete = "".join(list(map(lambda _: "_",word)))
    finish = False

    def get_word_to_complete_with_selected_chars(word_to_complete,selected_char):
        new_word_to_complete = []
        for idx,char in enumerate(word):
            if char == selected_char:
                new_word_to_complete.append(char)
            else:
                new_word_to_complete.append(word_to_complete[idx])
        return "".join(new_word_to_complete)
    while not finish:
        print("|---+")
        print("|   0    ")
        print("|  /|\   ")
        print("|  / \   ")
        print("|________")
        print(get_spaced_word(word_to_complete))
        print("         ")
        selected_char = input("Write a character or word: ")
        word_to_complete = get_word_to_complete_with_selected_chars(word_to_complete,selected_char)
        if word == word_to_complete:
            finish = True
        clear_view()
    
    print("Nashe")
def main():

    clear_view()
    """ Configuration variables """
    language_data = None
    difficulty_data  = None

    """ Language Selection """

    available_languages = get_languages()
    language_selector = TerminalMenu(list(map( lambda x : x["language"] , available_languages)))
    language_selection_index = language_selector.show()
    language_data = available_languages[language_selection_index]
    print(language_data["language"])
    """ Difficulty Selection """

    available_difficulties = get_difficulties_in_range(language_data["num"],language_data["last_num"])
    difficulties_selector = TerminalMenu(list(map(lambda x: x["difficulty"],available_difficulties)))
    difficulty_index = difficulties_selector.show()
    difficulty_data = available_difficulties[difficulty_index]
    print(difficulty_data["difficulty"])

    start_game(language_data,difficulty_data)



def initial_configuration():
    pass


if __name__ == "__main__":
    main()