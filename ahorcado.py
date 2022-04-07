from simple_term_menu import TerminalMenu

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
                    print(index)

    difficulties =[data | {"last_num": difficulties[index+1]["num"] - 1} if index <= len(difficulties) - 2 else  data | {"last_num": end } for index,data in enumerate(difficulties)]
    return difficulties

def main():
    """ Configuration variables """
    language_data = None
    difficulty  = None

    """ Language Selection """
    available_languages = get_languages()
    language_selector = TerminalMenu(list(map( lambda x : x["language"] , available_languages)))
    language_selection_index = language_selector.show()
    language_data = available_languages[language_selection_index]
    print(language_data)
    """ Difficulty Selection """
    available_difficulties = get_difficulties_in_range(language_data["num"],language_data["last_num"])
    print(available_difficulties)

def initial_configuration():
    pass


if __name__ == "__main__":
    main()