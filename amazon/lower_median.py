"""
Date: February 29, 2024
Name: Rajashree Dahal
Problem: Calculate lower median of two sorted lists
"""
def lower_median(A,al,ar, B, bl, br):
    if al == ar:
        return  min(A[al],B[bl])
    elif ar-al+1 == 2 :
        return min(max(A[al], B[bl]) , min(A[ar],B[br]))
    else:
        Amid = (al+ar)//2
        Bmid =  (bl+br)//2
        size =  ar +1 -al
        if size %2 == 1 :
            if A[Amid] <  B [Bmid]:
                return lower_median(A, Amid, ar, B, bl, Bmid)
            else:
                return lower_median(A, al, Amid, B,Bmid , br) 
        if size %2 == 0:
            if A[Amid]< B[Bmid]:
                return lower_median(A,Amid,ar,B, bl, Bmid+1)
            else:
                return lower_median(A, al,Amid+1, B, Bmid,br)