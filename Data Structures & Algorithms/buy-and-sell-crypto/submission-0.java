class Solution {
    public int maxProfit(int[] prices) {
        int max=0;
        for (int i=0;i<prices.length;i++){
            for (int j=i;j<prices.length;j++){
                if (i!=j){
                    int profit=prices[j]-prices[i];
                    if (profit>max){
                        max=profit;
                    }
                }
            }

        }

        return max;
        
    }
}
