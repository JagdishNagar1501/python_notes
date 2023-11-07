#Dictionaries Programming

ques_dict = {'Question': 'What is 12+12 = ?',
         'A': '25', 'B': '24', 'C': '23', 'D': '22',
         'ans': 'B'}
print("Question :-")
print(ques_dict['Question'])

print("Option :-")
print('A :',ques_dict['A'],'\t\tB :',ques_dict['B'])
# print('B :', dict['B'])
print('C :',ques_dict['C'],'\t\tD :',ques_dict['D'])
# print('D :', dict['D'])

user_ans = input("Enter your ans: ")
if user_ans==ques_dict['ans']:
    # print(f"Answer is: {user_ans}")
    # print(f"Answer is: {ques_dict}")
    print("Anser is True")
else:
    print("Anwer is False")
