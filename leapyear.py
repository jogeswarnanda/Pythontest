def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    div1 = year%4
    div2 = year%100
    div3 = year%400
    if div1 == 0 and div2 != 0:
        return True
    elif div1 == 0 and div3 == 0:
        return True
    else:
        return False
    
        
print(is_leap_year(1700))