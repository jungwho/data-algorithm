import numpy as np

from normalization import group_norm


if __name__ == "__main__":
    
    N = 3
    C = 32
    H = 8
    W = 8
    
    x = np.arange(N*C*H*W).reshape(N, C, H, W).astype(np.float32)
    eps = 1e-8
    
    # Group normalization using for-loops
    G = 4
    Cg = C // G  # Number of channels in a group
    y = x.copy()
    denom = Cg * H * W  # Denominator
    for n in range(N):
        for g in range(G):
            
            # 0. Get the start and end indices for this group
            ig_beg = g*Cg
            ig_end = (g+1)*Cg
            
            # 1. Get the average
            summ = 0 
            for c in range(ig_beg, ig_end): 
                for h in range(H):
                    for w in range(W):
                        summ += x[n, c, h, w]
                    # end of for w
                # end of for h
            # end of c
            avg = summ / denom            
                        
            # 2. Get the variance
            summ = 0
            for c in range(ig_beg, ig_end):
                for h in range(H):
                    for w in range(W):
                        summ += (x[n, c, h, w] - avg)**2
                    # end of for w
                # end of for h
            # end of for c
            var = summ / denom
    
            # 3. Normalize
            for c in range(ig_beg, ig_end):
                for h in range(H):
                    for w in range(W):
                        y[n, c, h, w] = (x[n, c, h, w] - avg) / np.sqrt(var + eps)
                    # end of for w
                # end of for h
            # end of for c
        # end of for g
    # end of for n
    
    solution = group_norm(x, G)
    #if not solution:
     #   raise ValueError("solution should not be None!")

    #assert(np.allclose(y, solution))
