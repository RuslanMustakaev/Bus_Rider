with open("animals.txt", "r") as file:
    file_content = file.readlines()
    content_new_file = ("".join(file_content)).replace("\n", " ")
with open("animals_new.txt", "w") as new_file:
    new_file.write(content_new_file)

"""with open('animals.txt', 'r', encoding='utf_8') as file_in:
    with open('animals_new.txt', 'w', encoding='utf_8') as file_out:
        for animal in file_in:
            file_out.write(animal.replace('\n', ' '))"""
