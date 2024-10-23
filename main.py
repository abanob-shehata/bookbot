def main():
    book_path = "books/frankenstein.txt"
    filecontents = get_text(book_path)
    word_count = get_wc(filecontents)
    char_count = get_char_count(filecontents)
    # print(filecontents)
    # print(f"The text word count is: {word_count}")
    # print(char_count)
    print_report(book_path, word_count, char_count)
    
def get_text(path):
    with open(path) as f:
        return f.read()
    
def get_wc(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def print_report(path, wc, dict):
    print(f"--- Begin report of {path} ---")
    print(f"{wc} words found in the document")
    sorted_list = sort_dict(dict)
    for item in sorted_list:
        print(f"The {item['letter']} character was found {item['count']} times")
    print("--- End report ---")
    
def sort_dict(dict):
    list = []
    for item in dict:
        list.append({"letter": item, "count": dict[item]})
    list.sort(reverse=True, key=sorton)
    return list

def sorton(dict):
    return dict["count"]

main()