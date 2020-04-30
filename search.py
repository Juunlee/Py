def generate_squares(n):
    a = []
    for i in range(n) :
        a.append(i*i)
    return a

squares2 = generate_squares(100000)

def deliberate_search(li, val):
    """searches the list li for the value val.
    Returns the index if it's found, and -1 otherwise,
    Assumes it is in increasing order."""
    for i in range(len(li)):
        if li[i]==val:
            return i
        elif li[i]>val:
            return -1
    return -1 

print(deliberate_search(squares2, 2000300002))

def binary_search(li, val):
    minimum = 0
    maximum = len(li)-1
    mid = (minimum+maximum)//2
    while maximum>minimum:
        mid = (minimum+maximum)//2
        if li[mid] == val:
            return mid
        elif val<li(mid):
            maximum = mid
        elif val>li(mid):
            minimum = mid+1
    return -1
    
