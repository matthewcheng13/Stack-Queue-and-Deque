from Linked_List import Linked_List
import unittest

class Linked_List_Tester(unittest.TestCase):

    def setUp(self):
      self.__list = Linked_List()

    def test_empty_list_string(self):
      self.assertEqual('[ ]', str(self.__list))

    def test_empty_list_length(self):
      self.assertEqual(0, len(self.__list))

    def test_add_string_head_empty(self):
      self.__list.append_element('Hello')
      self.assertEqual('[ Hello ]',str(self.__list))

    def test_add_int_head_empty(self):
      self.__list.append_element(1)
      self.assertEqual('[ 1 ]',str(self.__list))

    def test_add_string_tail_with_one(self):
      self.__list.append_element('Hello')
      self.__list.append_element('there')
      self.assertEqual('[ Hello, there ]',str(self.__list))

    def test_add_int_tail_with_one(self):
      self.__list.append_element(1)
      self.__list.append_element(2)
      self.assertEqual('[ 1, 2 ]',str(self.__list))

    def test_add_string_head_with_one(self):
      self.__list.append_element('Hello')
      self.__list.insert_element_at('Well',0)
      self.assertEqual('[ Well, Hello ]',str(self.__list))

    def test_add_int_head_with_one(self):
      self.__list.append_element(1)
      self.__list.insert_element_at(0,0)
      self.assertEqual('[ 0, 1 ]',str(self.__list))
    
    def test_add_string_tail_with_two(self):
      self.__list.append_element('Hello')
      self.__list.append_element('there')
      self.__list.append_element('computer')
      self.assertEqual('[ Hello, there, computer ]',str(self.__list))

    def test_add_int_tail_with_two(self):
      self.__list.append_element(1)
      self.__list.append_element(2)
      self.__list.append_element(3)
      self.assertEqual('[ 1, 2, 3 ]',str(self.__list))

    def test_add_string_head_with_two(self):
      self.__list.append_element('Hello')
      self.__list.append_element('there')
      self.__list.insert_element_at('Well',0)
      self.assertEqual('[ Well, Hello, there ]',str(self.__list))

    def test_add_int_head_with_two(self):
      self.__list.append_element(1)
      self.__list.append_element(2)
      self.__list.insert_element_at(0,0)
      self.assertEqual('[ 0, 1, 2 ]',str(self.__list))

    def test_add_string_middle_with_two(self):
      self.__list.append_element('Hello')
      self.__list.append_element('there')
      self.__list.insert_element_at('over',1)
      self.assertEqual('[ Hello, over, there ]',str(self.__list))

    def test_add_int_middle_with_two(self):
      self.__list.append_element(0)
      self.__list.append_element(2)
      self.__list.insert_element_at(1,1)
      self.assertEqual('[ 0, 1, 2 ]',str(self.__list))

    def test_add_string_second_of_four(self):
      self.__list.append_element('Hello')
      self.__list.append_element('over')
      self.__list.append_element('there')
      self.__list.insert_element_at('you',1)
      self.assertEqual('[ Hello, you, over, there ]',str(self.__list))

    def test_add_string_second_of_four(self):
      self.__list.append_element(0)
      self.__list.append_element(2)
      self.__list.append_element(3)
      self.__list.insert_element_at(1,1)
      self.assertEqual('[ 0, 1, 2, 3 ]',str(self.__list))

    def test_add_string_third_of_four(self):
      self.__list.append_element('Hello')
      self.__list.append_element('how')
      self.__list.append_element('you')
      self.__list.insert_element_at('are',2)
      self.assertEqual('[ Hello, how, are, you ]',str(self.__list))

    def test_add_string_third_of_four(self):
      self.__list.append_element(0)
      self.__list.append_element(1)
      self.__list.append_element(3)
      self.__list.insert_element_at(2,2)
      self.assertEqual('[ 0, 1, 2, 3 ]',str(self.__list))

    def test_get_one_length(self):
      self.__list.append_element('Word')
      self.assertEqual(1, len(self.__list))

    def test_get_two_length_append(self):
      self.__list.append_element('Word')
      self.__list.append_element('Word')
      self.assertEqual(2, len(self.__list))
    
    def test_get_two_length_insert(self):
      self.__list.append_element('Word')
      self.__list.insert_element_at('Word',0)
      self.assertEqual(2, len(self.__list))

    def test_get_three_length_insert(self):
      self.__list.append_element('Word')
      self.__list.append_element('Word')
      self.__list.insert_element_at('Word',1)
      self.assertEqual(3, len(self.__list))

    def test_remove_head_leaving_zero_returned(self):
      self.__list.append_element('Dungeon')
      returned = self.__list.remove_element_at(0)
      self.assertEqual('Dungeon',returned)

    def test_remove_head_leaving_zero_remaining(self):
      self.__list.append_element('Dungeon')
      returned = self.__list.remove_element_at(0)
      self.assertEqual('[ ]',str(self.__list))
    
    def test_remove_head_leaving_zero_length(self):
      self.__list.append_element('Dungeon')
      returned = self.__list.remove_element_at(0)
      self.assertEqual(0,len(self.__list))

    def test_remove_head_leaving_one_returned(self):
      self.__list.append_element('Dungeon')
      self.__list.append_element('Castle')
      returned = self.__list.remove_element_at(0)
      self.assertEqual('Dungeon',returned)

    def test_remove_head_leaving_one_remaining(self):
      self.__list.append_element('Dungeon')
      self.__list.append_element('Castle')
      returned = self.__list.remove_element_at(0)
      self.assertEqual('[ Castle ]',str(self.__list))
    
    def test_remove_head_leaving_one_length(self):
      self.__list.append_element('Dungeon')
      self.__list.append_element('Castle')
      returned = self.__list.remove_element_at(0)
      self.assertEqual(1,len(self.__list))

    def test_remove_tail_leaving_one_returned(self):
      self.__list.append_element('Dungeon')
      self.__list.append_element('Castle')
      returned = self.__list.remove_element_at(1)
      self.assertEqual('Castle',returned)

    def test_remove_tail_leaving_one_remaining(self):
      self.__list.append_element('Dungeon')
      self.__list.append_element('Castle')
      returned = self.__list.remove_element_at(1)
      self.assertEqual('[ Dungeon ]',str(self.__list))
    
    def test_remove_tail_leaving_one_length(self):
      self.__list.append_element('Dungeon')
      self.__list.append_element('Castle')
      returned = self.__list.remove_element_at(1)
      self.assertEqual(1,len(self.__list))

    def test_remove_middle_leaving_one_returned(self):
      self.__list.append_element('Dungeon')
      self.__list.append_element('Castle')
      self.__list.append_element('Tower')
      returned = self.__list.remove_element_at(1)
      self.assertEqual('Castle',returned)

    def test_remove_middle_leaving_one_remaining(self):
      self.__list.append_element('Dungeon')
      self.__list.append_element('Castle')
      self.__list.append_element('Tower')
      returned = self.__list.remove_element_at(1)
      self.assertEqual('[ Dungeon, Tower ]',str(self.__list))
    
    def test_remove_middle_leaving_one_length(self):
      self.__list.append_element('Dungeon')
      self.__list.append_element('Castle')
      self.__list.append_element('Tower')
      returned = self.__list.remove_element_at(1)
      self.assertEqual(2,len(self.__list))

    def test_get_head_with_one(self):
      self.__list.append_element('Dragon')
      returned = self.__list.get_element_at(0)
      self.assertEqual('Dragon',returned)

    def test_get_head_with_one_remaining(self):
      self.__list.append_element('Dragon')
      returned = self.__list.get_element_at(0)
      self.assertEqual('[ Dragon ]',str(self.__list))

    def test_get_head_with_one_length(self):
      self.__list.append_element('Dragon')
      returned = self.__list.get_element_at(0)
      self.assertEqual(1,len(self.__list))

    def test_get_tail_with_two(self):
      self.__list.append_element('Dragon')
      self.__list.append_element('Knight')
      returned = self.__list.get_element_at(1)
      self.assertEqual('Knight',returned)

    def test_get_tail_with_two_remaining(self):
      self.__list.append_element('Dragon')
      self.__list.append_element('Knight')
      returned = self.__list.get_element_at(1)
      self.assertEqual('[ Dragon, Knight ]',str(self.__list))

    def test_get_tail_with_two_length(self):
      self.__list.append_element('Dragon')
      self.__list.append_element('Knight')
      returned = self.__list.get_element_at(1)
      self.assertEqual(2,len(self.__list))

    def test_get_middle_with_three(self):
      self.__list.append_element('Dragon')
      self.__list.append_element('Knight')
      self.__list.append_element('Griffon')
      returned = self.__list.get_element_at(1)
      self.assertEqual('Knight',returned)

    def test_get_middle_with_three_remaining(self):
      self.__list.append_element('Dragon')
      self.__list.append_element('Knight')
      self.__list.append_element('Griffon')
      returned = self.__list.get_element_at(1)
      self.assertEqual('[ Dragon, Knight, Griffon ]',str(self.__list))

    def test_get_middle_with_three_length(self):
      self.__list.append_element('Dragon')
      self.__list.append_element('Knight')
      self.__list.append_element('Griffon')
      returned = self.__list.get_element_at(1)
      self.assertEqual(3,len(self.__list))

    def test_add_at_negative_index_ignore(self):
      with self.assertRaises(IndexError):
        self.__list.insert_element_at('Word',-1)
      self.assertEqual('[ ]',str(self.__list))

    def test_remove_at_negative_index_ignore(self):
      with self.assertRaises(IndexError):
        self.__list.remove_element_at(-1)
      self.assertEqual('[ ]',str(self.__list))

    def test_get_at_negative_index_ignore(self):
      with self.assertRaises(IndexError):
        self.__list.get_element_at(-1)
      self.assertEqual('[ ]',str(self.__list))

    def test_add_at_zero_index_ignore(self):
      with self.assertRaises(IndexError):
        self.__list.insert_element_at('Word',0)
      self.assertEqual('[ ]',str(self.__list))

    def test_remove_at_zero_index_ignore(self):
      with self.assertRaises(IndexError):
        self.__list.remove_element_at(0)
      self.assertEqual('[ ]',str(self.__list))

    def test_get_at_zero_index_ignore(self):
      with self.assertRaises(IndexError):
        self.__list.get_element_at(0)
      self.assertEqual('[ ]',str(self.__list))

    def test_add_at_one_past_index_ignore(self):
      self.__list.append_element('Zero')
      with self.assertRaises(IndexError):
        self.__list.insert_element_at('Word',1)
      self.assertEqual('[ Zero ]',str(self.__list))

    def test_remove_at_one_past_index_ignore(self):
      self.__list.append_element('Zero')
      with self.assertRaises(IndexError):
        self.__list.remove_element_at(1)
      self.assertEqual('[ Zero ]',str(self.__list))

    def test_get_at_one_past_index_ignore(self):
      self.__list.append_element('Zero')
      with self.assertRaises(IndexError):
        self.__list.get_element_at(1)
      self.assertEqual('[ Zero ]',str(self.__list))

    def test_empty_iterator(self):
      for value in self.__list:
        self.fail()

    def test_one_iterator(self):
      self.__list.append_element('Iterate')
      count = 0
      for value in self.__list:
        self.assertEqual('Iterate',value)
        count += 1
      self.assertEqual(1, count)

    def test_multiple_iterator(self):
      strs = [ 'One', 'Two', 'Three']
      self.__list.append_element(strs[0])
      self.__list.append_element(strs[1])
      self.__list.append_element(strs[2])
      count = 0
      for value in self.__list:
        self.assertEqual(strs[count],value)
        count += 1
      self.assertEqual(3, count)

    def test_rotate_left_empty(self):
      self.__list.rotate_left()
      self.assertEqual('[ ]', str(self.__list))

    def test_rotate_left_one(self):
      self.__list.append_element('Rotate')
      self.__list.rotate_left()
      self.assertEqual('[ Rotate ]', str(self.__list))

    def test_rotate_left_two(self):
      self.__list.append_element('Rotate')
      self.__list.append_element('Left')
      self.__list.rotate_left()
      self.assertEqual('[ Left, Rotate ]', str(self.__list))

    def test_rotate_left_three(self):
      self.__list.append_element('Please')
      self.__list.append_element('Rotate')
      self.__list.append_element('Left')
      self.__list.rotate_left()
      self.assertEqual('[ Rotate, Left, Please ]', str(self.__list))

if __name__ == "__main__":
    unittest.main()