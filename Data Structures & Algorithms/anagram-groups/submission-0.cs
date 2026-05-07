public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        List<List<string>> solution = new List<List<string>>();

        // cat -> act -> index 2
        Dictionary<string, int> sortedStringToIndexMap = new Dictionary<string, int>();

        foreach (string s in strs)
        {
            string sortedString = String.Concat(s.OrderBy(c => c));
            if (sortedStringToIndexMap.ContainsKey(sortedString))
            {
                int index = sortedStringToIndexMap[sortedString];
                solution[index].Add(s);
            }
            else
            {
                List<string> newList = new List<string>();
                newList.Add(s);
                solution.Add(newList);

                sortedStringToIndexMap.Add(sortedString, solution.Count - 1);
            }
        }

        return solution;
    }
}
