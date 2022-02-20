class Wizard:
    def __init__(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age

    def change_rating(self, other):
        new_rating = self.rating + other
        new_rating = min(max(new_rating, 1), 100)
        if new_rating > self.rating:
            self.age -= abs(other) // 10
            self.age = max(self.age, 18)
        elif new_rating < self.rating:
            self.age += abs(other) // 10

        self.rating = new_rating

    def __iadd__(self, other):
        value = len(other)
        self.change_rating(value)
        return self

    def __call__(self, arg):
        return (arg - self.age) * self.rating

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
