print("Task you have on todo list 1 add 2.view 3.delete 4.restore,5.exit ")
task = [] #All the task will be stored here 
res = []# res is used to restore the deleted ones
k, h = [], []# Temporary lists to assist with restoring deleted tasks

while True:# It runs till the condition is False when ch==5 
    ch = input("1.add 2.view 3.delete 4 restore 5.exit: ")# It is the input statement Where we have to choose the Numbers from 1 to 5
    if ch == '1':# If we choose 1 as the input we can add the task in our todo list
        add = input("ENTER YOUR TASK: ")#This is the input for our task
        task.append(add)#THIS is stored in task list because multiple tasks can be added
        print("TASKED IS ADDED!!")
    elif ch == '2':
        print(task)# If it is 2 It will show all the task 
    elif ch == '3':
        o = int(input("ENTER WHICH TASK U WANT TO DELETE: "))# if we choose 3 it is used to delete the elements o is the imput to delete the elements
        k = task.pop(o)# In the task list the input number of o will be popped out of the list and stored in k variable
        res.append(k)# Store the deleted task in res list for possible restore later
        print("TASK HAS BEEN DELETED !!")
    elif ch == '4':
        h = res.pop()# res will pop the last values and that are stored in h variable
        task.append(h)#  Add the restored task back to the main task list
        print("THE RESTORE!! ", h)


    elif ch == '5':
        print("EXITED!!")# If user selects 5, show exit message and break the loop
        break

    else:

        print("INVALID ERROR") #If user enters an invalid choice, show error message
