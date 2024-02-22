class shapes:
    def __init__(self,numbers,target) -> None:
        self.numbers = numbers
        self.target =target

    def sum(self):
        print(self.numbers + self.target)


class Awesome (shapes):
    def display(self):
        print("Numbers: ", self.numbers, "Target: ", self.target)
        print("Sum: ", self.numbers + self.target)

if __name__ == "__main__":
    s = shapes(3,4)
    s.sum()

    leta = Awesome(0,4)
    leta.display()
    leta.sum()
