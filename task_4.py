#List

# num_1 = '100'
# num_2 = '200'

# num_1 = int(num_1)
# num_2 = int(num_2)
# print(num_1 + num_2)

# list_1 = ['history', 'math', 'physics', 'comsci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'art'

# print(list_1)
# print(list_2)

# print(courses.index('comsci'))  

# for index, course in  enumerate (courses, start=1):
#     print(index, course)

# course_str = ' - '.join(courses)

# new_list = course_str.split(' - ')
# print(course_str)



# nums = [1, 5, 3, 2, 4]
# sorted_courses = sorted(courses)
# # print(sorted_courses)
# # print(min(nums))
# # print(max(nums))
# print(sum(nums))



# courses_2 = ['art', 'education']
# courses.remove('math')
# courses.extend(courses_2)
# courses.reverse()
# courses.sort(reverse=True)
# num.sort(reverse=True)
#print(num)
# # print(len(courses))
# print(courses[0:2])
# print(courses[1])
# print(courses[:2])
# print(courses[2:])


#Tuple

# tuple_1 = ('history', 'math', 'physics', 'comsci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'art'

# print(tuple_1)
# print(tuple_2)

# Sets
# cs_courses = {'history', 'math', 'physics', 'comsci'}
# art_courses = {'history', 'math', 'art', 'design'}

# # print(cs_courses.intersection(art_courses))
# # print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))

# Empty Lists
# empty_list = []
# empty_list = list()

# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()

# # Empty Sets
# empty_set = {}
# empty_set = set()



#dictionaries

student = {'name': 'jagdish', 'age': 21, 'courses': ['math', 'compsci']}
# print(student)
# print(student['name'])
# print(student['age'])
# student['phone'] = '555-5555'
# student['name'] = 'jay'
# print(student.get('phone', 'not found'))
#student.update({'name': 'jay', 'age': '22', 'phone': '1234567890'})
# del student['age']
# age = student.pop('age')
#print(len(student))

for key, value in student.items():    
    print(key, value)