public class LinkedList {

    private class LinkedListNode
    {
        public int m_data = 0;
        public LinkedListNode m_next = null;

        public LinkedListNode(int val)
        {
            m_data = val;
        }
    }

    private LinkedListNode m_head;

    public LinkedList() {
        m_head = null;
    }

    public int Get(int index) {
        if (m_head == null)
        {
            return -1;
        }

        LinkedListNode node = m_head;
        for (int i = 0; i < index; ++i)
        {
            node = node.m_next;

            if (node == null)
            {
                return -1;
            }
        }

        return node.m_data;
    }

    public void InsertHead(int val) {
        LinkedListNode newHead = new LinkedListNode(val);

        if (m_head != null)
        {
            newHead.m_next = m_head;
        }

        m_head = newHead;
    }

    public void InsertTail(int val) {
        LinkedListNode newTail = new LinkedListNode(val);

        if (m_head == null)
        {
            m_head = newTail;
            return;
        }

        LinkedListNode tail = m_head;
        while (tail.m_next != null)
        {
            tail = tail.m_next;
        }

        tail.m_next = newTail;
    }

    public bool Remove(int index) {
        if (m_head == null)
        {
            return false;
        }

        if (index == 0)
        {
            m_head = m_head.m_next;
            return true;
        }
        
        LinkedListNode currNode = m_head;
        LinkedListNode prevNode = null;
        
        for (int i = 0; i < index; ++i)
        {
            prevNode = currNode;
            currNode = currNode.m_next;

            if (currNode == null)
            {
                return false;
            }
        }

        if (prevNode != null)
        {
            prevNode.m_next = currNode.m_next;
        }

        return true;
    }

    public List<int> GetValues() {
        List<int> values = new List<int>();

        LinkedListNode node = m_head; 
        while (node != null)
        {
            values.Add(node.m_data);
            node = node.m_next;
        }

        return values;
    }
}