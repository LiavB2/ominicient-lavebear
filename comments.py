import json

class Person:
    def __init__(self, name, comment):
        self.name = name
        self.comment = comment

def generate_board(persons):
    rows = ""
    for person in persons:
        row = f"<tr><td>{person.name}</td><td>{person.comment}</td></tr>"
        rows += row
    return f"<table>{rows}</table>"

def save_to_json(persons):
    data = []
    for person in persons:
        data.append({"name": person.name, "comment": person.comment})
    with open("data.json", "w") as file:
        json.dump(data, file)

def load_from_json():
    with open("data.json", "r") as file:
        data = json.load(file)
    persons = []
    for item in data:
        persons.append(Person(item["name"], item["comment"]))
    return persons

def update_markdown_file(board_html):
    with open("board.md", "w") as file:
        file.write(board_html)

def main():
    persons = []
    while True:
        name = input("Enter your name (or 'q' to quit): ")
        if name == "q":
            break
        comment = input("Enter your comment: ")
        persons.append(Person(name, comment))
    
    save_to_json(persons)
    persons = load_from_json()
    board = generate_board(persons)
    update_markdown_file(board)

if __name__ == "__main__":
    main()
