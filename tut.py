# -*- coding: utf-8 -*-
# Importing itertools package for pairing the numbers
import itertools
# Getting input from user and storing it in "a"
a = input('Enter the first integer number')
if a.isdigit():
    a= int(a)
    print(a)
    if a <= 0:
        print('Enter a number greater than zero')
    # if the given input is greater than zero then the code will be executed
    else:
        # printing the user input
        print('first number is ', a)
        # getting next set of numbers as input from user
        input_string = input('Enter a list element separated by space ')
        # Separating thr numbers with respect to space using split function
        the_list = input_string.split()
        # Displaying the set of numbers
        print('Input list is', the_list)
        # storing that set of numbers in a variable named results
        results = [int(i) for i in the_list]


        # creating a function to remove the duplicate numbers
        def Remove(duplicate):
            # Another list is created to store the non duplicated values
            final_list = []
            # for loop is used to check each and every number in the list
            for num in duplicate:
                # using if statement we are checking for duplicates
                if num not in final_list:
                    final_list.append(num)
            # returning the list without any duplicates
            return final_list


        # using remove function in our input list
        results = Remove(results)
        # print (results)
        b = ()
        # using itertools pairing is done
        for i in itertools.combinations(results, 2):
            # print(i)

            b += (i,)
        # print (b)
        final = ()
        # checking for addition of these paired numbers and first number which we got as input fro m user are equal
        for x in b:
            # creating temporary variable named sum
            sum = 0
            # using for loop code can access each pair in list
            for y in x:
                sum += y
                sum = int(sum)
            # using if condition checking for addition of two numbers in pair are equal to "a" which is input from user
            if a == sum:
                final += (x,)
                # print (x)

        # pair_sum.append(sum)
        # print(sum)
        # printing the final result
        print(final)


else:
    print("Enter a valid number")
# Checking whether the given input is greater than zero
# if the inout is less than or equal to zero then the code will get terminated
