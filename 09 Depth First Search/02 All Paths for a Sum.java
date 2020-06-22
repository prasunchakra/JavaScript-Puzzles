import java.util.*;

class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode(int x) {
    val = x;
  }
};

class FindAllTreePaths {
  public static List<List<Integer>> findPaths(TreeNode root, int sum) {
    List<List<Integer>> allPaths = new ArrayList<>();
    List<Integer> currentPath = new ArrayList<>();
    findPathsRecurse(root,sum,currentPath,allPaths);
    return allPaths;
  }
  private static void findPathsRecurse(TreeNode currentNode,int requiredSum,
  List<Integer> currentPath,List<List<Integer>> allPaths){
    if (currentNode==null)
      return;
    
    currentPath.add(currentNode.val);
    if(currentNode.val==requiredSum && currentNode.left==null && currentNode.right==null){
      allPaths.add(new ArrayList<Integer>(currentPath));
    }else{
      findPathsRecurse(currentNode.left,requiredSum-currentNode.val,currentPath,allPaths);
      findPathsRecurse(currentNode.right,requiredSum-currentNode.val,currentPath,allPaths);
    }
    currentPath.remove(currentPath.size()-1);
  }
  public static void main(String[] args) {
    TreeNode root = new TreeNode(12);
    root.left = new TreeNode(7);
    root.right = new TreeNode(1);
    root.left.left = new TreeNode(4);
    root.right.left = new TreeNode(10);
    root.right.right = new TreeNode(5);
    int sum = 23;
    List<List<Integer>> result = FindAllTreePaths.findPaths(root, sum);
    System.out.println("Tree paths with sum " + sum + ": " + result);
  }
}
