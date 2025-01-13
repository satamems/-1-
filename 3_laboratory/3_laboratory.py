read_path = "3_laboratory/example.txt"
write_path = "3_laboratory/saved_text.txt"


def print_file(path):
    try:
        with open(path, "r") as file:
            content = file.read()
            print(content)
            file.close()
    except FileNotFoundError:
        print("Файл с таким именем не найден")

def print_file_by_string(path):
    try:
        with open(path, "r") as file:
            for line in file:
                print(line)
            file.close()
    except FileNotFoundError:
        print("Файл с таким именем не найден")


def write_text(path):
    text = input("введите текст: ")
    with open("3_laboratory/user_input.txt", "a") as file:
        file.write(text + "\n")
        file.close()


def write_text(path):
    text = input("введите текст: ")
    file = open(path, "x")
    file.write(text)
    file.close()

        


