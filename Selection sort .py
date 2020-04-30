def sort(li):
    """Uses Selection Sort to put the list in increasing order."""
    for i in range(len(li)):
        # Find the smallest value left in the list
        # Put it at the beginning of the tail.
        currIndex = i 
        currMin = li[i]
        for j in range(i, len(li)):
            if li[j]<currMin:
                currIndex = j
                currMin = li[j]
        temp = li[i]
        li[i] = currMin
        li[currIndex] = temp 
             
            
