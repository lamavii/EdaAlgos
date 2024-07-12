# дан массив, состоящий из n элементов и число k<n
# Найти минимальную сумму элементов, которая состояит из k элементов

# def p(arr,k):
#     n=len(arr)
#     mn=sum(arr[0:k])
#     for i in range (1,n-k+1):
#         if mn>sum(arr[i:i+k]):
#             mn=sum(arr[i:i+k])
#     return mn

def p(arr,k):
    n=len(arr)
    cur_sum=sum(arr[0:k])
    mn=cur_sum
    for i in range(1, n-k+1):
        cur_sum+=arr[i+k-1]-arr[i-1]
        if mn>cur_sum:
            mn=cur_sum
    return mn