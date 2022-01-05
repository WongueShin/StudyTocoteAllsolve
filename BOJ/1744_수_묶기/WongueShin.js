const fs = require('fs');
//let input = fs.readFileSync('dev/stdin').toString().trim().split('\n')
//    .slice(1, ).map(e=> parseInt(e));
let input = `2
1
2`.split('\n').slice(1, ).map(e => parseInt(e));

const solution = () => {
    input = input.sort((a, b) => b - a);
    const[positive, zeros, minus] = [[], [], []];
    for(ele of input){
        if(ele > 0){positive.push(ele)}
        if(ele === 0){zeros.push(ele)}
        if(ele < 0){minus.push(ele)}
    }
    positive.sort((a, b) => b - a);
    minus.sort((a, b) => a - b);
    let result = 0;
    while(positive.length > 0){
        if(positive.length >= 2 && positive[0]> 1 && positive[1] > 1){
            result += positive.shift() * positive.shift();
            continue;
        }
        result += positive.shift();
    }
    while(minus.length > 0){
        if(minus.length >= 2){
            result += minus.shift() * minus.shift();
            continue;
        }
        if(zeros.length >= 1){
            minus.shift();
            zeros.shift();
            continue;
        }
        result += minus.shift();
    }
    return result;
}

console.log(solution());