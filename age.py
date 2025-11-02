current_year = 2025
birth_year = int(input("당신이 태어난 년도를 입력하세요"))
current_age = current_year - birth_year + 1

# 아래 조건보다는 20 <= current_age and current_age <= 26 를 써라!!
if 20 <= current_age <= 26:
    print("대학생")
elif 17 <= current_age < 20:
    print("고등학생")
elif 14 <= current_age < 17:
    print("중학생")
elif 8 <= current_age < 14:
    print("초등학생")
else:
    print("학생이 아닙니다")
