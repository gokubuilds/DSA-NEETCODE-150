class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap <String,ArrayList<String>> map= new HashMap<>();
        for (String i:strs){
            char[] str=i.toCharArray();
            Arrays.sort(str);
            String sorted= new String(str);
            map.putIfAbsent(sorted, new ArrayList<>());
            map.get(sorted).add(i);
            
        }
        return new ArrayList<>(map.values());
        
    }
}
