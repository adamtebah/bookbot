def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for ch in text:
        ch = ch.lower()
        if ch in char_counts:
            char_counts[ch] += 1
        else:
            char_counts[ch] =1
    return char_counts

def sort_on(char_dict):
    return char_dict["num"]

def chars_dict_to_sorted_list(char_counts):
    chars_list = []
    for ch, count in char_counts.items():
        chars_list.append({"char": ch, "num": count})
    chars_list.sort(key=sort_on, reverse=True)
    return chars_list