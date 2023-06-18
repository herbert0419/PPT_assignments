def mySqrt(x):
    left = 0
    right = x
    
    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
    
    return right


# Example1
input_1 = 4
output_1 = mySqrt(input_1)
print(f"The square root of {input_1} is {output_1}")

# Example2
input_2 = 8
output_2 = mySqrt(input_2)
print(f"The square root of {input_2} is {output_2}")