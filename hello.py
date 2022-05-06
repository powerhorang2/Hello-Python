def add(*params):  # * 한개
    print(params)
    total = 0
    for param in params:
        total += param
    return total


print(add(10))
print(add(10, 100))
print(add(10, 100, 1000))


def print_map(**dicts):  # ** 두개
    for item in dicts.items():
        print(item)


print_map(하나=1)
print_map(one=1, two=2)
print_map(하나=1, 둘=2, 셋=3)