const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().split('\n');
/*const input = `10 50000
1
5
10
50
100
500
1000
5000
10000
50000`.split('\n');*/

const [N, K] = input[0].split(' ').map(e=>parseInt(e));
const listOfCoin = input.slice(1, ).map(e=>parseInt(e));

const solution = (remainVal) => {
    let numOfCoin = 0;
    for (let idx = listOfCoin.length - 1; idx > -1; idx--){
        if(remainVal === 0){
            break
        }
        if (listOfCoin[idx] <= remainVal){
            numOfCoin += parseInt(remainVal / listOfCoin[idx]);
            remainVal = remainVal % listOfCoin[idx];
        }
    }
    return numOfCoin;
}
console.log(solution(K));

/*
1. 재귀로 풀어보려다가 스택오버플로우 발생. => while 반복문으로 해결하자.
2. 해당하는 코인을 찾앗을때, reaminVal -= coinVal 로 계산하다가, 그냥 나눠버리면 된다는 생각이 듬
=> 시간복잡도 훨신 최적화 가능해짐(이러면 재귀로도 풀이가 가능 할 것 같다.)
*/