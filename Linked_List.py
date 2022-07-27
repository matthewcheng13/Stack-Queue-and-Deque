class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      # declare and initialize the public attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation
      self.value = val
      self.previous = None
      self.next = None

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    # TODO replace pass with your implementation
    self.__header = Linked_List.__Node(None)
    self.__trailer = Linked_List.__Node(None)
    self.__header.next = self.__trailer
    self.__trailer.previous = self.__header
    self.__size = 0

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    # TODO replace pass with your implementation
    return self.__size

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation
    newest = Linked_List.__Node(val)
    newest.previous = self.__trailer.previous
    newest.next = self.__trailer
    self.__trailer.previous = newest
    newest.previous.next = newest
    self.__size += 1

  def __get_node(self, index):
    # to avoid repeating the same code for 
    # insert, remove, or get element at, this private method
    # will determine whether the size is even or odd,
    # and then current walk accordingly. It will then
    # return the desired node.
    if index not in range(self.__size):
      raise IndexError
    if index < (self.__size + 1) // 2:
      cur = self.__header.next
      for i in range(index):
        cur = cur.next
    else:
      cur = self.__trailer
      for i in range(self.__size-index):
        cur = cur.previous
    return cur

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.
    # TODO replace pass with your implementation
    cur = self.__get_node(index)
    newest = Linked_List.__Node(val)
    newest.previous = cur.previous
    newest.next = cur
    cur.previous = newest
    newest.previous.next = newest
    self.__size += 1

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation
    cur = self.__get_node(index)
    cur.previous.next = cur.next
    cur.next.previous = cur.previous
    self.__size -= 1
    return cur.value

  def get_element_at(self, index):
      # assuming the head position (not the header node)
      # is indexed 0, return the value stored in the node 
      # at the specified index, but do not unlink it from 
      # the list. If the specified index is invalid, raise 
      # an IndexError exception.
      # TODO replace pass with your implementation
      cur = self.__get_node(index)
      return cur.value

  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    # TODO replace pass with your implementation.
    if self.__size < 2:
      return
    cur = self.__header.next
    cur.next.previous = self.__header
    self.__header.next = cur.next
    cur.previous = self.__trailer.previous
    self.__trailer.previous.next = cur
    self.__trailer.previous = cur
    cur.next = self.__trailer
    
  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
    if self.__size == 0:
      return '[ ]'
    string = '[ '
    cur = self.__header
    for i in self:
      cur = cur.next
      value = cur.value
      string += str(value) + ', '
    return string[0:-2] + ' ]'

  def __iter__(self):
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
    self.__iter_index = 0
    self.__cur = self.__header.next
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation
    if self.__cur == self.__trailer:
        raise StopIteration
    val = self.__cur.value
    self.__iter_index += 1
    self.__cur = self.__cur.next
    return val

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests

  # messages to avoid repeating code
  good = 'Correctly caught out of cells'
  error = 'Error: Unexpected out of cells'

  ll = Linked_List()

  # empty list
  # testing str and len methods
  print('Should say "[ ]"')
  print(str(ll))
  print('Should say 0')
  print(len(ll))
  # verifying that insert, remove, and get return IndexErrors
  # for an empty list
  print('Should say six correct messages and [ ]:')
  try:
    ll.insert_element_at(2,0)
  except IndexError:
    print(good)
  print(str(ll))
  try:
    ll.insert_element_at(2,1)
  except IndexError:
    print(good)
  print(str(ll))
  try:
    print(ll.remove_element_at(0))
  except IndexError:
    print(good)
  print(str(ll))
  try:
    print(ll.remove_element_at(1))
  except IndexError:
    print(good)
  print(str(ll))
  try:
    print(ll.get_element_at(0))
  except IndexError:
    print(good)
  print(str(ll))
  try:
    print(ll.get_element_at(1))
  except IndexError:
    print(good)
  print(str(ll))
  # making sure rotate_left() does nothing but also does not crash the program
  ll.rotate_left()
  print('Should still be "[ ]"')
  print(str(ll))
  # verifying that __iter__ and __next__ do nothing for an
  # empty list but also do not raise any errors
  print('Should not have anything printed before next "should say..." statement')
  for val in ll:
    print(val)
  
  # list with one element
  ll.append_element(1)
  # testing str and len methods
  print('Should say "[ 1 ]"')
  print(str(ll))
  # also confirms that appending an element did increment the size by 1
  print('Should say 1')
  print(len(ll))
  # verifying that remove, insert, and get element at all
  # perform correctly and catch all index errors
  print('Should return 1 and change the length from 1 to 0')
  try:
    print(ll.remove_element_at(0))
  except IndexError:
    print(error)
  print(str(ll))
  print(len(ll))
  print('(Other than "should have" messages, should have three correct messages and two returned values in between (2 and 1)')
  ll.append_element(1)
  try:
    ll.insert_element_at(2,0)
  except IndexError:
    print(error)
  print(f'Should be [ 2, 1 ]:{str(ll)}')
  print(f'Should be 2: {len(ll)}')
  try:
    ll.insert_element_at(2,3)
  except IndexError:
    print(good)
  print(f'Should still be [ 2, 1 ]:{str(ll)}')
  try:
    print(ll.remove_element_at(0))
  except IndexError:
    print(error)
  print(f'Should be [ 1 ]:{str(ll)}')
  print(f'Should be 1: {len(ll)}')
  try:
    print(ll.remove_element_at(3))
  except IndexError:
    print(good)
  print(f'Should still be [ 1 ]:{str(ll)}')
  try:
    print(ll.get_element_at(0))
  except IndexError:
    print(error)
  print(f'Should be [ 1 ]:{str(ll)}')
  print(f'Should be 1: {len(ll)}')
  try:
    print(ll.get_element_at(3))
  except IndexError:
    print(good)
  print(f'Should be [ 1 ]:{str(ll)}')
  # making sure rotate_left() does nothing
  ll.rotate_left()
  print('Should still be "[ 1 ]"')
  print(str(ll))
  # test __iter__ and __next__
  print('Should print 1')
  for val in ll:
    print(val)
  
  # list with multiple elements
  ll.append_element(2)
  ll.append_element(3)
  # testing str and len methods
  print('Should say "[ 1, 2, 3 ]":')
  print(str(ll))
  # also confirms that insert_element_at() did increment the size
  print('Should say 3:')
  print(len(ll))
  # verifying that remove, insert, and get element at all
  # perform correctly and catch all index errors
  print('Should have three correct messages and two returned values in between (2 and 1)')
  try:
    ll.insert_element_at(2,2)
  except IndexError:
    print(error)
  print(f'Should be [ 1, 2, 2, 3 ]:{str(ll)}')
  print(f'Should be 4: {len(ll)}')
  try:
    ll.insert_element_at(2,5)
  except IndexError:
    print(good)
  print(f'Should still be [ 1, 2, 2, 3 ]:{str(ll)}')
  try:
    print(ll.remove_element_at(2))
  except IndexError:
    print(error)
  print(f'Should be [ 1, 2, 3 ]:{str(ll)}')
  print(f'Should be 3: {len(ll)}')
  try:
    print(ll.remove_element_at(5))
  except IndexError:
    print(good)
  print(f'Should still be [ 1, 2, 3 ]:{str(ll)}')
  try:
    print(ll.get_element_at(0))
  except IndexError:
    print(error)
  print(f'Should still be [ 1, 2, 3 ]:{str(ll)}')
  print(f'Should be 3: {len(ll)}')
  try:
    print(ll.get_element_at(5))
  except IndexError:
    print(good)
  print(f'Should still be [ 1, 2, 3 ]:{str(ll)}')
  # check to see that rotate_left() actually does rotate left
  ll.rotate_left()
  print('Should be "[ 2, 3, 1 ]"')
  print(str(ll))
  # test __iter__ and __next__
  print('Should print 2 then 3 then 1')
  for val in ll:
    print(val)