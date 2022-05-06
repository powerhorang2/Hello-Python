def total(a, b=5, c=10):
    print(a + b + c)

total(1)
total(1, 2)
total(1, 2, 3)
# total(b=2, c=3) # 기본값을 설정하지 않은 매개변수에 인수를 전달하지 않음 -> TypeError
# total(1, 2, 3, 4) # 매개변수의 수보다 더 많은 인수를 전달함 -> TypeError