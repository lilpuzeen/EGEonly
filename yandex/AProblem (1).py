class Wizard:

    def __init__(self, Name: str, Rating: int, Age: int) -> None:
        self.Name = Name
        self.Rating = Rating
        self.Age = Age

    def __Age_smooth_out(self, _value: int) -> int:

        Age_difference = _value // 10
        Age_estimated = self.Age + Age_difference

        #  Limit checking by Age
        if Age_estimated < 18:
            Age_difference = self.Age - 18

        return -Age_difference

    def __Rating_smooth_out(self, _value: int) -> int:

        Rating_difference = _value
        Rating_estimated = self.Rating + Rating_difference

        #  Limit checking by Rating
        if Rating_estimated > 100:
            Rating_difference = 100 - self.Rating

        if Rating_estimated < 1:
            Rating_difference = self.Rating

        return Rating_difference

    def change_rating(self, value: int) -> None:
        self.Rating += self.__Rating_smooth_out(value)
        self.Age += self.__Age_smooth_out(value)
        return

    def __iadd__(self, String: str):
        value = len(String)
        self.Rating += self.__Rating_smooth_out(value)
        self.Age += self.__Age_smooth_out(value)
        return self

    def __call__(self, number):
        return (number - self.Age) * self.Rating

    def __str__(self):
        return f"Wizard {self.Name} with {self.Rating} rating looks {self.Age} years old"

    def __eq__(self, other):
        if self.Rating == other.rating:
            if self.Age == other.age:
                if self.Name[0] == other.name[0]:
                    return True
        return False

    def __lt__(self, other):
        if self.Rating < other.rating:
            return True
        elif self.Rating == other.rating:
            if self.Age < other.age:
                return True
            elif self.Age == other.age:
                if self.Name[0] < other.name[0]:
                    return True
        return False

    def __le__(self, other):
        if self.Rating <= other.rating:
            return True
        elif self.Rating == other.rating:
            if self.Age <= other.age:
                return True
            elif self.Age == other.age:
                if self.Name[0] <= other.name[0]:
                    return True
        return False

    def __ne__(self, other):
        if self.Rating != other.rating:
            return True
        elif self.Rating == other.rating:
            if self.Age != other.age:
                return True
            elif self.Age == other.age:
                if self.Name[0] != other.name[0]:
                    return True
        return False

    def __gt__(self, other):
        if self.Rating > other.rating:
            return True
        elif self.Rating == other.rating:
            if self.Age > other.age:
                return True
            elif self.Age == other.age:
                if self.Name[0] > other.name[0]:
                    return True
        return False

    def __ge__(self, other):
        if self.Rating >= other.rating:
            return True
        elif self.Rating == other.rating:
            if self.Age >= other.age:
                return True
            elif self.Age == other.age:
                if self.Name[0] >= other.name[0]:
                    return True
        return False
    # def __gt__(self, other):
    #     if self.Rating > other.Rating:
    #         return True
    #     elif self.Rating == other.Rating:
    #         if self.Age > other.Age:
    #             return True
    #         elif self.Age == other.Age:
    #             for x in range(len(min(self.Name, other.Name))):
