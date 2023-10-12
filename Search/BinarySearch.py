
def search(l,r,arr,k):
    mid = (l+r)//2
    if k == arr[mid]:
        return True
    if l == r:
        return False
    if k < arr[mid]:
        return search(l,mid-1,arr,k)
    if k > arr[mid]:
        return search(mid+1,r,arr,k)

inp = input("Enter Input : ").split("/")
arr,k = list(map(int,inp[0].split())),int(inp[1])
print(search(0,len(arr)-1,sorted(arr),k))



