import numpy as np

from normalization import layer_norm


if __name__ == "__main__":
    
    N = 3
    C = 4
    H = 8
    W = 8
    
    x = np.arange(N*C*H*W).reshape(N, C, H, W).astype(np.float32)
    eps = 1e-8
    
    # Layer normalization using for-loops
    y = x.copy()
    denom = C * H * W  # Denominator
    for n in range(N):
        # 1. Get the average
        summ = 0  
        for c in range(C):        
            for h in range(H):
                for w in range(W):
                    summ += x[n, c, h, w]
                # end of for w
            # end of for h
        # end of for c
        avg = summ / denom
        
        # 2. Get the variance
        summ = 0
        for c in range(C):        
            for h in range(H):
                for w in range(W):
                    summ += (x[n, c, h, w] - avg)**2
                # end of for w
            # end of for h
        # end of for c
        var = summ / denom
        
        # 3. Normalize
        for c in range(C):        
            for h in range(H):
                for w in range(W):
                        y[n, c, h, w] = (x[n, c, h, w] - avg) / np.sqrt(var + eps)
                # end of for w
            # end of for h
        # end of for c
    # end of for n
    
    solution = layer_norm(x)
    if not solution:
        raise ValueError("solution should not be None!")
        
    assert(np.allclose(y, solution))
