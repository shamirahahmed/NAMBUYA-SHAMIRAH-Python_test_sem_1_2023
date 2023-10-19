#1
#snake case- StudentsMarks
#camel case-total_average_mark

#ii, convert the variable age=22 to a float value,print its new data type 
age = 22
age_as_float = float(age)
print(type(age_as_float))

                                                  #2
def average(x, y):
    return (x + y) / 2


num1 = 30
num2 = 40

average = average(num1, num2)
print(f"The average of {num1} and {num2} is {average}")

# ii,

num1 = float(input(" 15.3:"))
num2 = float(input(" 4.4: "))
num3 = float(input(" 2.8: "))

minimum = min(num1, num2, num3)

print(f"The minimum number among {num1}, {num2}, and {num3} is {min}")


                                                          #3
student_marks = [78, 83, 90, 88, 75]

total_marks = sum(student_marks)

print(f"The sum of items in the student marks list is {total_marks}.")

# ii,
student_marks = [78, 83, 90, 88, 75]

first_mark = student_marks[0]
print(f"The first mark is: {first_mark}")

last_mark = student_marks[-1]
print(f"The last mark is: {last_mark}")

# iii,

student_marks.append(96)

print("Updated list of student marks:", student_marks)

#iv,


