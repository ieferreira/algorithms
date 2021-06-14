// two sum problem naive in dart
main(List<String> args) {
  List nums = [7, 11, 15, -4, 11, 13, 7, 2, 4, 5];
  int target = 9;
  List sol = twoSum(nums, target);
  print(sol);
}

List twoSum(List N, int target) {
  int len = N.length;
  for (int i = 0; i <= len; i++) {
    for (int j = i + 1; j <= len - 1; j++) {
      if (N[i] + N[j] == target) {
        int idx1 = i;
        int idx2 = j;
        print('found at indexes: ${[idx1, idx2]}');
      }
    }
  }
  return N;
}
