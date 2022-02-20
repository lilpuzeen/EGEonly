class Wizard:

    def __init__(self, name, rating, age):  # имя, рейтинг и оценка возраста
        self.name = name
        # при инициализаии будем счиать, что ::
        # рейтинг лежит в диапазоне [1, 100]
        # возраст лежит в диапазоне [18, +inf]
        self.rating = rating
        self.age = age

    def change_rating(self, value):
        new_rating = self.rating + value
        new_rating = min(max(new_rating, 1), 100)
        if new_rating > self.rating:  # если рейтинг вырос
            self.age -= abs(value)//10  # уменьшаем возраст
            self.age = max(self.age, 18)
        elif new_rating < self.rating:  # если рейтинг упал
            self.age += abs(value)//10  # увеличиваем возраст

        self.rating = new_rating  # обновляем рейтинг

    def __iadd__(self, string):
        value = len(string)
        self.change_rating(value)
        return self

    def __call__(self, number):
        return (number - self.age)*self.rating

    def __str__(self):
        return f'Wizard {self.name} with {self.rating} rating looks ' \
               f'{self.age} years old'

    def __lt__(self, other):
        return (
            (self.rating, self.age, self.name) <
            (other.rating, other.age, other.name)
        )

    def __gt__(self, other):
        return (
            (self.rating, self.age, self.name) >
            (other.rating, other.age, other.name)
        )

    def __le__(self, other):
        return (
            (self.rating, self.age, self.name) <=
            (other.rating, other.age, other.name)
        )

    def __ge__(self, other):
        return (
            (self.rating, self.age, self.name) >=
            (other.rating, other.age, other.name)
        )

    def __eq__(self, other):
        return (
            (self.rating, self.age, self.name) ==
            (other.rating, other.age, other.name)
        )

    def __ne__(self, other):
        return (
            (self.rating, self.age, self.name) !=
            (other.rating, other.age, other.name)
        )


if __name__ == "__main__":
    print('Пример 1')
    wd = Wizard('Haw1', 75, 27)
    print(wd)
    wd.change_rating(23)
    wd += 'great magician'
    print(wd)
    print(wd(42))

    print()

    print('Пример 2')
    wd = Wizard('Haw1', 75, 27)
    wd1 = Wizard('Saliman', 75, 27)
    print(wd > wd1)
    wd.change_rating(-1)
    print(wd < wd1)
    print(wd, wd1, sep='\n')
