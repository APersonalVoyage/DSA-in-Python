# Big O : O(2n)
def print_items(n):
    for i in range(n):
        print(i)
        
    for j in range(n):
        print(j)    

print_items(10)    

# Big O: O(n^2)
def print_items(n):
    for i in range(n):
        #print(i)
        for j in range(n):
            print(i,j)    

print_items(10)

'''
 O(n^2): Loop within a Loop, O(n): Proportional, O(log n): Divide and conquer, O(1): 
Constant where n being the number of operations. 
'''

