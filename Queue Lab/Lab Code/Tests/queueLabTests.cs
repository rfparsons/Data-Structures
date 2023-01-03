using System;
using Xunit;

namespace TestQueueLab
{
    public class queueLabTests
    {

        [Fact]
        public void testCreatequeue()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(1);
            bool actual;
            // ACT
            actual = myQueue.isEmpty();
            // ASSERT
            Assert.True(actual);
        }

        [Fact]
        public void testIsEmptyTrue()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(1);
            bool actual;
            // ACT
            actual = myQueue.isEmpty();
            // ASSERT
            Assert.True(actual);
        }

        [Fact]
        public void testIsEmptyFalse()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(1);
            String item = "C# is Fun!";
            bool actual;
            // ACT
            myQueue.enqueue(item);
            actual = myQueue.isEmpty();
            // ASSERT
            Assert.False(actual);
        }

        [Fact]
        public void testIsFullTrue()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(1);
            String item = "C# is Fun!";
            bool actual;
            // ACT
            myQueue.enqueue(item);
            actual = myQueue.isFull();
            // ASSERT
            Assert.True(actual);
        }

        [Fact]
        public void testIsFullFalse()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(1);
            bool actual;
            // ACT
            actual = myQueue.isFull();
            // ASSERT
            Assert.False(actual);
        }

        [Fact]
        public void testEmqueue()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(2);
            String item = "queueItem";
            String actual, expected;
            expected = "queueItem1";
            // ACT
            myQueue.enqueue(item + "1");
            myQueue.enqueue(item + "2");
            actual = myQueue.peek();
            // ASSERT
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void testEnqueueFullQueue()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(1);
            String item = "queueItem";
            // ACT
            myQueue.enqueue(item);
            // ASSERT
            Assert.Throws<QueueLabWithTests.queueFullException>(() => myQueue.enqueue(item));
        }

        [Fact]
        public void testDequeue()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(1);
            String item = "queueItem";
            String actual, expected;
            expected = item;
            myQueue.enqueue(item);
            // ACT
            actual = myQueue.dequeue();
            // ASSERT
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void testSizeZero()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(2);
            int actual, expected;
            expected = 0;
            // ACT
            actual = myQueue.size();
            // ASSERT
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void testSizeNonZero()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(2);
            String item = "queueItem";
            int actual, expected;
            expected = 2;
            // ACT
            myQueue.enqueue(item + "1");
            myQueue.enqueue(item + "2");
            actual = myQueue.size();
            // ASSERT
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void testDequeueEmptyQueue()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(1);
            // ACT
            // ASSERT
            Assert.Throws<QueueLabWithTests.queueEmptyException>(() => myQueue.dequeue());
        }

        [Fact]
        public void testWrapAround()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(2);
            String item = "queueItem";
            String actual, expected;
            expected = "queueItem3";
            // ACT
            myQueue.enqueue(item + "1");
            myQueue.enqueue(item + "2");
            myQueue.dequeue();
            myQueue.enqueue(item + "3");
            myQueue.dequeue();
            actual = myQueue.peek();
            // ASSERT
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void testPeek()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(1);
            String item = "queueItem";
            String actual, expected;
            expected = item;
            // ACT
            myQueue.enqueue(item);
            actual = myQueue.peek();
            // ASSERT
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void testPeekEmptyQueue()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(1);
            // ACT
            // ASSERT
            Assert.Throws<QueueLabWithTests.queueEmptyException>(() => myQueue.peek());

        }

        [Fact]
        public void testPrintQueueEmptyQueue()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(1);
            String actual, expected;
            expected = "queue is Empty";
            // ACT
            actual = myQueue.printQueue();
            // ASSERT
            Assert.Equal(expected, actual);
        }
        [Fact]
        public void testPrintQueue()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(2);
            String item = "queueItem";
            String actual, expected;
            expected = "queueItem2\nqueueItem1\n";
            // ACT
            myQueue.enqueue(item + "1");
            myQueue.enqueue(item + "2");
            actual = myQueue.printQueue();
            // ASSERT
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void testPrintQueueWrapAround()
        {
            // ARRANGE
            QueueLabWithTests.queue myQueue = new QueueLabWithTests.queue(2);
            String item = "queueItem";
            String actual, expected;
            expected = "queueItem3\n";
            // ACT
            myQueue.enqueue(item + "1");
            myQueue.enqueue(item + "2");
            myQueue.dequeue();
            myQueue.enqueue(item + "3");
            myQueue.dequeue();
            actual = myQueue.printQueue();
            // ASSERT
            Assert.Equal(expected, actual);
        }

    }
}
