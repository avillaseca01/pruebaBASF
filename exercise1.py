#exercise1

array1 = "UIBAZSIAHFB"
array2 = "PQACIZIBDLAG"
array3 = "QIDBCZKSHDVF"


#I know this is not the most efficient way to solve this problem, but it works when there is only one longest common substring
def longest_common_substring(arr1, arr2, arr3):
    longest = ""
    
    for i in range(len(arr1)):
        for j in range(i + 1, len(arr1) + 1):
            substring = arr1[i:j]
            
            if substring in arr2 and substring in arr3:
                if len(substring) > len(longest):
                    longest = substring
    
    return longest

result = longest_common_substring(array1, array2, array3)

print("Longest common substring:", result)