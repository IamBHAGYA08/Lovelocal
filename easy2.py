class treenode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left
def sortedarray(nums):
    if not nums:
        return None
    mid=len(nums)//2
    root=treenode(nums[mid])
    root.left=sortedarray(nums[:mid])
    root.right=sortedarray(nums[mid+1:])
    return root
nums=[1,2,3,4,5,6,7]
tree=sortedarray(nums) 
print(tree)       
            

