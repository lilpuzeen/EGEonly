class Wizard:
    def __init__(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age

    def change_rating(self, value):
        if value < 0:
            self.rating += value
            self.age += abs(value)
        else:
            self.rating += value
            self.age -= abs(value) // 10
        if self.age < 18:
            self.age = 18

    def __add__(self, other):
        self.rating = self.rating + len(other)
        if self.rating > 100:
            self.rating = 100
        self.age -= len(other) // 10
        if self.age < 18:
            self.age = 18
        print(self.rating)
        print(self.age)

    def __call__(self, value):
        return (value - self.age) * self.rating

    def __eq__(self, other):
        if self.rating == other.rating:
            if self.age == other.age:
                if self.name[0] == other.name[0]:
                    return True
        return False

    def __lt__(self, other):
        if self.rating < other.rating:
            return True
        elif self.rating == other.rating:
            if self.age < other.age:
                return True
            elif self.age == other.age:
                if self.name[0] < other.name[0]:
                    return True
        return False

    def __le__(self, other):
        if self.rating <= other.rating:
            return True
        elif self.rating == other.rating:
            if self.age <= other.age:
                return True
            elif self.age == other.age:
                if self.name[0] <= other.name[0]:
                    return True
        return False

    def __ne__(self, other):
        if self.rating != other.rating:
            return True
        elif self.rating == other.rating:
            if self.age != other.age:
                return True
            elif self.age == other.age:
                if self.name[0] != other.name[0]:
                    return True
        return False

    def __gt__(self, other):
        if self.rating > other.rating:
            return True
        elif self.rating == other.rating:
            if self.age > other.age:
                return True
            elif self.age == other.age:
                if self.name[0] > other.name[0]:
                    return True
        return False

    def __ge__(self, other):
        if self.rating >= other.rating:
            return True
        elif self.rating == other.rating:
            if self.age >= other.age:
                return True
            elif self.age == other.age:
                if self.name[0] >= other.name[0]:
                    return True
        return False

    def __str__(self):
        print(1)
        return 'Wizard ' + str(self.name) + ' with ' + str(self.rating) + ' rating looks ' + str(self.age)\
               + ' years old'


wd = Wizard("Hawl", 75, 27)
print(type(wd))
wd += "great magician"
print(type(wd))
print(wd)