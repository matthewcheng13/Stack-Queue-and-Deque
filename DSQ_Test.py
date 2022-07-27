import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # SECTION 1: DEQUE TEST
  def test_empty_string_d(self):
    self.assertEqual('[ ]',str(self.__deque))

  # push_front and push_back
  def test_push_front_empty_d(self):
    self.__deque.push_front('Front')
    self.assertEqual('[ Front ]',str(self.__deque))

  def test_push_back_empty_d(self):
    self.__deque.push_back('Back')
    self.assertEqual('[ Back ]',str(self.__deque))

  def test_push_front_twice_d(self):
    self.__deque.push_front('Front')
    self.__deque.push_front('Front')
    self.assertEqual('[ Front, Front ]',str(self.__deque))

  def test_push_back_twice_d(self):
    self.__deque.push_back('Back')
    self.__deque.push_back('Back')
    self.assertEqual('[ Back, Back ]',str(self.__deque))

  def test_push_front_back_d(self):
    self.__deque.push_front('Front')
    self.__deque.push_back('Back')
    self.assertEqual('[ Front, Back ]',str(self.__deque))

  def test_push_back_front_d(self):
    self.__deque.push_back('Back')
    self.__deque.push_front('Front')
    self.assertEqual('[ Front, Back ]',str(self.__deque))

  def test_push_front_back_front_d(self):
    self.__deque.push_front('Front')
    self.__deque.push_back('Back')
    self.__deque.push_front('Front')
    self.assertEqual('[ Front, Front, Back ]',str(self.__deque))

  def test_push_back_front_back_d(self):
    self.__deque.push_back('Back')
    self.__deque.push_front('Front')
    self.__deque.push_back('Back')
    self.assertEqual('[ Front, Back, Back ]',str(self.__deque))

  def test_push_front_three_times_d(self):
    self.__deque.push_front('Front')
    self.__deque.push_front('Front')
    self.__deque.push_front('Front')
    self.assertEqual('[ Front, Front, Front ]',str(self.__deque))

  def test_push_back_three_times_d(self):
    self.__deque.push_back('Back')
    self.__deque.push_back('Back')
    self.__deque.push_back('Back')
    self.assertEqual('[ Back, Back, Back ]',str(self.__deque))

  # length function and ensuring push increments size
  def test_get_empty_length_d(self):
    self.assertEqual(0,len(self.__deque))

  def test_get_one_length_front_d(self):
    self.__deque.push_front('Front')
    self.assertEqual(1,len(self.__deque))

  def test_get_one_length_back_d(self):
    self.__deque.push_back('Back')
    self.assertEqual(1,len(self.__deque))

  def test_get_two_length_front_d(self):
    self.__deque.push_front('Front')
    self.__deque.push_front('Front')
    self.assertEqual(2,len(self.__deque))

  def test_get_two_length_back_d(self):
    self.__deque.push_back('Back')
    self.__deque.push_back('Back')
    self.assertEqual(2,len(self.__deque))

  def test_get_two_length_front_back_d(self):
    self.__deque.push_front('Front')
    self.__deque.push_back('Back')
    self.assertEqual(2,len(self.__deque))

  def test_get_two_length_back_front_d(self):
    self.__deque.push_back('Back')
    self.__deque.push_front('Front')
    self.assertEqual(2,len(self.__deque))

  # pop_front and pop_back
  def test_pop_front_leaving_zero_value_d(self):
    self.__deque.push_front('Pop')
    returned = self.__deque.pop_front()
    self.assertEqual('Pop',returned)

  def test_pop_front_leaving_zero_remaining_d(self):
    self.__deque.push_front('Pop')
    returned = self.__deque.pop_front()
    self.assertEqual('[ ]',str(self.__deque))

  def test_pop_front_leaving_zero_length_d(self):
    self.__deque.push_front('Pop')
    returned = self.__deque.pop_front()
    self.assertEqual(0,len(self.__deque))

  def test_pop_back_leaving_zero_value_d(self):
    self.__deque.push_front('Pop')
    returned = self.__deque.pop_back()
    self.assertEqual('Pop',returned)

  def test_pop_back_leaving_zero_remaining_d(self):
    self.__deque.push_front('Pop')
    returned = self.__deque.pop_back()
    self.assertEqual('[ ]',str(self.__deque))

  def test_pop_back_leaving_zero_length_d(self):
    self.__deque.push_front('Pop')
    returned = self.__deque.pop_back()
    self.assertEqual(0,len(self.__deque))

  def test_pop_front_leaving_one_value_d(self):
    self.__deque.push_front('Pop')
    self.__deque.push_front('Corn')
    returned = self.__deque.pop_front()
    self.assertEqual('Corn',returned)

  def test_pop_front_leaving_one_remaining_d(self):
    self.__deque.push_front('Pop')
    self.__deque.push_front('Corn')
    returned = self.__deque.pop_front()
    self.assertEqual('[ Pop ]',str(self.__deque))

  def test_pop_front_leaving_one_length_d(self):
    self.__deque.push_front('Pop')
    self.__deque.push_front('Corn')
    returned = self.__deque.pop_front()
    self.assertEqual(1,len(self.__deque))

  def test_pop_back_leaving_one_value_d(self):
    self.__deque.push_front('Pop')
    self.__deque.push_front('Corn')
    returned = self.__deque.pop_back()
    self.assertEqual('Pop',returned)

  def test_pop_back_leaving_one_remaining_d(self):
    self.__deque.push_front('Pop')
    self.__deque.push_front('Corn')
    returned = self.__deque.pop_back()
    self.assertEqual('[ Corn ]',str(self.__deque))

  def test_pop_back_leaving_one_length_d(self):
    self.__deque.push_front('Pop')
    self.__deque.push_front('Corn')
    returned = self.__deque.pop_back()
    self.assertEqual(1,len(self.__deque))

  def test_pop_front_twice_value_d(self):
    self.__deque.push_front('Back')
    self.__deque.push_front('Middle')
    self.__deque.push_front('Front')
    self.assertEqual('Front',self.__deque.pop_front())
    self.assertEqual('Middle',self.__deque.pop_front())

  def test_pop_front_twice_remaining_d(self):
    self.__deque.push_front('Back')
    self.__deque.push_front('Middle')
    self.__deque.push_front('Front')
    action1 = self.__deque.pop_front()
    self.assertEqual('[ Middle, Back ]',str(self.__deque))
    action2 = self.__deque.pop_front()
    self.assertEqual('[ Back ]',str(self.__deque))

  def test_pop_front_twice_length_d(self):
    self.__deque.push_front('Back')
    self.__deque.push_front('Middle')
    self.__deque.push_front('Front')
    action1 = self.__deque.pop_front()
    self.assertEqual(2,len(self.__deque))
    action2 = self.__deque.pop_front()
    self.assertEqual(1,len(self.__deque))

  def test_pop_back_twice_value_d(self):
    self.__deque.push_front('Back')
    self.__deque.push_front('Middle')
    self.__deque.push_front('Front')
    self.assertEqual('Back',self.__deque.pop_back())
    self.assertEqual('Middle',self.__deque.pop_back())

  def test_pop_back_twice_remaining_d(self):
    self.__deque.push_front('Back')
    self.__deque.push_front('Middle')
    self.__deque.push_front('Front')
    action1 = self.__deque.pop_back()
    self.assertEqual('[ Front, Middle ]',str(self.__deque))
    action2 = self.__deque.pop_back()
    self.assertEqual('[ Front ]',str(self.__deque))

  def test_pop_back_twice_length_d(self):
    self.__deque.push_front('Back')
    self.__deque.push_front('Middle')
    self.__deque.push_front('Front')
    action1 = self.__deque.pop_back()
    self.assertEqual(2,len(self.__deque))
    action2 = self.__deque.pop_back()
    self.assertEqual(1,len(self.__deque))

  # peek_front and peek_back
  def test_peek_front_with_one_d(self):
    self.__deque.push_front('Peek')
    returned = self.__deque.peek_front()
    self.assertEqual('Peek',returned)

  def test_peek_front_with_one_remaining_d(self):
    self.__deque.push_front('Peek')
    returned = self.__deque.peek_front()
    self.assertEqual('[ Peek ]',str(self.__deque))

  def test_peek_front_with_one_length_d(self):
    self.__deque.push_front('Peek')
    returned = self.__deque.peek_front()
    self.assertEqual(1,len(self.__deque))

  def test_peek_back_with_one_value_d(self):
    self.__deque.push_front('Peek')
    returned = self.__deque.peek_back()
    self.assertEqual('Peek',returned)

  def test_peek_back_with_one_remaining_d(self):
    self.__deque.push_front('Peek')
    returned = self.__deque.peek_back()
    self.assertEqual('[ Peek ]',str(self.__deque))

  def test_peek_back_with_one_length_d(self):
    self.__deque.push_front('Peek')
    returned = self.__deque.peek_back()
    self.assertEqual(1,len(self.__deque))

  def test_peek_front_with_two_value_d(self):
    self.__deque.push_front('Peek')
    self.__deque.push_front('Boo')
    returned = self.__deque.peek_front()
    self.assertEqual('Boo',returned)

  def test_peek_front_with_two_remaining_d(self):
    self.__deque.push_front('Peek')
    self.__deque.push_front('Boo')
    returned = self.__deque.peek_front()
    self.assertEqual('[ Boo, Peek ]',str(self.__deque))

  def test_peek_front_with_two_length_d(self):
    self.__deque.push_front('Peek')
    self.__deque.push_front('Boo')
    returned = self.__deque.peek_front()
    self.assertEqual(2,len(self.__deque))

  def test_peek_back_with_two_value_d(self):
    self.__deque.push_front('Peek')
    self.__deque.push_front('Boo')
    returned = self.__deque.peek_back()
    self.assertEqual('Peek',returned)

  def test_peek_back_with_two_remaining_d(self):
    self.__deque.push_front('Peek')
    self.__deque.push_front('Boo')
    returned = self.__deque.peek_back()
    self.assertEqual('[ Boo, Peek ]',str(self.__deque))

  def test_peek_back_with_two_length_d(self):
    self.__deque.push_front('Peek')
    self.__deque.push_front('Boo')
    returned = self.__deque.peek_back()
    self.assertEqual(2,len(self.__deque))
    
  # checking cases where nothing happens or nothing is returned
  def test_pop_front_with_empty_d(self):
    self.assertEqual(None,self.__deque.pop_front())

  def test_pop_back_with_empty_d(self):
    self.assertEqual(None,self.__deque.pop_back())

  def test_peek_front_with_empty_d(self):
    self.assertEqual(None,self.__deque.peek_front())

  def test_peek_back_with_empty_d(self):
    self.assertEqual(None,self.__deque.peek_back())

  def test_pop_front_twice_with_one_d(self):
    self.__deque.push_front('Pop')
    self.__deque.pop_front()
    returned = self.__deque.pop_front()
    self.assertEqual(None,returned)

  def test_pop_back_twice_with_one_d(self):
    self.__deque.push_front('Pop')
    self.__deque.pop_back()
    returned = self.__deque.pop_back()
    self.assertEqual(None,returned)

  def test_pop_front_back_with_one_d(self):
    self.__deque.push_front('Pop')
    self.__deque.pop_front()
    returned = self.__deque.pop_back()
    self.assertEqual(None,returned)

  def test_pop_back_front_with_one_d(self):
    self.__deque.push_front('Pop')
    self.__deque.pop_back()
    returned = self.__deque.pop_front()
    self.assertEqual(None,returned)





  # SECTION 2: STACK TEST
  def test_empty_string_s(self):
    self.assertEqual('[ ]', str(self.__stack))

  # testing push
  def test_push_empty_s(self):
    self.__stack.push('Overflow')
    self.assertEqual('[ Overflow ]', str(self.__stack))

  def test_push_one_s(self):
    self.__stack.push('Overflow')
    self.__stack.push('Exchange')
    self.assertEqual('[ Exchange, Overflow ]', str(self.__stack))

  def test_push_two_s(self):
    self.__stack.push('Overflow')
    self.__stack.push('Exchange')
    self.__stack.push('Cup')
    self.assertEqual('[ Cup, Exchange, Overflow ]', str(self.__stack))

  # testing length
  def test_get_empty_length_s(self):
    self.assertEqual(0, len(self.__stack))

  def test_get_one_length_s(self):
    self.__stack.push('Overflow')
    self.assertEqual(1, len(self.__stack))

  def test_get_two_length_s(self):
    self.__stack.push('Overflow')
    self.__stack.push('Exchange')
    self.assertEqual(2, len(self.__stack))

  # testing pop
  def test_pop_leaving_zero_value_s(self):
    self.__stack.push('Overflow')
    returned = self.__stack.pop()
    self.assertEqual('Overflow', returned)

  def test_pop_leaving_zero_remaining_s(self):
    self.__stack.push('Overflow')
    returned = self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_leaving_zero_length_s(self):
    self.__stack.push('Overflow')
    returned = self.__stack.pop()
    self.assertEqual(0, len(self.__stack))

  def test_pop_leaving_one_s(self):
    self.__stack.push('Overflow')
    self.__stack.push('Exchange')
    returned = self.__stack.pop()
    self.assertEqual('Exchange', returned)

  def test_pop_leaving_one_remaining_s(self):
    self.__stack.push('Overflow')
    self.__stack.push('Exchange')
    returned = self.__stack.pop()
    self.assertEqual('[ Overflow ]', str(self.__stack))

  def test_pop_leaving_one_length_s(self):
    self.__stack.push('Overflow')
    self.__stack.push('Exchange')
    returned = self.__stack.pop()
    self.assertEqual(1, len(self.__stack))

  def test_pop_twice_value_s(self):
    self.__stack.push('Back')
    self.__stack.push('Middle')
    self.__stack.push('Front')
    self.assertEqual('Front',self.__stack.pop())
    self.assertEqual('Middle',self.__stack.pop())

  def test_pop_twice_remaining_s(self):
    self.__stack.push('Back')
    self.__stack.push('Middle')
    self.__stack.push('Front')
    action1 = self.__stack.pop()
    self.assertEqual('[ Middle, Back ]',str(self.__stack))
    action2 = self.__stack.pop()
    self.assertEqual('[ Back ]',str(self.__stack))

  def test_pop_twice_length_s(self):
    self.__stack.push('Back')
    self.__stack.push('Middle')
    self.__stack.push('Front')
    action1 = self.__stack.pop()
    self.assertEqual(2,len(self.__stack))
    action2 = self.__stack.pop()
    self.assertEqual(1,len(self.__stack))

  # testing peek
  def test_peek_with_one_s(self):
    self.__stack.push('Overflow')
    returned = self.__stack.peek()
    self.assertEqual('Overflow', returned)

  def test_peek_with_one_remaining_s(self):
    self.__stack.push('Overflow')
    returned = self.__stack.peek()
    self.assertEqual('[ Overflow ]', str(self.__stack))

  def test_peek_with_one_length_s(self):
    self.__stack.push('Overflow')
    returned = self.__stack.peek()
    self.assertEqual(1, len(self.__stack))

  def test_peek_with_two_s(self):
    self.__stack.push('Overflow')
    self.__stack.push('Exchange')
    returned = self.__stack.peek()
    self.assertEqual('Exchange', returned)

  def test_peek_with_two_remaining_s(self):
    self.__stack.push('Overflow')
    self.__stack.push('Exchange')
    returned = self.__stack.peek()
    self.assertEqual('[ Exchange, Overflow ]', str(self.__stack))

  def test_peek_with_two_length_s(self):
    self.__stack.push('Overflow')
    self.__stack.push('Exchange')
    returned = self.__stack.peek()
    self.assertEqual(2, len(self.__stack))

  # testing None cases
  def test_pop_with_empty_s(self):
    self.assertEqual(None,self.__stack.pop())

  def test_peek_with_empty_s(self):
    self.assertEqual(None,self.__stack.peek())
  




  # SECTION 3: QUEUE TEST
  def test_empty_string_q(self):
    self.assertEqual('[ ]', str(self.__queue))

  # enqueue
  def test_enqueue_empty_q(self):
    self.__queue.enqueue('Ball')
    self.assertEqual('[ Ball ]', str(self.__queue))

  def test_enqueue_one_q(self):
    self.__queue.enqueue('Ball')
    self.__queue.enqueue('Tip')
    self.assertEqual('[ Ball, Tip ]', str(self.__queue))

  def test_enqueue_two_q(self):
    self.__queue.enqueue('Ball')
    self.__queue.enqueue('Tip')
    self.__queue.enqueue('Call')
    self.assertEqual('[ Ball, Tip, Call ]', str(self.__queue))

  # length
  def test_get_empty_length_q(self):
    self.assertEqual(0, len(self.__queue))

  def test_get_one_length_q(self):
    self.__queue.enqueue('Ball')
    self.assertEqual(1, len(self.__queue))

  def test_get_two_length_q(self):
    self.__queue.enqueue('Ball')
    self.__queue.enqueue('Tip')
    self.assertEqual(2, len(self.__queue))

  # dequeue
  def test_dequeue_leaving_zero_value_q(self):
    self.__queue.enqueue('Ball')
    returned = self.__queue.dequeue()
    self.assertEqual('Ball', returned)

  def test_dequeue_leaving_zero_remaining_q(self):
    self.__queue.enqueue('Ball')
    returned = self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_leaving_zero_length_q(self):
    self.__queue.enqueue('Ball')
    returned = self.__queue.dequeue()
    self.assertEqual(0, len(self.__queue))

  def test_dequeue_leaving_one_q(self):
    self.__queue.enqueue('Ball')
    self.__queue.enqueue('Tip')
    returned = self.__queue.dequeue()
    self.assertEqual('Ball', returned)

  def test_dequeue_leaving_one_remaining_q(self):
    self.__queue.enqueue('Ball')
    self.__queue.enqueue('Tip')
    returned = self.__queue.dequeue()
    self.assertEqual('[ Tip ]', str(self.__queue))

  def test_dequeue_leaving_one_length_q(self):
    self.__queue.enqueue('Ball')
    self.__queue.enqueue('Tip')
    returned = self.__queue.dequeue()
    self.assertEqual(1, len(self.__queue))

  def test_dequeue_twice_value_q(self):
    self.__queue.enqueue('Front')
    self.__queue.enqueue('Middle')
    self.__queue.enqueue('Back')
    self.assertEqual('Front',self.__queue.dequeue())
    self.assertEqual('Middle',self.__queue.dequeue())

  def test_dequeue_twice_remaining_q(self):
    self.__queue.enqueue('Front')
    self.__queue.enqueue('Middle')
    self.__queue.enqueue('Back')
    action1 = self.__queue.dequeue()
    self.assertEqual('[ Middle, Back ]',str(self.__queue))
    action2 = self.__queue.dequeue()
    self.assertEqual('[ Back ]',str(self.__queue))

  def test_dequeue_twice_length_q(self):
    self.__queue.enqueue('Front')
    self.__queue.enqueue('Middle')
    self.__queue.enqueue('Back')
    action1 = self.__queue.dequeue()
    self.assertEqual(2,len(self.__queue))
    action2 = self.__queue.dequeue()
    self.assertEqual(1,len(self.__queue))

  # peek
  def test_peek_with_one_q(self):
    self.__queue.enqueue('Ball')
    returned = self.__queue.peek()
    self.assertEqual('Ball', returned)

  def test_peek_with_one_remaining_q(self):
    self.__queue.enqueue('Ball')
    returned = self.__queue.peek()
    self.assertEqual('[ Ball ]', str(self.__queue))

  def test_peek_with_one_length_q(self):
    self.__queue.enqueue('Ball')
    returned = self.__queue.peek()
    self.assertEqual(1, len(self.__queue))

  def test_peek_with_two_q(self):
    self.__queue.enqueue('Ball')
    self.__queue.enqueue('Tip')
    returned = self.__queue.peek()
    self.assertEqual('Ball', returned)

  def test_peek_with_two_remaining_q(self):
    self.__queue.enqueue('Ball')
    self.__queue.enqueue('Tip')
    returned = self.__queue.peek()
    self.assertEqual('[ Ball, Tip ]', str(self.__queue))

  def test_peek_with_two_length_q(self):
    self.__queue.enqueue('Ball')
    self.__queue.enqueue('Tip')
    returned = self.__queue.peek()
    self.assertEqual(2, len(self.__queue))

  # None cases
  def test_pop_with_empty_q(self):
    self.assertEqual(None,self.__queue.dequeue())

  def test_peek_with_empty_q(self):
    self.assertEqual(None,self.__queue.peek())




if __name__ == '__main__':
  unittest.main()

