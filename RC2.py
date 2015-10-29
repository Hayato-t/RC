def sample():
    return 500
def vin():
    return 10
def st_x():
    return 20

from scipy import *
from scipy import linalg
x=zeros([st_x(),1])
x2=zeros([st_x(),1])
W=zeros([st_x(),st_x()])
u=zeros([vin(),1])
Win=zeros([st_x(),vin()+1])
Wout=zeros([1,1+vin()+st_x()])
alpha=1
ganma=0.5
Xt=zeros([sample(),1+vin()+st_x()])
Y=zeros([1,sample()])
b=zeros(vin())

random.seed()

for i in range(0,st_x()):
    for j in range(0,st_x()):
        W[i][j]=random.random()

for i in range(0,st_x()):
    for j in range(0,vin()+1):
        Win[i][j]=random.random()

for i in range(0,sample()):
    a=random.randint(0,1024)
    Y[0][i]=a
    for j in range(0,vin()):
        b[j]=a%2
        a=a/2
    #print b
    u=matrix("%d;%d;%d;%d;%d;%d;%d;%d;%d;%d"%(b[9],b[8],b[7],b[6],b[5],b[4],b[3],b[2],b[1],b[0]))
    #u=matrix("%d;%d;%d;%d"%(b[3],b[2],b[1],b[0]))
    x2=tanh(Win.dot(r_[eye(1,1),u])+W.dot(x))
    x=x2*alpha+x*(1-alpha)
    Xt[i]=c_[eye(1,1),u.T,x.T]
X=Xt.T
X2=X.dot(Xt)+ganma*ganma*eye(1+vin()+st_x(),1+vin()+st_x())
X2=linalg.inv(X2)
Wout=Y.dot(Xt.dot(X2))

#print Wout

while 1:
    print "input value"
    a=input()
    if a == 'end':
        break
    for j in range(0,vin()):
        b[j]=a%10
        a=a/10
    u=matrix("%d;%d;%d;%d;%d;%d;%d;%d;%d;%d"%(b[9],b[8],b[7],b[6],b[5],b[4],b[3],b[2],b[1],b[0]))
    #u=matrix("%d;%d;%d;%d"%(b[3],b[2],b[1],b[0]))
    X=r_[eye(1,1),u,x]
    print Wout.dot(X)
