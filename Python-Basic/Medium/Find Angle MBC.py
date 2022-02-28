Input Format

The first line contains the length of side AB.
The second line contains the length of side BC.

Output Format

Output LMBC in degrees.

Note: Round the angle to the nearest integer.
  
Sample Input

10
10
Sample Output

45°

Code:
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB_length = int(input())
BC_length = int(input())

print(round(math.degrees(math.atan(AB_length/BC_length))),chr(176),sep="")
