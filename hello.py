def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print("0으로 나누면 안돼요!", e)
    except:  # 에러명이나 as 를 입력하지 않으면 모든 에러를 체크함
        print("에러 발생!")
    # else: # 에러가 발생하지 않았을 때 실행 될 코드
    # finally: # 무조건 실행 될 코드


divide(3, 0)

# raise NotImplementedError # 에러 발생시키기 (raise 문) - 발생시킨 에러는 필수 구현 사항을 구현하지 않았을 때 발생하는 에러
