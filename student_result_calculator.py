name = input("Enter Student Name: ")

sub1 = int(input("English Marks: "))
sub2 = int(input("Math Marks: "))
sub3 = int(input("Science Marks: "))
sub4 = int(input("Social Marks: "))
sub5 = int(input("Computer Marks: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
