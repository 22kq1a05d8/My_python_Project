#task management
#admin section
#user section
task_list=['Buy groceries','Pending','Complete assignment','In progress','Read book','Completed']
user_list=['Admin','User1','User2']
completed_list=[]
while True:
    print('\n=====TASK MANAGEMENT SYSTEM ======')
    print('1.Admin')
    print('2.User')
    print('3.Exit')
    role=input('select role:')
    if role=='1':
        print('\n=====ADMIN SECTION=====')
        print('1.Add Task')
        print('2.Update Task')
        print('3.Delete Task')
        print('4.View all Tasks')
        print('5.View Users')
        print('6.Exit')
        while True:
            ch=input('what do you want(yes/no):')
            if ch=='yes':
                ch=input('what do you want:')
                if ch=='1':
                    task=input('Enter new task:')
                    task_list.append(task)
                    print(task,'is added')
                elif ch=='2':
                    print(task_list)
                    task=input('which task do you want to update:')
                    if task in task_list:
                        idx=task_list.index(task)
                        new_task=input('enter new task:')
                        task_list[idx]=new_task
                        print('Task is updated')
                    else:
                        print('task is not available')
                elif ch=='3':
                    print(task_list)
                    task=input('which task do you want to delete:')
                    if task in task_list:
                        idx=task_list.index(task)
                        task_list.pop(idx)
                        print(task,'is deleted')
                    else:
                        print('Task is not available')
                elif ch=='4':
                    print('All task:')
                    for task in task_list:
                        print(task)
                elif ch=='5':
                    print('Users:')
                    for user in user_list:
                        print(user)
                elif ch=='6':
                    print('Exiting Admin section')
                    break
                else:
                    print('Invalid choice')
            else:
                break
    elif role=='2':
        while True:
            print('\n======USER SECTION======')
            print('1.View my Tasks')
            print('2.Add Task')
            print('3.Update my task')
            print('4.Delete my task')
            print('5.Mark Task Complete')
            print('6.Exit')
            ch=input('what do you want:')
            if ch=='1':
                print('\nMy Tasks:')
                for task in task_list:
                    print(task)
            elif ch=='2':
                task=input('enter new task:')
                task_list.append(task)
                print(task,'is added to my task list')
            elif ch=='3':
                print(task_list)
                task=input('which task do you want to update:')
                if task in task_list:
                    idx=task_list.index(task)
                    new_task=input('enter new task:')
                    task_list[idx]=new_task
                    print('Task is updated')
                else:
                    print('Task is not available')
            elif ch=='4':
                print(task_list)
                task=input('which task do you want to delete:')
                if task in task_list:
                    idx=task_list.index(task)
                    
                    task_list.pop(idx)
                    print(task,'is deleted')
                else:
                    print('Task is not available')
            elif ch=='5':
                print(task_list)
                task=input('which task is completed:')
                if task in task_list:
                    idx=task_list.index(task)
                    completed_list.append(task)
                   
                    task_list.pop(idx)
                    print(task ,'is completed')
                else:
                    print('Task is not available')
            elif ch=='6':
                print('Exiting User section')
                break
            else:
                print('Invalid choice')
    elif role=='3':
        print('! Thank you')
        break
    else:
        print('Invalid role')
    
