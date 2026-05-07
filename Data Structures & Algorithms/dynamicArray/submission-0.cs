public class DynamicArray {
    
    private int[] m_array;
    private int m_rear;

    public DynamicArray(int capacity) {
        m_array = new int[capacity];
        m_rear = 0;
    }

    public int Get(int i) {
        return m_array[i];
    }

    public void Set(int i, int n) {
        m_array[i] = n;
    }

    public void PushBack(int n) {
        if (m_array.Length <= m_rear)
        {
            Resize();
        }

        m_array[m_rear] = n;
        ++m_rear;
    }

    public int PopBack() {
        return m_array[--m_rear];
    }

    private void Resize() {
        Array.Resize(ref m_array, m_array.Length * 2);
    }

    public int GetSize() {
        return m_rear;
    }

    public int GetCapacity() {
        return m_array.Length;
    }
}
