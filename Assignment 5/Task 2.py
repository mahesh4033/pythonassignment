list1=[1,2,3,4,5,6,7,8,9,10]

#first 5 numbers
first_5=list1[:5]
print(f"First 5 numbers are: {first_5}")


remaining_list=list1[5:]
#print(f"Remaining numbers are: {remaining_list}")


reversed_list=remaining_list[::-1]
print(f"Reversed extracted elements: {reversed_list}")