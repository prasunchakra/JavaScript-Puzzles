import java.util.*;

class SubsetWithDuplicates {

  public static List<List<Integer>> findSubsets(int[] nums) {
    List<List<Integer>> subsets = new ArrayList<>();
    Arrays.sort(nums);
    subsets.add(new ArrayList<>());
    int beg=0,end=0;
    for(int j=0;j<nums.length;j++){
      beg=0;
      if(j>0 && nums[j]==nums[j-1])
            beg=end+1;
      end=subsets.size()-1; //Why -1 ?
      for(int i=beg;i<=end;i++){
        List<Integer> set = new ArrayList<>(subsets.get(i));
        set.add(nums[j]);
        subsets.add(set);
      }
    }
    return subsets;
  }

  public static void main(String[] args) {
    List<List<Integer>> result = SubsetWithDuplicates.findSubsets(new int[] { 1, 3, 3 });
    System.out.println("Here is the list of subsets: " + result);

    result = SubsetWithDuplicates.findSubsets(new int[] { 1, 5, 3, 3 });
    System.out.println("Here is the list of subsets: " + result);
  }
}
