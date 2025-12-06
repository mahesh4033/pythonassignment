try:
    with open("sample.txt", "r") as t:
        line1=t.readline().strip()
        line2=t.readline().strip()
        print("Reading file content:")
        print(f"Line 1: line1")
        print(f"Line 2: line2")
except FileNotFoundError:
    print("Error:The File 'sample.txt' not found.")