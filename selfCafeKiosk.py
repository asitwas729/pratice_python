bank = 5000
ame = [1, "아메리카노", 3000]
rat = [2, "카페라떼", 3500]
cino = [3, "카푸치노", 4000]
# 메뉴 출력
print("1. ", ame[1])
print("2. ", rat[1])
print("3. ", cino[1])
# 메뉴 입력
cho = input()

# 메뉴 저장
if(cho == "1"):
    menu = ame
    print("아메리카노 3000원")
elif(cho == "2"):
    print("카페라떼 3500원")
elif(cho == "3"):
    print("카푸치노 4000원")
else :
    print("Error")
# 결제
print("결제중입니다.")
bank -= menu[2]
print("남은 돈 : ", bank)