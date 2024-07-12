def reverse(text): #creating function which reverses a given string input
    n=len(text) #measuring the string length
    rev="" #blank string to which i'll append letters from the input string
    for i in range(1, n+1):
        rev+=text[n-i] #Adding letters from the end of the input string as the first letters of the blank string
    return rev
def ComplementGenerator(template):
    template=template.upper()
    length=len(template)
    complement="" #blank string to which i'll append each letter's complement
    for j in range(length): #the loop will last for the length of the template
        if template[j]=="A": #If there's A we complement with T, vice versa and so on
            complement+="T"
        elif template[j]=="T":
            complement+="A"
        elif template[j]=="C":
            complement+="G"
        else:
            complement+="C"
    print(reverse(complement)) #reversing the finished complement
template=input("Enter any template strand to get its complement ")
ComplementGenerator(template)