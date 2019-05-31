def staircase(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
#    print("Before return, n = {}".format(n))
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)



def test_function(test_case):
    answer = staircase(test_case[0])
    print("answer: {}".format(answer))
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case = [4, 7]
test_function(test_case)

test_case = [5, 13]
test_function(test_case)

test_case = [6, 19]
test_function(test_case)

test_case = [7,   ]
test_function(test_case)

#test_case = [3, 4]
#test_function(test_case)

#test_case = [20, 121415]
#test_function(test_case)
