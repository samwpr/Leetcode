class ListNode{
    constructor(input){
        this.data = input
        this.next = null
    }
}

class LinkedList{
    constructor(head = null){
        this.head = head
    }
}

let node1 = new ListNode(1);
let node2 = new ListNode(2);
node1.next = node2;

let list = new LinkedList(node1);

console.log(list.head.data); //print 1
console.log(list.head.next.data); //print 2


