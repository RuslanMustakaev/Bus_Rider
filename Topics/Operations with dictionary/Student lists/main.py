import operator

#  student_list = {'key': [5, 6, 7], 'interesting': [0, 2], 'what': [5, 6, 8, 9, 10, 50]}

sorted_student_list = sorted(student_list.items(), key=operator.itemgetter(1))
print(sorted_student_list[0][0])
