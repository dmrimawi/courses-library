#                 0 1 2 3 4
# int arr[5]; -> [7, ,8, ,9]
# arr[0] = 7 -> O(1)
# arr[2] = 8
# arr[4] = 9

# int arr[5]; -> [10, 7, 0, 8, ]
# to inster 10, we need to shift the data one element to the right
# arr[0] = 10 
# insert to array costs O(n), because of shifting
# the same for deleting O(n), because of shifting

# int mat[n][m];
# access -> O(1)
# insert -> O(n*m)
# delete -> O(n*m)

# O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < ... < O(2^n)

#     head
# [data1] -> [data2] -> [data3] -> ... -> [datan] -> None
# access -> O(n)
# 