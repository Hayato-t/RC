from scipy import *
from scipy import linalg
x=zeros([10,1])
x2=zeros([10,1])
W=zeros([10,10])
u=zeros([4,1])
Win=zeros([10,5])
Wout=zeros([16,15])
alpha=0.5
ganma=0.5
Xt=zeros([320,15])
Y=zeros([16,320])
random.seed()
for i in range(0,9):
    for j in range(0,9):
        W[i][j]=random.random()
for i in range(0,9):
    for j in range(0,4):
        Win[i][j]=random.random()
for i in range(0,319):
    a=random.randint(0,16)
    print a
    Y[a][i]=1
    b=zeros(4)
    b[0]=a%2
    a=a/2
    b[1]=a%2
    a=a/2
    b[2]=a%2
    a=a/2
    b[3]=a%2
    u=matrix("%d;%d;%d;%d"%(b[3],b[2],b[1],b[0]))
    x2=tanh(Win.dot(r_[eye(1,1),u])+W.dot(x))
    x=x2*alpha+x*(1-alpha)
    Xt[i]=c_[eye(1,1),u.T,x.T]
X=Xt.T
#Y=c_[eye(16,16),eye(16,16),eye(16,16),eye(16,16),eye(16,16),eye(16,16)]
#print Y.ndim
#print (X.dot(Xt)+ganma*ganma*eye(15,15))
X2=(X.dot(Xt)+ganma*ganma*eye(15,15))
#print X2
#print linalg.det(X2)
X2=linalg.inv(X2)
Wout=Y.dot(Xt.dot(X2))

print Wout

while 1:
    print "input value"
    a=input()
    if a == 'end':
        break
    print a
    b=zeros(4)
    b[0]=a%10
    a=a/10
    b[1]=a%10
    a=a/10
    b[2]=a%10
    a=a/10
    b[3]=a%10
    u=matrix("%d;%d;%d;%d"%(b[3],b[2],b[1],b[0]))
    X=r_[eye(1,1),u,x]
    print Wout.dot(X)
print x
