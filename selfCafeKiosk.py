bank = 5000
menus = [
    [1, "ame", "아메리카노", 3000],
    [2, "rat", "카페라떼", 3500],
    [3, "cino", "카푸치노", 4000]
]
# 메뉴 출력
for m in menus:
    print(f"{m[0]}. {m[2]} {m[3]}원")
# 메뉴 입력
cho = input("주문할 번호 : ")

# 메뉴 저장
for m in menus:
    if cho == str(m[0]):
        print(f"{m[2]}를 선택하셨습니다.")
        print(f"결제금액은 {m[3]}원 입니다.")
        break
# 결제
print("결제중입니다.")
bank -= menus[int(cho)-1][3]
print(f"잔액 : {bank}")