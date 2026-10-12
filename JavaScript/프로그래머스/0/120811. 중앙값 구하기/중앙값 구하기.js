function solution(array) {
    array.sort((a,b) => a-b);
    const result = Math.floor(array.length / 2) ;
    var answer = array[result];
    
    return answer;
}