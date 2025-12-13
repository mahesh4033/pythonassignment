
students = {
    "rahul": {"name": "Rahul", "age": 20, "mark": 92},
    "neha": {"name": "Neha", "age": 21, "mark": 94},
    "arjun": {"name": "Arjun", "age": 19, "mark": 98}
    }

input1=input("Enter the student's name: ")
try:
    mark=students[input1]["mark"]
    print(f"{input1}'s marks:{mark}")
except KeyError:
    print("Student not found.")