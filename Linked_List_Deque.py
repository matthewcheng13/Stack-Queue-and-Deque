from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  
  def push_front(self, val):
    # TODO replace pass with your implementation.
    if len(self.__list) == 0:
      self.__list.append_element(val)
    else:
      self.__list.insert_element_at(val,0)
  
  def pop_front(self):
    # TODO replace pass with your implementation.
    if len(self.__list) == 0:
      return None
    else:
      return self.__list.remove_element_at(0)

  def peek_front(self):
    # TODO replace pass with your implementation.
    if len(self.__list) == 0:
      return None
    else:
      return self.__list.get_element_at(0)

  def push_back(self, val):
    # TODO replace pass with your implementation.
    self.__list.append_element(val)
  
  def pop_back(self):
    # TODO replace pass with your implementation.
    if len(self.__list) == 0:
      return None
    else:
      return self.__list.remove_element_at(len(self.__list)-1)

  def peek_back(self):
    # TODO replace pass with your implementation.
    if len(self.__list) == 0:
      return None
    else:
      return self.__list.get_element_at(len(self.__list)-1)

# Unit tests make the main section unneccessary.
if __name__ == '__main__':
  dq = Linked_List_Deque()

  print('0, [ ]')
  print(len(dq))
  print(dq)
  print(' ')

  print('1, [ 3 ]')
  dq.push_front(3)
  print(len(dq))
  print(dq)
  print(' ')

  print('3, 0, [ ]')
  print(dq.pop_back())
  print(len(dq))
  print(dq)
  print(' ')

  print('2, [ 1, 2 ]')
  dq.push_back(2)
  dq.push_front(1)
  print(len(dq))
  print(dq)
  print(' ')

  print('1, 2, 1')
  print(dq.peek_front(),dq.peek_back())
  print(dq.pop_front())

