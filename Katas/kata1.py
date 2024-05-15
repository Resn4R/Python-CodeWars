'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
'''

def count_positives_sum_negatives(arr):
    if not arr: return []

    #refactor 2
    return [len(list(filter(lambda n: n>0,arr))),sum(list(filter(lambda n: n<=0, arr)))]

    #refactor 1
    '''
    a = [0, 0]
    a[0] = len(list(filter(lambda n: n>0,arr)))
    a[1] = sum(list(filter(lambda n: n<=0, arr)))
    '''

    '''
    for number in arr:
        if number > 0:
            a[0]+=1
        else:
            a[1] += number
    '''
    #return a

#test
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]

result = count_positives_sum_negatives(sample)
solution = [10,-65]

print(result, solution)