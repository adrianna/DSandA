def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """


    # Build a hash with the sqrt results
    # On first lookup, check what the sqrt(n) and sqrt(n-1) or sqrt(n+1),
    # depending if n > n_lookup or n < n_lookup
    # Bin search between those two numbers
    # Pick the lower value of the two hash key values
    # for the floored number
    
    ref_sq = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256,
              289, 324, 361, 400]
    
    

    pass


    
def binSearchBase(input_list, number, idx):
    start_pt = 0
    end_pt = len(input_list)
    mid_pt = len(ref_sq) // 2;
    
    if number == ref_sq[mid_pt]:
        base = mid_pt + 1
        return base
    elif number < ref_sq[mid_pt]:
        end_pt = mid_pt
        mid_pt = (end_pt - start_pt)//2
        binSearchBase(input_list, number, mid_pt)
    elif number > ref_sq[mid_pt]:
        start = mid_pt + 1
        mid_pt = (end_pt - start_pt)//2
        binSearchBase(input_list, number, mid_pt)



    



print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
