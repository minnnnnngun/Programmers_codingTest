function solution(s) {
    const tokens = s.split(" ");
    let total = 0;
    let previous = 0;
    
    for(const token of tokens) {
        if(token === "Z") {
            total -= previous;
        } else {
            previous = Number(token);
            total += previous;
        }
    }
    
    return total;
}