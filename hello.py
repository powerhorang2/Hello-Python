class Alphabets:
    __str = ""

    def __init__(self, text):
        self.text = text

        Alphabets.__str += text

    def print_class_variable(self):
        print(Alphabets.__str)


if __name__ == '__main__':
    o1 = Alphabets('p')

    o2 = Alphabets('y')

    o3 = Alphabets('t')

    o4 = Alphabets('h')

    o5 = Alphabets('o')

    o6 = Alphabets('n')

    print(o1.text)
    print(o2.text)
    print(o3.text)
    print(o4.text)
    print(o5.text)
    print(o6.text)

    o1.print_class_variable()

    o5.print_class_variable()

