def maximumSubarray(a,b,array):
    start=0
    end=0
    current_sum = array[0]
    maxi=0
    while end<a:
        if current_sum<=b:
            maxi=max(maxi, current_sum)
            end+=1
            if end<a:
                current_sum+=array[end]
            if current_sum==b:
                return current_sum
        else:
            current_sum -= array[start]
            start += 1
    return maxi

a=int(input())
b=int(input())
array=list(map(int, input().split()))
print(maximumSubarray(a,b,array))