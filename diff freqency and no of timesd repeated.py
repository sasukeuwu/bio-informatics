text = "CGATATATCCATAG"
k = 3  #k is the grp of letters u want to find frequency of 

def FrequencyMap(text,k):
    freq = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        freq[pattern] = 0
        
    for i in range(n-k+1):
         pattern = text[i:i+k] 
         freq[pattern] = freq[pattern]+1
    return freq       
print(FrequencyMap(text,k))

#if Pattern in freq:
#            freq[Pattern] +=1
#        else:
#            freq[Pattern] = 1
#instead of long ahh code just use this 