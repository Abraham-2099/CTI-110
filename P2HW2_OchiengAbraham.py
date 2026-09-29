#Abraham Ochieng
#9/29/2026
#P2HW2
#test grades

#prompt for grades

grade1 = float(input("Enter grade for module 1: "))
grade2 = float(input("Enter grade for module 2: "))
grade3 = float(input("Enter grade for module 3: "))
grade4 = float(input("Enter grade for module 4: "))
grade5 = float(input("Enter grade for module 5: "))
grade6 = float(input("Enter grade for module 6: "))

#store grades in a list
grades = [grade1, grade2, grade3, grade4, grade5, grade6]

#calculate required results 
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

#display results
print("\n------------results------------")
print(f'{"Lowest grade:":<20} {lowest_grade:<20.1f}')
print(f'{"Highest grade:":<20} {highest_grade:<20.1f}')
print(f'{"Sum of grades:":<20} {sum_of_grades:<20.1f}')
print(f'{"Average grade:":<20} {average_grade:<20.2f}')
print("----------------------------------------")