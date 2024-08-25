def array(A , start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    array(A, start+1,end-1)

ar = [1,4,7,9]
arr = array(ar,0,3)
print(ar)