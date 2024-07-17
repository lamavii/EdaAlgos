#найти пару элементов с суммой s

# def p(arr, s):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n):
#             if arr[i]+arr[j]==s:
#                 return(i,j)


def p(arr, s):
    n = len(arr)
    pred=dict()
    for i in range(n):
        if s-arr[i]in pred:
            return(i, pred[s-arr[i]])
        pred[arr[i]]=i