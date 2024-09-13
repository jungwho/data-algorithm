import numpy as np

def batch_norm(x, eps=1e-8):
    
    s=x.shape[3]*x.shape[2]*x.shape[0]
    
    m_sum=x.sum(axis=3, keepdims=True).sum(axis=2, keepdims=True).sum(axis=0, keepdims=True)
    m=m_sum/s
 
    p=np.square(x-m)
    v_sum=p.sum(axis=3, keepdims=True).sum(axis=2, keepdims=True).sum(axis=0, keepdims=True)
    v=v_sum/s
 
    a=np.sqrt(v+eps)
    return (x-m)/a

def instance_norm(x, eps=1e-8):
    
    s=x.shape[3]*x.shape[2]
    
    m_sum=x.sum(axis=3, keepdims=True).sum(axis=2, keepdims=True)
    m=m_sum/s
 
    p=np.square(x-m)
    v_sum=p.sum(axis=3, keepdims=True).sum(axis=2, keepdims=True)
    v=v_sum/s
 
    a=np.sqrt(v+eps)
    return (x-m)/a

def layer_norm(x, eps=1e-8):
    
    s=x.shape[3]*x.shape[2]*x.shape[1]
    
    m_sum=x.sum(axis=3, keepdims=True).sum(axis=2, keepdims=True).sum(axis=1, keepdims=True)
    m=m_sum/s
 
    p=np.square(x-m)
    v_sum=p.sum(axis=3, keepdims=True).sum(axis=2, keepdims=True).sum(axis=1, keepdims=True)
    v=v_sum/s
 
    a=np.sqrt(v+eps)
    return (x-m)/a

def group_norm(x, n_groups, eps=1e-8):
    
    g=n_groups
    n=int(x.shape[0])
    c=int(x.shape[1])
    h=int(x.shape[2])
    w=int(x.shape[3])

    hw=int((c/g)*h*w)
    a=x.reshape(n,g,hw)

    m=a.mean(axis=2,keepdims=True)
    v=a.var(axis=2,keepdims=True)
    p=np.sqrt(v+eps)
    r=(a-m)/p

    return r.reshape(n,c,h,w)



    
    
    
    
    
    
