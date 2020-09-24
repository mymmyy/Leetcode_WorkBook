# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学 
#  👍 4949 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        cur = result
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            cur.next = ListNode(carry)
        return result.next
# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#
#     s = Solution()
#     l1 = ListNode(2)
#     l1.next = ListNode(0)
#     l1.next.next = ListNode(9)
#
#     l2 = ListNode(3)
#     l2.next = ListNode(1)
#     l2.next.next = ListNode(3)
#
#     result = s.addTwoNumbers(l1, l2)
#
#     cur_print = result
#     while cur_print:
#         print(cur_print.val)
#         cur_print = cur_print.next
