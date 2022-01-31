Let's learn about list comprehensions! You are given three integers x,y,z representing the dimensions of a cuboid along with an integer n.Print a list of all possible 
coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to . Here, 0<=i<=x; 0<=j<=y; 0<=k<=z. Please use list comprehensions rather than multiple loops, 
as a learning exercise.

Example
x=1
y=1
z=2
n=3

All permutations of [i,j,k] are,
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]

Input Format
Four integers x,y,z and n each on a separate line.

Constraints
Print the list in lexicographic increasing order.

Sample Input 0
1
1
1
2

Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Sample Input 1
2
2
2
2

Sample Output 1
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

Code:
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    list_comprehensions = [[elements,elements_1,elements_2] for elements in range(0,x+1) for elements_1 in range(0,y+1) for elements_2 in range(0,z+1) if (elements+elements_1+elements_2)!=n]
    print(list_comprehensions)
