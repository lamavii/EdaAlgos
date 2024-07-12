#найти пару элементов с суммой s

# def p(arr, s):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n):
#             if arr[i]+arr[j]==s:
#                 return(i,j)


def p(arr, s):
    n = len(arr)
    pred=set()
    for i in range(n):
        if s-arr[i]in pred:
            print(arr[i], s-arr[i])
        pred.add(arr[i])