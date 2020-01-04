# --------------
def check_palindrome(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        return True

def palindrome(num):
    bol=False
    #x=len(str(num))
    num=num+1
    while(bol==False):
        if(check_palindrome(num)):
            bol=True
        else:
            num=num+1
    return num

b=palindrome(8)
print(b)


# --------------
#Code starts here
def a_scramble(str_1, str_2):
    list1=[]
    list2=[]
    for i in range(len(str_1)):
        list1.append(str_1[i].lower())

    for i in range(len(str_2)):
        list2.append(str_2[i].lower())
    
    for i in range(len(list2)):
        if(list2[i] in list1):
            list1.remove(list2[i])
            #print(list2[i]+'IF')
            bol=True
        else:
            #print(list2[i]+'ELSE')
            bol=False
    return bol


bol=a_scramble("baby shower","shows")
print(bol)


# --------------
#Code starts here
def check_fib(num):
    num1=0
    num2=1
    num3=0
    fibo=[num1,num2]
    while(num>=num3):
        num3=num1+num2
        fibo.append(num3)
        num1,num2=num2,num3
    c= num in fibo
    return c

d=check_fib(145)
print(d)


# --------------
#Code starts here
def compress(word):
    word=word.lower()
    count = 1
    string=''
    for i in range(1, len(word) + 1):
        if i == len(word):
            string=string+word[i - 1] + str(count)
            break
        else:
            if word[i - 1] == word[i]:
                count += 1
            else:
                string=string+word[i - 1] + str(count)
                count = 1
    return string

word=compress('Ss')
print(word)


# --------------
#Code starts here
def k_distinct(string,k):
    list1=[]
    list2=[]
    for i in range(len(string)):
        list1.append(string[i].lower())
    set1=set(list1)
    list2=list(set1)
    if(k==len(list2)):
        return True
    else:
        return False

value=k_distinct('banana',4)
print(value)


