n = input("enter your task 1 add 2.view 3.delete 4.exit : ")
task = []
res = []
k, h = [], []

while True:
    ch = input("1.add 2.view 3.delete 4 restore 5.exit: ")
    if ch == '1':
        add = input("ENTER YOUR TASK: ")
        task.append(add)
        print("TASKED IS ADDED!!")
    elif ch == '2':
        print(task)
    elif ch == '3':
        o = int(input("ENTER WHICH TASK U WANT TO DELETE: "))
        k = task.pop(o)
        res.append(k)
        print("TASK HAS BEEN DELETED !!")
    elif ch == '4':
        h = res.pop()
        task.append(h)
        print("THE RESTORE!! ", h)


    elif ch == '5':
        print("EXITED!!")
        break

    else:
        print("INVALID ERROR")