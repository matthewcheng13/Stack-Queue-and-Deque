from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    self.__front = None
    self.__back = None
    self.__size = 0
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    if self.__size == 0:
      return '[ ]'
    string = '[ '
    cur = self.__front
    for i in range(self.__size):
      value = self.__contents[cur]
      string += str(value) + ', '
      cur = (cur + 1) % self.__capacity
    return string[0:-2] + ' ]'
    
  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.__size

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    temp = [None] * self.__capacity
    size = self.__size
    for i in range(self.__capacity):
      temp[i] = self.pop_front()
    self.__size = size
    self.__contents = temp
    self.__contents += ([None] * self.__capacity)
    self.__capacity *= 2
    self.__front = 0
    self.__back = self.__size - 1
    
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__capacity == self.__size:
      self.__grow()
    if self.__size == 0:
      self.__front = 0
      self.__back = 0
    else:
      self.__front = (self.__front - 1) % self.__capacity
    self.__contents[self.__front] = val
    self.__size += 1
    
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size == 0:
      return None
    elif self.__size == 1:
      to_return = self.__contents[self.__front]
      self.__front = None
      self.__back = None
      self.__size -= 1
      return to_return
    else:
      to_return = self.__contents[self.__front]
      self.__front = (self.__front + 1) % self.__capacity
      self.__size -= 1
      return to_return
    
  def peek_front(self):
    # TODO replace pass with your implementation.
    if self.__size == 0:
      return None
    return self.__contents[self.__front]
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__capacity == self.__size:
      self.__grow()
    if self.__size == 0:
      self.__front = 0
      self.__back = 0
    else:
      self.__back = (self.__back + 1) % self.__capacity
    self.__contents[self.__back] = val
    self.__size += 1
  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size == 0:
      return None
    elif self.__size == 1:
      to_return = self.__contents[self.__back]
      self.__front = None
      self.__back = None
      self.__size -= 1
      return to_return
    else:
      to_return = self.__contents[self.__back]
      self.__back = (self.__back - 1) % self.__capacity
      self.__size -= 1
      return to_return

  def peek_back(self):
    # TODO replace pass with your implementation.
    if self.__size == 0:
      return None
    return self.__contents[self.__back]

# No main section is necessary. Unit tests take its place.
if __name__ == '__main__':
  dq = Array_Deque()

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

  dq.push_back(3)
  dq.push_back(4)
  dq.push_back(5)
  print(dq)