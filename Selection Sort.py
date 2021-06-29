# Happy coding ,code by Md Arif uddin
# This example of Selection  sort code 
# coding time 12:47 Am ,date 6/28/2021

def Selectionsort(num):

    for i in range(6):
        minpos = i
        for j in range(i, 7):
            if num [j] < num[minpos]:
                minpos = j


        temp = num[i]
        num[i] = num[minpos]
        num[minpos] = temp

        print(num)

num = [11,31,56,8,6,7,2]
Selectionsort(num)


print(num)

"""
 this code output :
[2, 31, 56, 8, 6, 7, 11]
[2, 6, 56, 8, 31, 7, 11]
[2, 6, 7, 8, 31, 56, 11]
[2, 6, 7, 8, 31, 56, 11]
[2, 6, 7, 8, 11, 56, 31]
[2, 6, 7, 8, 11, 31, 56]
[2, 6, 7, 8, 11, 31, 56]
"""
