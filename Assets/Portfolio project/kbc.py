que = ["1+1", "2+2", "3+3", "4+4", "5+5"]
ans = [2,4,6,8,10]
prize = [10, 100, 1000, 10000, 100000 ]
name = input("Enter your name : ")
print("Welcome to Sasta KBC " , name, "ji")
ready = input("are you ready \n (yes/no) : ")
if ready == "yes":
    print("Get ready for questions")
    # q1
    c_quession = 0
    c_prize = prize[c_quession]
    
    while c_quession < len(que):
        print(f"What is {c_quession +1}: {que[c_quession]}")
        c_ans = int(input("Enter Your answer :"))
        if (c_ans == ans[c_quession]):
            print("correct answer \n You win : %d " % c_prize)
            c_quession = c_quession +1
            c_prize = prize[c_quession]
        else:
            print("wrong Answer \n game over")
            break
else:
    print("GO anyway")

