function solution(i, j, k) {
  let count = 0;
  const target = String(k);

  for (let number = i; number <= j; number++) {
    for (const digit of String(number)) {
      if (digit === target) {
        count++;
      }
    }
  }

  return count;
}