import unittest
import StackLab.Stack as lc
import StackLab.StackFullException as StackFullException
import StackLab.StackEmptyException as StackEmptyException


class MyTestCase(unittest.TestCase):
    def test_something(self):
        
        self.assertEqual(True, False)
        
    def test_create_stack(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        # ACT
        actual = my_stack.is_empty()
        # ASSERT
        self.assertTrue(actual)

    def test_is_empty_True(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        # ACT
        actual = my_stack.is_empty()
        expected = True
        # ASSERT
        self.assertEqual(expected, actual)
        
    def test_is_empty_false(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        item = "Java is Fun!"
        # ACT
        my_stack.push(item)
        actual = my_stack.is_empty()
        expected = False
        # ASSERT
        self.assertEqual(expected, actual)
                
    def test_is_full_True(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        item = "Java is Fun!"
        # ACT
        my_stack.push(item)
        actual = my_stack.is_full()
        expected = True
        # ASSERT
        self.assertEqual(expected, actual)
        
    def test_is_full_False(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        # ACT
        actual = my_stack.is_full()
        expected = False
        # ASSERT
        self.assertEqual(expected, actual)
        
    def test_push_stack(self):
        # ARRANGE
        my_stack = lc.Stack(2)
        item = "StackItem"
        expected = "StackItem2\nStackItem1\n"
        # ACT
        my_stack.push(item + "1")
        my_stack.push(item + "2")
        actual = my_stack.print_stack_up()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_push_full_stack(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        item = "StackItem"
        # ACT
        # ASSERT
        self.assertRaises(StackFullException.StackFullException, my_stack.push(item))
     
    def test_pop_stack(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        item = "StackItem"
        expected = "StackItem"
        my_stack.push(item)
        # ACT
        actual = my_stack.pop()
        # ASSERT
        self.assertEqual(expected, actual)
        
    def test_stack_size_zero(self):
        # ARRANGE
        my_stack = lc.Stack(2)
        expected = 0
        # ACT
        actual = my_stack.size()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_stack_size_non_zero(self):
        # ARRANGE
        my_stack = lc.Stack(2)
        item = "StackItem"
        expected = 2
        # ACT
        my_stack.push(item + "1")
        my_stack.push(item + "2")
        actual = my_stack.size()
        # ASSERT
        self.assertEqual(expected, actual)
        
    def test_pop_empty_stack(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        # ACT
        # ASSERT
        self.assertRaises(StackEmptyException.StackEmptyException, my_stack.pop())
        
    def test_peek_stack(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        item = "StackItem"
        # ACT
        my_stack.push(item)
        expected = item
        actual = my_stack.peek()
        # ASSERT
        self.assertEqual(expected, actual)
        
    def test_peek_empty_stack(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        # ACT
        # ASSERT
        self.assertRaises(StackEmptyException.StackEmptyException, my_stack.peek())

    def test_print_stack_up(self):
        # ARRANGE
        my_stack = lc.Stack(2)
        item = "StackItem"
        expected = "StackItem2\nStackItem1\n"
        # ACT
        my_stack.push(item + "1")
        my_stack.push(item + "2")
        actual = my_stack.print_stack_up()
        # ASSERT
        self.assertEqual(expected, actual)
        
    def test_print_stack_up_empty_stack(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        expected = "Stack is Empty"
        # ACT
        actual = my_stack.print_stack_up()
        # ASSERT
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
