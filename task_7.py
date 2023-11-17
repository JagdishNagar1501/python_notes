student = [{"student_name": "jagdish",
              "student_class": 5,
              "student_roll-no": 15},
              {"student_name": "nagar",
               "student_class": 6,
               "student_roll-no": 16}]
for std in student:
    # print(std)
    print(std["student_name"])
    print(std["student_class"])


student_data = []
for std in range(0,2):
    student_info = {}    

    a = input("What is student name:-")
    student_info["student_name"] = a
    b = input("What is student class:-")
    student_info["student_class"] = b
    c = input("What is student roll-no:-")
    student_info["student_roll-no"] = c
    print(student_info)
    student_data.append(student_info)

print(student_data)
