arr=[int(x) for x in input("enter the sorted list of numbers seperated by spaces:").split()]
target=int(input("enter the target value to search:"))
def first_occ(arr,n,key):
    s,e=0,n-1
    ans=-1
    while s<=e:
        mid=s+(e-s)//2
        if arr[mid]==key:
            ans=mid
            e=mid-1
        elif key>arr[mid]:
            s=mid+1
        else:
            e=mid-1
    return ans


def last_occ(arr,n,key):
    s,e=0,n-1
    ans=-1
    while s<=e:
        mid=s+(e-s)//2
        if arr[mid]==key:
            ans=mid
            e=mid+1
        elif key>arr[mid]:
            s=mid+1
        else:
            e=mid-1
    return ans