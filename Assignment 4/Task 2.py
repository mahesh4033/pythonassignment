with open("output.txt", "w") as f:
        input1 = input("Enter text to write to the file: ")
        f.write(input1 + "\n")

        input2=input("Enter additional text to write to file: ")
        f.write(input2 + "\n")
    
opened_file = open("output.txt", "r")
print("final content of output.txt:")
for line in opened_file:
    print(line.strip())

    