class Solution(object):
    def reverseKGroup(self, head, k):
        temp = head
        count = 0
        while temp and count < k:
            temp = temp.next
            count += 1

        if count == k:
            prev, curr = None, head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            head.next = self.reverseKGroup(curr, k)
            return prev

        return head