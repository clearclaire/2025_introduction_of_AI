
number_1 = int(input("구구단 몇단을 계산할까요?"))
print(f"구구단 {number_1} 단을 계산합니다.")
for i in range(1, 10):
    number_2 = i * number_1
    # print(f"{number_1} X {i} = {number_1 * i}")
    print(f"{number_1} X {i} = {number_2}")