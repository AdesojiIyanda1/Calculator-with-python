# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# results = int(num1) + int(num2)
# print(results)
# # int is used for a whole number while float is used for decimals
# users should create 3 sets and find the;1 intersection
# Union 
# symmetric difference 
# difference 

# SOLUTION TO SETS

# Set1 = input(())
# Set2 = input(())
# Set3 = input(())
# for i = Set1.intersection(Set2).intersection(Set3) or u == Set1.union(Set2).union(Set3)
# print(i)


# intercept = Set1.intersection(Set2).intersection(Set3)
# print(intercept)
# Unions = Set1.union(Set2).union(Set3)
# print(Unions)
# Symmetric_Diff = Set1.symmetric_difference(Set2).symmetric_difference(Set3)
# print(Symmetric_Diff)
# Difference = Set1.difference(Set2).difference(Set3)
# print(Difference)


# CORRECTION

# set1 = set(input("supply 5 values"))
# set2 = set(input("supply 5 values"))
# set3 = set(input("supply 5 values"))
# print("""press:
# 1. union
# 2. intersection
# 3. symmetric difference
# 4. difference

# 5. union2 = set1 | set2 or set1 | set3 or or set2 | set3

# """)
# response = input(">>>")
# if response == "1":
#     output = set1.union(set2).union(set3)
#     print(output)
# elif response == "2":
#     output = set1.intersection(set2).intersection(set3)
#     print(output)
# elif response == "3":
#     output = set1.symmetric_difference(set2).symmetric_difference(set3)
#     print(output)
# elif response == "4":
#     output = set1.difference(set2).difference(set3)
#     print(output)
# else:
#     response == "5"
#     output = set1.union(set2) or set1.union(3) or set2.union(set3)
#     print(output)

set1 = set(input("supply 5 values"))
set2 = set(input("supply 5 values"))
set3 = set(input("supply 5 values"))
print("""press:
1. union
2. intersection
3. symmetric difference
4. difference
5. union2 = set1.union(set2)
""")
response = input(">>>")
if response == "1":
    output = set1.union(set2).union(set3)
    print(output)
elif response == "2":
    output = set1.intersection(set2).intersection(set3)
    print(output)
elif response == "3":
    output = set1.symmetric_difference(set2).symmetric_difference(set3)
    print(output)
elif response == "4":
    output = set1.difference(set2).difference(set3)
    print(output)
else:
    response == "5"
    output = set1.union(set2) or set1.union(3) or set2.union(set3)
    print(output)``