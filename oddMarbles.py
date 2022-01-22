
# TODO: PROBLEM SOLVING find the odd one from 9 Marbles

"""
1) You have 9 marbles.

2) 8 of them are exactly the same weight. The remaining marble is slightly heavier/lighter than the others. 
You don’t know which is which.

3) You are allowed to use/set the scale TWICE in total. In other words, 
you get to take 2 measurements (or “comparisons”) here.

4) Each “bucket” has enough room for multiple marbles. As long as you have the same number of marbles in each side, 
the odd marble has just enough weight to tip the scale.

"""

#TODO: # balancing scale

#TODO: Dividing input into 3 parts

#TODO: Check the condition 

#TODO: if size == 1 then return

import random

def balancer(setA:list[int], setB: list[int]) -> int:

    # calculate sum of each set
    sumA:int = sum(setA)
    sumB:int = sum(setB)

    if sumA == sumB: return 0

    if sumA > sumB: return 1

    return -1


def findOddMarble(input:list[int], flag=0) -> list[int]:

    if input == []: return []
    print("Weighing...")

    #divide given input into 3 parts
    size:int = len(input) # 3,9,27,81

    if size == 1: return input

    n:int = int(size/3)

    setA:list[int] = input[:n]
    setB:list[int] = input[n:-n]
    setC:list[int] = input[-n:]

    # first scale
    res = balancer(setA,setB)
    # a == b
    if(res == 0):
        # check size of setC if 1 then return element
        if n == 1: return setC
        # c has the odd element
        return findOddMarble(setC)

    # a != b
    else: 

        if(res>0): # a > b
            if n==1:
                if flag == 1: return setA
                if flag == -1: return setB
            # secind scale
            check:int = balancer(setA, setC)
            # a == c 
            if check == 0:
                return findOddMarble(setB, -1)
            # a > c
            
            return findOddMarble(setA,1)

        if res < 0: # b > a

            if n ==1: 
                if flag ==1: return setB
                if flag ==-1: return setA

            check:int =  balancer(setB,setC)
            # b == c
            if check == 0: return findOddMarble(setA,-1)

            return findOddMarble(setB,1)

    return []

def generateTestData(num): #3,9,27,81
    index = random.randint(1,num)
    odd_one = random.randint(1,100)
    elem = random.randint(1,100)

    while(elem == odd_one):
        elem = random.randint(1,100)

    output = [elem for _ in range(num-1)]
    output.insert(index,odd_one)
    return output, odd_one, index


     
output, odd_one, index = generateTestData(27)

actual = findOddMarble(output)[0]
actual_index = output.index(actual)

print("Input Array is {}".format(output))
print("Expected Odd element is {} and Actual odd element is {}".format(odd_one, actual))
print("Expected Index is {} and Actual Index is {}".format(output.index(odd_one)+1,actual_index+1))


















