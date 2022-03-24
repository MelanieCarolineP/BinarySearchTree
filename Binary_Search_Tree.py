class Binary_Search_Tree:

  class __BST_Node:
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 0

  def __init__(self):
    self.__root = None
    self.__string= ''
    self.__size= 0
    self.__list = []

  def _update_height(self, current):
    if self.__root is None:
        pass
    elif current.right is None and current.left is None: #its a leaf node
        current.height = 1
    elif current.right is None: #has a left child
        current.height = current.left.height + 1
    elif current.left is None: #has a right child
        current.height= current.right.height + 1
    else: #has two chidlren, get the max of the two and add 1
        current.height = max(current.left.height, current.right.height) + 1

  def __balance(self, current):
    if (current.left is None) and (current.right is None): #it is balanced.
        self._update_height(current)
        return current
    elif (current.right is None and (0 - current.left.height) == -2) or\
    (current.left is None and (current.right.height - 0) == -2) or\
    (current.left is not None and current.right is not None and (current.right.height - current.left.height) == -2):  # children are left-heavy
        if (current.left is not None and current.left.left is None and (current.left.right.height == 1)) or\
        (current.left is not None and current.left.left is not None and current.left.right is not None and (current.left.right.height - current.left.left.height == 1)):
            old_cur = current.left #left-right imbalance
            floater2 = old_cur.right.left
            current.left = current.left.right#first rotation
            current.left.left = old_cur
            current.left.left.right = floater2
            #second rotation
            old_cur = current
            floater = current.left.right
            current = current.left
            current.right = old_cur
            current.right.left = floater
            self._update_height(current)
            return current
        else: #left-left imbalance
            floater = current.left.right
            old_cur= current #left-left imbalace
            current= current.left
            current.right= old_cur
            current.right.left = floater
            self._update_height(current)
            return current
#(current.right is None and (0 - current.left.height) == 2) or\
    elif (current.left is None and (current.right.height - 0) == 2) or\
    (current.left is not None and current.right is not None and (current.right.height - current.left.height) == 2): #children are right-heavy
        if (current.right is not None and current.right.right is None and (0 - current.right.left.height) == -1) or\
        (current.right is not None and current.right.left is not None and current.right.right is not None and (current.right.right.height - current.right.left.height) == -1):
            old_cur = current.right #right-left imbalance
            floater2 = old_cur.left.right
            current.right = current.right.left #first rotation
            current.right.right = old_cur
            current.right.right.left = floater2
            #second rotation
            old_cur = current
            floater = current.right.left
            current.left = old_cur
            current.left.right = floater
            self._update_height(current)
            return current
        else: #right-right imbalance
            floater = current.right.left
            old_cur = current
            current = current.right
            current.left = old_cur
            current.left.right = floater
            self._update_height(current)
            return current
    else:
        return current

  def insert_element(self, value):
    self.__root = self._rec_insert(value, self.__root)
    self.__size += 1 #for the list method
    self._update_height(self.__root)

  def _rec_insert(self, value, current): #private recursive insertion method, where current is the current node
    if current is None:
        current= self.__BST_Node(value)
        self._update_height(current)
        return current
    elif value < current.value: #if the value is smaller than current node
        current.left = self._rec_insert(value, current.left)

    elif value > current.value:
        current.right = self._rec_insert(value, current.right)
    else:
        raise ValueError
    return self.__balance(current)

  def remove_element(self, value):
    self.__root = self._rec_remove(value, self.__root) #will set the returned root node with its updated assignments as the new root node
    self.__size -= 1
    self._update_height(self.__root)

  def _rec_remove(self, value, current): #private recursive method for remove_element method
    if current == None:
        raise ValueError #raise error because value is missing
    if current.value == value: #value is found in the tree
        if current.left == None and current.right ==None: #node has zero children
            return None
        elif current.right == None: #child is on the left
            return current.left
        elif current.left == None: #child is on the right
            return current.right
        else: #node has two children
            min = current.right #temp minimum value of current's right subtree
            while min.left != None: #terminates when we find minimum
                min = min.left
            current.value = min.value #copying min value
            current.right = self._rec_remove(min.value, current.right)
            self._update_height(current)
    elif value < current.value: #if value is less than current value
        current.left = self._rec_remove(value, current.left)
    elif value > current.value:#if value is greater than current value
        current.right = self._rec_remove(value, current.right)

    return self.__balance(current)

  def in_order(self):
    if self.__root is None:
        return '[ ]'
    self.__string = '[ '
    if self.__root is not None:
        self._rin_order(self.__root)
        self.__string = self.__string[:-2] #slice off the last comma and space before closing the string representation.
        self.__string += ' ]'
        return self.__string

  def _rin_order(self, current): # private recursive in order method
    if current is not None: #if node has a value in it
        self._rin_order(current.left)
        self.__string += str(current.value) + ', '
        self._rin_order(current.right)

  def pre_order(self):
    if self.__root == None: #if the tree is empty return an emty list
       return '[ ]'
    self.__string = '[ '
    if self.__root is not None: #if the list isn't empty
       self._rpre_order(self.__root) #start recursion at root node
       self.__string = self.__string[:-2]
       self.__string += ' ]'
       return self.__string

  def _rpre_order(self, current): #private recursive method
      if current is not None:
        self.__string += str(current.value) + ', ' #append current value into string
        self._rpre_order(current.left) #go left
        self._rpre_order(current.right) #go right

  def post_order(self):
    if self.__root is None:
        return '[ ]'
    self.__string = '[ '
    if self.__root is not None:
        self._rpost_order(self.__root) #start at root, always
        self.__string = self.__string[:-2]
        self.__string+= ' ]'
        return self.__string
  def _rpost_order(self, current): #private recursive post order method
    if current is not None:
        self._rpost_order(current.left)
        self._rpost_order(current.right)
        self.__string += str(current.value)+ ', '

  def to_list(self):
    self._rlist(self.__root)
    return self.__list

  def _rlist(self, current):
    if current is not None: #when current node we are standing isn't None
        self._rlist(current.left)
        self.__list+= [current.value]
        self._rlist(current.right)

  def get_height(self):
    if self.__root is None:
        return 0
    return self.__root.height

  def __str__(self):
    return self.in_order()
