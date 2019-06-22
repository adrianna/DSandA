###################################
## sqrt()
##
## Issue: Need to work on numbers > 400
##
###################################


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


    start_pt = 0
    end_pt = len(ref_sq) - 1
    mid_pt = (end_pt - start_pt) // 2;
  #  print("length of ref_sq: {}".format(end_pt))
    base = binSearchBase(ref_sq, number, mid_pt, start_pt, end_pt)
  #  print("sqrt(): {}".format(base))
    return base


    
def binSearchBase(input_list, number, idx, start_pt, end_pt):

    mid_pt = idx
    base = 0
    if number == 0:
        return base
    
    if number > 400:
        print("does not do sqrt for n > 400")
        return None
    if number == input_list[mid_pt]:
        base = mid_pt + 1
        print("number equals il[mid]: {}".format(base))
        return base
    elif input_list[mid_pt] < number:
        
        if number < input_list[mid_pt+1]:
            base = mid_pt + 1  # Base numbers = 1+idx
            print("il[mid] <number < il[mid+1]: {}".format(base))
            print("\t{}".format(input_list[mid_pt]))
            print("\t{}".format(number))
            print("\t{}".format(base))
            
            return base
        else:
            start_pt = mid_pt
            mid_pt = start_pt + (end_pt - start_pt)//2
            return binSearchBase(input_list, number, mid_pt, start_pt, end_pt)
            
    elif input_list[mid_pt] > number:
        # recalculate the mid_pt
        print(input_list[mid_pt])
        print(number)
        print("\trecurse... at midpt: {}",format(mid_pt))
        end_pt = mid_pt
        mid_pt = start_pt + (end_pt - start_pt)//2

        return binSearchBase(input_list, number, mid_pt, start_pt, end_pt)



    
#print("Sqrt(4): {}".format(sqrt(4)))
#print("Sqrt(5): {}".format(sqrt(5)))
#print("Sqrt(27): {}".format(sqrt(5)))



#print ("Pass" if  (3 == sqrt(9)) else "Fail")
#print ("Pass" if  (0 == sqrt(0)) else "Fail")
#print ("Pass" if  (4 == sqrt(16)) else "Fail")
#print ("Pass" if  (1 == sqrt(1)) else "Fail")
#print ("Pass" if  (5 == sqrt(27)) else "Fail")

#print ("Pass" if  (22 == sqrt(500)) else "Fail")
#print ("Pass" if  (None == sqrt(500)) else "Fail")
#print ("Pass" if  (20 == sqrt(400)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
#print ("Pass" if  (18 == sqrt(350)) else "Fail")
#print ("Pass" if  (19 == sqrt(373)) else "Fail")
