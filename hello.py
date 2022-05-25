n, k = map(int, input().split())

result = 0

while True:
    # n 이 1이 되면 종료
    if n == 1:
        break
    # n 이 k 로 나누어 떨어질 때
    if n % k == 0:
        n //= k
        result += 1
    # 나머지가 존재하면 나머지 만큼 n에서 빼기
    else:
        remainder = n % k  # 나머지 구함

        # 만약 나눗셈의 몫이 0이면 나머지에 -1 한만큼 횟수 더해줌
        if n // k == 0:
            result += (remainder - 1)
            break
        n -= remainder
        result += remainder

print('result: ', result)
