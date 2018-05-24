def find(P, start, n):
    for i in range(start, len(P)):
        if P[i] == n or P[i] == -n:
            return i
            
def reversal(P, start, stop):
    rev = [-i for i in P[start:stop+1]]
    rev.reverse()
    P[start:stop+1] = rev
    
    return P
    
def greedy_sorting(P):
    approx_reversal_distance = 0
    
    print(P)
    
    for k in range(len(P)):
        if P[k] !=  k+1:
            i = find(P, k, k+1)
            P = reversal(P, k, i)
            approx_reversal_distance += 1
            
            print(P)
                        
            if P[k] < 0:
                P[k] = -P[k]
                approx_reversal_distance += 1
                
                print(P)
            
    return approx_reversal_distance
    
def main():
   # P = [+1, -7, +6, -10, +9, -8, +2, -11, -3, +5, +4]
   # P = [+6, -7, +1, -10, +9, -8, +2, -11, -3, +5, +4]
    P = [-2, -5, +3, +4, +1]
    
    print(greedy_sorting(P))
    
if __name__ == "__main__":
    main()


    
