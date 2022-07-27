print("hello world")
print("진행할 작업을 선택해주세요")
print("1.메모작성 2.메모읽기")

option = input()

print(option)

if option == "1":
    newmemo=input("메모를 입력해주세요\n")
    print(newmemo)
    filename='memo.txt'
    f=open(filename,'a')
    f.write(newmemo)
    f.close()
elif option == "2":
    filename='memo2.txt'
    f=open(filename)
    print(type(f))
    memo=f.read()
    print(memo)
    f.close()
else:
    ("잘못임력하였습니다") 

