data = {}
while(True):
    print("1.Enter the Question:-")
    print("2.Enter the Answer:-")
    print("3.Exit")
    user_choice = input("What is your choice ? :-")
    if int(user_choice) == 1: 
        question = input('Enter the Question: ')
        data["question"] = question
        Option_1 = input("Enter the Option A:")
        data["A"] = Option_1
        Option_2 = input("Enter the Option B:")
        data["B"] = Option_2
        Option_3 = input("Enter the Option C:")
        data["C"] = Option_3
        Option_4 = input("Enter the Option D:")
        data["D"] = Option_4
        ans = input("Enter the Answer:")
        data["ans"] = ans

    elif int(user_choice) == 2:
        print("Question :-")
        print(data["question"])
        print("Option :-")
        print('A :',data['A'],'\t\tB :',data['B'])
        print('C :',data['C'],'\t\tD :',data['D'])

        user_ans = input("Enter your ans: ")
        if user_ans==data['ans']:
            print("Anser is True")
        else:
            print("Anwer is False")
    elif int(user_choice) == 3:
        break
    else:
        print("Invalid Input")



