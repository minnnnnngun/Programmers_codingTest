function solution(numer1, denom1, numer2, denom2) {
    // 1. 두 분수를 통분하여 더한 분자와 분모 계산
    const numer = numer1 * denom2 + numer2 * denom1;
    const denom = denom1 * denom2;
    
    // 2. 유클리드 호제법을 이용한 최대공약수(GCD) 구하기 함수
    const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));
    const commonFactor = gcd(numer, denom);
    
    // 3. 분자와 분모를 최대공약수로 나누어 기약분수로 만들기
    return [numer / commonFactor, denom / commonFactor];
}
