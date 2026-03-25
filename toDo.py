task = []
# task 등록
while True:
    print(f"1. 등록   2. 수정   3. 조회   4. 삭제")

    sel = input()
    if sel == "1":
        new = input()
        task.append(new)
    elif sel == "2":
        num = int(input())
        task[num-1] = input()
    elif sel == "3":
        for i in task:
            print(f"{i}")
    elif sel == "4":
        task.remove(task[int(input())-1])
    elif sel.lower() == "q":
        break