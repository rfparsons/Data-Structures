import unittest

# import LabCode.Queue as lc
# import LabCode.QueueFullException as QueueFullException
# import LabCode.QueueEmptyException as QueueEmptyException

# I can't seem to get the imports working correctly without moving everything into the same folder

import Queue as lc
import QueueFullException as QueueFullException
import QueueEmptyException as QueueEmptyException


class MyTestCase(unittest.TestCase):
    def test_create_queue(self):
        # ARRANGE
        my_queue = lc.Queue(1)
        # ACT
        actual = my_queue.is_empty()
        # ASSERT
        self.assertTrue(actual)

    def test_is_empty_true(self):
        # ARRANGE
        my_queue = lc.Queue(1)
        # ACT
        actual = my_queue.is_empty()
        # ASSERT
        self.assertTrue(actual)

    def test_is_empty_false(self):
        # ARRANGE
        my_queue = lc.Queue(1)
        item = "Python is Fun!"
        # ACT
        my_queue.enqueue(item)
        actual = my_queue.is_empty()
        # ASSERT
        self.assertFalse(actual)

    def test_is_full_true(self):
        # ARRANGE
        my_queue = lc.Queue(1)
        item = "Python is Fun!"
        # ACT
        my_queue.enqueue(item)
        actual = my_queue.is_full()
        # ASSERT
        self.assertTrue(actual)

    def test_is_full_false(self):
        # ARRANGE
        my_queue = lc.Queue(1)
        # ACT
        actual = my_queue.is_full()
        # ASSERT
        self.assertFalse(actual)

    def test_enqueue(self):
        # ARRANGE
        my_queue = lc.Queue(2)
        item = "QueueItem"
        expected = "QueueItem1"
        # ACT
        my_queue.enqueue(item + "1")
        my_queue.enqueue(item + "2")
        actual = my_queue.peek()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_enqueue_full_queue(self):
        # ARRANGE
        my_queue = lc.Queue(1)
        item = "QueueItem"
        # ACT
        # ASSERT
        self.assertRaises(QueueFullException, my_queue.enqueue(item))

    def test_dequeue(self):
        # ARRANGE
        my_queue = lc.Queue(2)
        item = "QueueItem"
        expected = "QueueItem1"
        my_queue.enqueue(item+"1")
        my_queue.enqueue(item+"2")
        # ACT
        actual = my_queue.dequeue()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_wrap_around(self):
        # ARRANGE
        my_queue = lc.Queue(2)
        item = "QueueItem"
        expected = "QueueItem2"
        # ACT
        my_queue.enqueue(item + "1")
        my_queue.enqueue(item + "2")
        my_queue.dequeue()
        my_queue.enqueue(item + "3")
        actual = my_queue.peek()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_size_zero(self):
        # ARRANGE
        my_queue = lc.Queue(2)
        expected = 0
        # ACT
        actual = my_queue.size()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_size_non_zero(self):
        # ARRANGE
        my_queue = lc.Queue(2)
        item = "QueueItem"
        expected = 2
        # ACT
        my_queue.enqueue(item + "1")
        my_queue.enqueue(item + "2")
        actual = my_queue.size()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_dequeue_empty_queue(self):
        # ARRANGE
        my_queue = lc.Queue(1)
        # ACT
        # ASSERT
        self.assertRaises(QueueEmptyException.QueueEmptyException, my_queue.dequeue())

    def test_peek(self):
        # ARRANGE
        my_queue = lc.Queue(2)
        item = "QueueItem"
        expected = "QueueItem1"
        # ACT
        my_queue.enqueue(item + "1")
        my_queue.enqueue(item + "2")
        actual = my_queue.peek()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_peek_empty_queue(self):
        # ARRANGE
        my_queue = lc.Queue(1)
        # ACT
        # ASSERT
        self.assertRaises(QueueEmptyException, my_queue.peek())

    def test_print_queue_empty_queue(self):
        # ARRANGE
        my_queue = lc.Queue(1)
        expected = "Queue is Empty"
        # ACT
        actual = my_queue.print_queue()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_print_queue(self):
        # ARRANGE
        my_queue = lc.Queue(2)
        item = "QueueItem"
        expected = "QueueItem1\nQueueItem2\n"
        # ACT
        my_queue.enqueue(item + "1")
        my_queue.enqueue(item + "2")
        actual = my_queue.print_queue()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_print_queue_wrap_around(self):
        # ARRANGE
        my_queue = lc.Queue(2)
        item = "QueueItem"
        expected = "QueueItem2\nQueueItem3\n"
        # ACT
        my_queue.enqueue(item + "1")
        my_queue.enqueue(item + "2")
        my_queue.dequeue()
        my_queue.enqueue(item + "3")
        actual = my_queue.print_queue()
        # ASSERT
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
