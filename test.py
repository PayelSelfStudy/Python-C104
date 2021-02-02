new_data=[1,3,2,5,3,7,8,9,3,8,5]
n = len(new_data)
print(" n is "+str(n))
if n % 2 == 0:
    #getting the first number
	median1 = float(new_data[n//2])
    
    #getting the second number
	median2 = float(new_data[n//2 - 1])
    

    #getting mean of those numbers
	median = (median1 + median2)/2
    
else:
	median = new_data[n//2]

print("Median is: " + str(median))
