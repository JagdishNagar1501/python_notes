dict_var = {"Question_1": "1.What is 25+25.", "Option_1": ['a:', 20 ,'b:', 30 ,'c:', 40 ,'d:', 50] ,"Ans": 50,
"Question_2": "2.What is 50+50.", "Option_2": ['a:', 100 ,'b:', 90 ,'c:', 80 ,'d:', 50] ,"Ans": 100}
print(dict_var)


print("Question !!!")
print("---------------------------------------------")
a = dict_var["Question_1"]
print(a)

# a = dict_var["Option"]
# print(a)

# a = dict_var.keys()
# print(a)

# a = dict_var.values()
# print(b)

opt = dict_var["Option_1"]
print(opt[0], opt[1])
print(opt[2], opt[3])
print(opt[4], opt[5])
print(opt[6], opt[7])

ans = dict_var["Ans"]
print("Answer is:",ans)

b = dict_var["Question_2"]
print(b)

opt = dict_var["Option_2"]
print(opt[0], opt[1])
print(opt[2], opt[3])
print(opt[4], opt[5])
print(opt[6], opt[7])

ans = dict_var["Ans"]
print("Answer is:",ans)


# list = ["apple", "banana", "cherry"]
# print(list[:2])


dict_var = [
    {"Question": "1.What is 25+25.", 
    "Option": ['a:', 20 ,'b:', 30 ,'c:', 40 ,'d:', 50], 
    "Ans": "D" },
    {"Question": "2.What is 50+50.", 
     "Option": ['a:', 100 ,'b:', 90 ,'c:', 80 ,'d:', 50], 
     "Ans": "A"}
     ]

for i in range(len(dict_var)):
  print(dict_var[i])

print("Question !!!")
print("---------------------------------------------")
a = dict_var
for dt in dict_var:
    a = dt["Question"]
    print(a)

    opt = dt["Option"]
    print(opt[0], opt[1])
    print(opt[2], opt[3])
    print(opt[4], opt[5])
    print(opt[6], opt[7])

    user_ans = input("Enter your ans: ")
    ans = dt["Ans"]
    print(f"Answer is: {ans} and your ans: {user_ans}")
