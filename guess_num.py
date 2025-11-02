import random

ans_num = random.randint(1, 100)
print("숫자를 맞춰보세요 (1~100)")
user_num = 99999
#선언이 되지 않으면 그냥 임의의 값을 선언하고 시작

while user_num != ans_num:
    user_num = int(input())
    if user_num < ans_num:
        print(f"{user_num} : 숫자가 정답보다 작습니다.")
    elif user_num > ans_num:
        print(f"{user_num} : 숫자가 정답보다 큽니다.")
    else:
        break

print (f"정답입니다. 정답은 {user_num} 입니다.")


# if user_num < ans_num:
#     print(f"{user_num} : 숫자가 정답보다 작습니다.")
# elif user_num > ans_num:
#     print(f"{user_num} : 숫자가 정답보다 큽니다.")
# elif user_num == ans_num:
#     print(f"{user_num} : 정답입니다.")
# else:
#     print("error : 관리자에게 문의하세요")