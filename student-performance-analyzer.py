def calculate_total(marks):
    return sum(marks)
def calculate_average(marks):
    return sum(marks) / len(marks) 
def display_result(name,marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = max(marks)
    lowest = min(marks)

    if average>=40:
        result = "Pass"
    else:   
        result = "Fail"

    print("\n======student performance======")
    print(f"Name: {name}")
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Result: {result}")
print("\n======student performance report======")
name=input("enter student name: ")
subjects=int(input("total no. of subjects: "))
marks=[]
for i in range(subjects):
    mark=float(input(f"enter marks for subject {i+1}: "))
    marks.append(mark)
display_result(name, marks)