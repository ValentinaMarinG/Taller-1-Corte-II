from DoubleLinkedList import doubleLinkedList
inst_double_linked_list = doubleLinkedList()

inst_double_linked_list.prepend_node(3)
inst_double_linked_list.prepend_node('B')
inst_double_linked_list.prepend_node(1)
inst_double_linked_list.append_node(2)
inst_double_linked_list.show_double_linked_list()

inst_double_linked_list.delete_head()
inst_double_linked_list.show_double_linked_list()

#inst_double_linked_list.pop_tail()
#inst_double_linked_list.show_double_linked_list()

#inst_double_linked_list.update(2)
#nst_double_linked_list.show_double_linked_list()

inst_double_linked_list.insert(2,56)
inst_double_linked_list.show_double_linked_list()

inst_double_linked_list.insert(3,25)
inst_double_linked_list.show_double_linked_list()

inst_double_linked_list.delete_node(2)
inst_double_linked_list.show_double_linked_list()

#inst_double_linked_list.delete_node(1)
#inst_double_linked_list.show_double_linked_list()

#inst_double_linked_list.reverse_list()
#inst_double_linked_list.show_double_linked_list()

inst_double_linked_list.reverse_list_sqrt()
inst_double_linked_list.show_double_linked_list()