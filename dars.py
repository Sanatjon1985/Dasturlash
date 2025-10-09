print("x=")
x=int(input())
print("y=")
y=int(input())
i=x
s=0
while (i<=y):
    print(i)
    s=s+i
    if s>10:
        break
    i+=1
print("+++++")
raqamlar=[0,1,2,3,4,5,6,7,8,9]
for raqam in raqamlar:
    print(raqam)
def my_show():
    print("aa")
my_show()
def arif(x):
    return 50*x
print(arif(10))
def add(x,y):
    return x+y
a=10
b=20
print(a,"+",b,"=",add(a,b))
