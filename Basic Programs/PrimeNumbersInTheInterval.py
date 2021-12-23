# python program  to find the prime number in the interval
start = 0
end = 100
  
for i in range(start, end+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)