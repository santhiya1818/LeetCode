class Solution {
public ListNode swapPairs(ListNode head) {

    ListNode z = new ListNode();  
    ListNode current = head;   
    ListNode previous = z; 
    if(current == null || current.next == null){ 
        return head ;
    }
    while(current !=null && current.next != null){  
       previous.next = current.next; 
       current.next = previous.next.next; 
       previous.next.next = current; // link between 1 n 2
       // update  
       previous = current; 
       current = current.next;
    } 
    return z.next;
    
}

}