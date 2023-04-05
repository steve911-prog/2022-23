values = [1.14, 12,32,27,25,36,-11,-22,85,37,3,26,1.23,52,1.2,67,122,-26,-10,0,25,
          -15,26,-13.2,25,1,-2,-1.44,25,-36,-2,-31,-7,-1.2,-6,4,-22,31,-3,-4,2]
print("Max: ", max(values))
print("Min: ", min(values))
#print(average)
a = []
for i in values:
    if i > 20:
        #print(i)
        a.append(i)
        
values = a

print("All numbers bigger than 20: ", values)
