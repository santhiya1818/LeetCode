class Solution {
public ListNode removeNthFromEnd(ListNode Head, int n) {
ListNode slow = Head;
ListNode fast = Head;

while (n-- > 0)
fast = fast.next;
if (fast == null)
return Head.next;

while (fast.next != null) {
  slow = slow.next;
  fast = fast.next;
}
slow.next = slow.next.next;

return Head;

}
}