class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '{}->{}'.format(self.val, self.next)


class RemoveLinkedListElements:

    def __init__(self, list_node_head, value):
        self.list_node_head = list_node_head
        self.val = value

    def remove_linked_list_elements(self):
        temp = ListNode('x')
        temp.next = self.list_node_head
        previous, current = temp, temp.next
        while current:
            if current.val == self.val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
        return temp.next


if __name__ == '__main__':
    linked_list_node = ListNode(1)
    linked_list_node.next = ListNode(2)
    val = 2
    remove_linked_list_elements_obj = RemoveLinkedListElements(linked_list_node, val)
    print(remove_linked_list_elements_obj.remove_linked_list_elements())
