Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores.Store them in a list and find the score of the runner-up.

Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints
2<=n<=10
-100<=A[]<=100

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5

Code: 
  
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    new_array=[]
    [new_array.append(values) for values in arr if values not in new_array]
    new_array.sort()
print(new_array[-2])

Time complexity of the code: 
  List comprehension: n*n = n <sup>2</sup>
