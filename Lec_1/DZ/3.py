# Вам дан массив целых чисел размера n, и ваша задача найти два значения
# (на разных позициях) чья сумма равна x.
def find_pairs_sum(arr,n,x):
    num_index={}
    for i in range (n):
        if(x-arr[i])in num_index:
            return(num_index[x-arr[i]]+1, i+1)
        num_index[arr[i]]=i
    return None



n, x = map(int, input().split())
arr = list(map(int, input().split()))