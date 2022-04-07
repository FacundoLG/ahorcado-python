from simple_term_menu import TerminalMenu


def get_languages():
    languages = []
    file_len = 0
    with open("./words.hang", "r") as words_file:
        for num, line in enumerate(words_file,1):
            if "[" in line and "]" in line:
                line = line.rstrip("\n")
                languages.append({"language": line,"num":num})
            if file_len < num: file_len = num
             
    language_full_data = []
    for index, lang_data in enumerate(languages):
        if index == len(languages) - 1:
            language_full_data.append(lang_data | {"last_num": file_len})
            continue
        new_lang_data = lang_data | { "last_num": int(languages[index + 1]["num"]) - 1}
        language_full_data.append(new_lang_data)
    return language_full_data


def main():
    """ Configuration variables """
    language = None
    difficulty  = None
    available_languages = get_languages()
    language_selector = TerminalMenu(list(map( lambda x : x["language"] , available_languages)))
    language_selector.show()

def initial_configuration():
    pass


if __name__ == "__main__":
    main()