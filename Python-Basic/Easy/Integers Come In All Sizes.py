Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is:  2^31-1(c++ int) or  2^63-1(C++ long long int).

As we know, the result of a^b grows really fast with increasing b.

Let's do some calculations on very large integers.

Task
Read four numbers a, b, c, and d print the result of a^b + c^d.

Input Format
Integers a, b, c, and d  are given on four separate lines, respectively.

Output Format
Print the result of a^b + c^d on one line.

Sample Input

9
29
7
27
Sample Output

4710194409608608369201743232  

code:
# Enter your code here. Read input from STDIN. Print output to STDOUT
a_value,b_value,c_value,d_value = [int(input()) for _ in '1234']
print(pow(a_value,b_value)+pow(c_value,d_value))
