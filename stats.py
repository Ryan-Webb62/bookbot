def count_words(text):
  split_text = text.split()
  num_words = len(split_text)
  return num_words


def char_count(text):
  chars = {}
  for char in text.lower():
    if char in chars:
      chars[char] += 1
    else:
      chars[char] =1
  return chars


def make_two_key_dict(one_key_dict):
  two_key_dict_list=[]
  for char, count in one_key_dict.items():
    two_key_dict_list.append({"char":char,"count":count})
  two_key_dict_list.sort(key=lambda item: item["count"], reverse=True)
  return(two_key_dict_list)

