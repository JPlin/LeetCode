# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        P = None
        jinwei = 0
        while l1 is not None and l2 is not None:
            single_sum = l1.val + l2.val + jinwei
            jinwei = single_sum // 10
            ans = ListNode(single_sum % 10)
            if P is not None:
                P.next = ans
            else:
                head = ans
            P = ans
            l1 = l1.next
            l2 = l2.next            
        
        while l1 is not None:
            single_sum = l1.val + jinwei
            jinwei = single_sum // 10
            ans = ListNode(single_sum % 10)
            if P is not None:
                P.next = ans
            else:
                head = ans                
            P = ans
            l1 = l1.next            
        
        while l2 is not None:
            single_sum = l2.val + jinwei
            jinwei = single_sum // 10
            ans = ListNode(single_sum % 10)
            if P is not None:
                P.next = ans
            else:
                head = ans                
            P = ans        
            l2 = l2.next

        if jinwei != 0:
            ans = ListNode(jinwei)
            P.next = ans  
        return head

solution = Solution()
print(solution.addTwoNumbers([2,4,3] , [5,6,4]))