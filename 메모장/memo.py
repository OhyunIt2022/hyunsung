print("hello world")
print("진행할 작업을 선택해주세요")
print("1.메모작성 2.메모읽기")

option = input()

print(option)

if option == "1":
    print("아직 구현안함")
elif option == "2":
    f=open('memo.txt')
    print(type(f))
    memo=f.read()
    print(memo)
    f.close()
else:
    ("잘못임력하였습니다") 

