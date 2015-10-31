n = int(input("Please Enter a Number: "))

def values():
    
    value = n+(n*11)+n*(111)
    print(value)
    return 0
values()
#anather way

n1 = int("%s" % n)
n2 = int("%s%s" % (n,n))
n3 = int("%s%s%s" %(n,n,n))
print(n1+n2+n3)

#Ques11, write python programe to print the documents(syntax, description etc)
print(abs.__doc__)

print("""
atring that you "don't" have to escape
This
is a ....multi-line
heredoc string ------> example
""")

