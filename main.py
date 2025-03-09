from stats import count_words, char_count, make_two_key_dict
import sys

def get_book_text(file_path):
  try:
    with open(file_path) as f:
      file_contents =f.read()
      return str(file_contents)
  except FileNotFoundError:
    print(f"Error: File {file_path} not found")
  except Exception as e:
    print(f"An error occured: {e}")

def main():
  if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  filepath = sys.argv[1]

  text = get_book_text(filepath)
  count_of_words = count_words(text)
  one_key_dict = char_count(text)
  two_key_dict = make_two_key_dict(one_key_dict)
  
  print_string = f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {count_of_words} total words
--------- Character Count -------\n"""
  for item in two_key_dict:
    if item['char'].isalpha():
      print_string += f"{item['char']}: {item['count']}\n"
  print_string += f"============= END ==============="
  print(print_string)

main()