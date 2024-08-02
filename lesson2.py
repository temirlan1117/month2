# ООП
# принципы ООП


class Book:
    strr = 400
    # методы
    def __init__(self, title, author, color):
        self.title = title
        self.author = author
        self.color = color

    def info(self):
        print(self.title, self.author, self.color, self.strr)

    def __str__(self):
        return (f'title:{self.title}, author:{self.author}, \n'
                f'color:{self.color}, strr:{self.strr}, \n')
    def __len__(self):
        return len(self.title + self.color + self.author)

# обьект, экземпляр класса
город_воров = Book('город воров', 'Каныкей', "зелёный")
капитанская_дочка = Book('капитанская дочка', "Пушкин", "серый")


print(len(капитанская_дочка))

# beka = Book("этомир", "бека", "блек")
# `print(len(beka))
# Is= [1,1,1,1]
# print(Is)`