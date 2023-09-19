def count_words(string):
    
    if string == "":
        return 0    
    else:
        count_word_list = string.split(" ")      
        word_total = len(count_word_list)
        return word_total
        