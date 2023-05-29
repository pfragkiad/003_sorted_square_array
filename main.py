

# sorted squared array (new array)

# input IS sorted array (hint άρα μπορούμε να πάμε σε κάτι καλύτερο >> O(n))

a = [1,2,3,5,6,8,9]
a = [-7, -5 ,-4, 3, 6, 8, 9]
a=[1]

# 1, 4, 9, 25, 36, 64, 81

#O(nlogn) time, O(n) space 
r = [x*x for x in a] #nlogn due to sort (merge,heap,quick )
r.sort()
print(r)

# O(n) time, O(n) space
def get_sorted_squared(a):
    #initialize array and 
    la = len(a)
    s = [0]*la #he: [0 for _ in a]

    start = 0
    end = la-1
    for i in range(la-1,0,-1): #we iterate until the s[1]   (he: reversed(range(len(a))))
        if abs(a[end])>abs(a[start]):
            s[i] = a[end] * a[end]
            end -=1
        else:
            s[i] = a[start]*a[start]
            start+=1
    #for the last element it is always start=end (no need for checks) (mine)
    s[0] = a[start]*a[start] 
        
    return s
    
print(get_sorted_squared(a))