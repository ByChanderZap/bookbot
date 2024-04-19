def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = count_chars(text)
    sorted_list = count_to_sorted_list(chars_dict)
    # print(sorted_list)
    show_report(book_path, num_words, sorted_list)


def show_report(book_path, words_count, list):
  print(f"--- Being report of {book_path} ---")
  print(f"Books contains {words_count} words")
  print()

  for item in list:
     print(f"The character {item['char']} appears {item['count']} times")

  print("End of report...")


def get_num_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    chars = {}
    for char in text:
      lower_char = char.lower()
      
      if not lower_char.isalpha():
         continue
      
      if lower_char in chars:
        chars[lower_char] += 1
      else:
        chars[lower_char] = 0
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(d):
    return d["count"]

def count_to_sorted_list(dict_chars_count):
    sorted_list = []
    for ch in dict_chars_count:
      sorted_list.append({"char": ch, "count": dict_chars_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()