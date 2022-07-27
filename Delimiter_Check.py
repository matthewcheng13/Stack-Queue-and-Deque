import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.
  stack = Stack()
  start_delimiters = ['(','[','{']
  end_delimiters = [')',']','}']
  with open(filename,'r') as file_to_check:
    full_text = file_to_check.read()
  for i in full_text:
    if i in start_delimiters:
      stack.push(i)
    elif i in end_delimiters:
      if i == end_delimiters[0]:
        if start_delimiters[0] == stack.peek():
          stack.pop()
      elif i == end_delimiters[1]:
        if start_delimiters[1] == stack.peek():
          stack.pop()
      elif i == end_delimiters[2]:
        if start_delimiters[2] == stack.peek():
          stack.pop()
  if len(stack) == 0:
    return True
  else:
    return False

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


