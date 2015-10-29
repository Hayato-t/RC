def sample():
    return 20
def vin():
    return 2
def st_x():
    return 10

from scipy import *
from scipy import linalg
import pylab as plt

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

Yans=zeros([1,20])
Xtsim=zeros([20,1+vin()+st_x()])
usim=zeros([1,vin()])

nikkei=loadtxt("kabuka.csv",delimiter=",")

#print nikkei
random.seed()

for i in range(0,st_x()):
    for j in range(0,st_x()):
        W[i][j]=random.random()

for i in range(0,st_x()):
    for j in range(0,vin()+1):
        Win[i][j]=random.random()

for i in range(0,sample()):
    # Y = Nikkeiheikin
    Y[0][i]=nikkei[i][3]
    # u = (uri,kai)
    u=matrix("%d;%d"%(nikkei[i][1],nikkei[i][2]))
    
    # calc x
    x2=tanh(Win.dot(r_[eye(1,1),u])+W.dot(x))
    x=x2*alpha+x*(1-alpha)
    Xt[i]=c_[eye(1,1),u.T,x.T]
X=Xt.T
X2=X.dot(Xt)+ganma*ganma*eye(1+vin()+st_x(),1+vin()+st_x())
X2=linalg.inv(X2)
Wout=Y.dot(Xt.dot(X2))

ypred=zeros(50-sample());

for i in range (sample(),50):
    usim=matrix("%d;%d"%(nikkei[i][1],nikkei[i][2]))
    x2=tanh(Win.dot(r_[eye(1,1),usim])+W.dot(x))
    x=x2*alpha+x*(1-alpha)
    ypred[i-sample()]=Wout.dot(r_[eye(1,1),usim,x])
    if i != sample():
        del Xtt
    Xtt=r_[Xt,c_[eye(1,1),usim.T,x.T]]
    del Xt
    Xt=Xtt
    del X
    X=Xt.T
    del X2
    X2=X.dot(Xt)+ganma*ganma*eye(1+vin()+st_x(),1+vin()+st_x())
    X2=linalg.inv(X2)
    Z=Y
    del Y
    Y=c_[Z,nikkei[i][3]]
    del Wout
    Wout=Y.dot(Xt.dot(X2))

xravel=linspace(sample(),50,50-sample())
ytrue=nikkei[sample():50,3].T

plt.plot(xravel,ypred,color="k",marker="o")
plt.plot(xravel,ytrue,color="c",marker="o")

plt.show()
