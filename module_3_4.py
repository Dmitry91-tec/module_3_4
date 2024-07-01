same_words = []
def first(string_1, string_2):
    global same_words
    string_1low = string_1.lower()
    string_2low = string_2.lower()
    if len(string_1) >= len(string_2):
        index_ = string_1low.find(string_2low)                    #вхождение 2-й строки в 1-ю
        while index_ >= 0:
            break
        if string_1low[index_:index_+len(string_2low)] == string_2low:
            same_words += [string_2]
    elif len(string_1) < len(string_2):
        index_ = string_2low.find(string_1low)                    # вхождение 1-й строки в 2-ю
        while index_ >= 0:
            break
        if string_2low[index_:index_ + len(string_1low)] == string_1low:
            same_words += [string_2]
def single_root_words(root_word, *other_words):
    global same_words
    for i in other_words:
        first(root_word,i)
    print(same_words)
    same_words = []


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
