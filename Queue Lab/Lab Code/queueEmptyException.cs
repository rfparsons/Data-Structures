using System;
using System.Collections.Generic;
using System.Text;

namespace QueueLabWithTests
{
    public class queueEmptyException : Exception
    {
        public override string Message
        {
            get
            {
                return "Queue is Empty";
            }
        }
    }
}
