#singly Linked list

#arr = []->10 ->[]20, []30, 


class Node:
    def _init_(self,data):
        self.data = data
        self.data =data
        self.next =None

        class LinkedList:
            def _init_(self):
                self.head = None

                def insert_front(self, data):
                    new_node = Node(data)
                    new_node.next = self.head
                    self.head = new_node
                    

                    #print list
                    def print_list(self):
                        curr = self.head

                        while curr:
                            print(curr.data, end = "->")
                            curr = curr.next
                            print("none")

                        

