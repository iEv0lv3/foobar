def solution(x, y):
  set1 = set(x)
  set2 = set(y)
  prisoners = set1.symmetric_difference(set2)
  return min(prisoners)
