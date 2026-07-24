class Solution {
    public int maxArea(int[] heights) {
        int start=0;
        int end=heights.length-1;
        int max_area=0;
        while(start<end){
            int b=Math.min(heights[start],heights[end]);
            int l=end-start;
            int area=b*l;
            if (area>max_area){
                max_area=area;
            }
            if (heights[start]>heights[end]){
                end--;
            }
            else{
                start++;
            }
        }
        return max_area;
        
    }
}
