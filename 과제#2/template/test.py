import numpy as np
eps=0.0000001

x=np.array([[[[1,2],[2,4]], [[1,2],[2,4]], [[1,2],[2,4]], [[1,2],[2,4]]],
           [[[2,4],[3,6]], [[2,4],[3,6]], [[2,4],[3,6]], [[2,4],[3,6]]]])

n=int(x.shape[0])
c=int(x.shape[1])
h=int(x.shape[2])
w=int(x.shape[3])

g=int(2)
hw=int((c/g)*h*w)
a=x.reshape(n,g,hw)

m=a.mean(axis=2,keepdims=True)
v=a.var(axis=2,keepdims=True)
s=np.sqrt(v+eps)

r=(a-m)/s
print(r)

rr=r.reshape(n,c,h,w)
