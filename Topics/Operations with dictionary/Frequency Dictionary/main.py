sentence_list = input().lower().split()
sentence_dict = {word: sentence_list.count(word) for word in sentence_list}
for key, value in sentence_dict.items():
    print(key, value)
