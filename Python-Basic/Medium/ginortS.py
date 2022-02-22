You are given a string S.
S contains alphanumeric characters only.

Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string S.

Output Format

Output the sorted string S.

Sample Input

Sorting1234
Sample Output

ginortS1324

Code:
# Enter your code here. Read input from STDIN. Print output to STDOUT
string = input()
uppercase_string = []
lowercase_string = []
digits = []
odd = []
even = []

for character in range(len(string)):
    if string[character].isupper():
        uppercase_string.append(string[character])
    elif string[character].islower():
        lowercase_string.append(string[character])
    elif string[character].isnumeric:
        digits.append((string[character]))

for value in digits:
    if int(value)%2 ==0:
        even.append(value)
    else:
        odd.append(value)
print("".join((sorted(lowercase_string)+ sorted(uppercase_string)+ sorted(odd) + sorted(even))))
        
