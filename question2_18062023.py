class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    curr = dummy_head
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        sum_val = x + y + carry
        carry = sum_val // 10
        curr.next = ListNode(sum_val % 10)

        curr = curr.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry:
        curr.next = ListNode(carry)

    return dummy_head.next




# Example 1:
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

output_1 = addTwoNumbers(l1, l2)
result_1 = []
curr = output_1
while curr:
    result_1.append(curr.val)
    curr = curr.next
print("Input: l1 = [2, 4, 3], l2 = [5, 6, 4]")
print("Output:", result_1)

# Example 2:
l3 = ListNode(0)
l4 = ListNode(0)

output_2 = addTwoNumbers(l3, l4)
result_2 = []
curr = output_2
while curr:
    result_2.append(curr.val)
    curr = curr.next
print("Input: l3 = [0], l4 = [0]")
print("Output:", result_2)

# Example 3:
l5 = ListNode(9)
l5.next = ListNode(9)
l5.next.next = ListNode(9)
l5.next.next.next = ListNode(9)
l5.next.next.next.next = ListNode(9)
l5.next.next.next.next.next = ListNode(9)
l5.next.next.next.next.next.next = ListNode(9)

l6 = ListNode(9)
l6.next = ListNode(9)
l6.next.next = ListNode(9)
l6.next.next.next = ListNode(9)

output_3 = addTwoNumbers(l5, l6)
result_3 = []
curr = output_3
while curr:
    result_3.append(curr.val)
    curr = curr.next
print("Input: l5 = [9, 9, 9, 9, 9, 9, 9], l6 = [9, 9, 9, 9]")
print("Output:", result_3)