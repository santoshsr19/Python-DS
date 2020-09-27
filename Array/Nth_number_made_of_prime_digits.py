def nthprimedig(n):
    a={1:'2',2:'3',3:'5',4:'7'}
    b= ""
    while(n>0):
        k=n%4
        if (k==1):
            b +='2'
        if (k==2):
            b +='3'
        if (k==3):
            b +='5'
        if (k==0):
            b +='7'  
        if (n%4==0):
            n=n-1
        n=n//4
    print(b[::-1])
        
t=int(input())
for _ in range(t):
    n=int(input())
    nthprimedig(n)


"""
Given a number 'N'. The task is to find the Nth number whose each digit is a prime number i.e 2, 3, 5, 7. In other words, you have to find the nth number of this sequence: 2, 3, 5, 7, 22, 23,.. and so on.

Input:
The first line contains a single integer T i.e. the number of test cases. The first and only line of each test case consists of an integer N. 

Output: 
In one line print the nth number of the given sequence made of prime digits.

Expected Auxiliary Space: O(N).

Constraints:
1 <= T <= 100
1 <= N <= 100

Examples:
Input:
2
10
21
Output:
33
222
"""