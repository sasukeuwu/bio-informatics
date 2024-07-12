#Implement PatternCount 
text = "GCGCG"
pattern = "GCG"

def PatternCount(Text, Pattern):

    count = 0

    for i in range(len(Text) - len(Pattern) + 1):

        if Text[i:i+len(Pattern)] == Pattern:

            count = count + 1

    return count       
            
print(PatternCount(text,pattern))            

#u can add any sequence and pattern fo rit and it will work in this code
