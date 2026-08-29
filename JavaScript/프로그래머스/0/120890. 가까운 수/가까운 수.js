function solution(array, n) {
  const answer = array.reduce((closest, current) => {
    const closestDistance = Math.abs(closest - n);
    const currentDistance = Math.abs(current - n);

    if (currentDistance < closestDistance) {
      return current;
    }
    if (currentDistance === closestDistance) {
      return Math.min(closest, current);
    }


    return closest;
  }, array[0]);

  return answer;
}