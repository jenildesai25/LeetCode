# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '{}->{}'.format(self.val, self.next)


class MergeTwoSortedLists:

    def merge_two_sorted_lists(self, list_node_1, list_node_2):
        current = temp = ListNode(0)
        while list_node_1 and list_node_2:
            if list_node_1.val < list_node_2.val:
                current.next = list_node_1
                list_node_1 = list_node_1.next
            else:
                current.next = list_node_2
                list_node_2 = list_node_2.next
            current = current.next
        current.next = list_node_1 or list_node_2
        return temp.next


if __name__ == "__main__":
    merge_two_sorted_lists_obj = MergeTwoSortedLists()
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(4)
    print(merge_two_sorted_lists_obj.merge_two_sorted_lists(l1, l2))
