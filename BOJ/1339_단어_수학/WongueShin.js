const fs = require('fs');
let input = fs.readFileSync("dev/stdin")
    .toString()
    .trim()
    .split('\n')
    .slice(1,);

/*let input = `10
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB`.split('\n').slice(1,);*/

let convertedList = input.map(e=> e.split(''))

let memo = {};
for(subList of convertedList){
    for(let idx = 0; idx < subList.length; idx++){
        let digit = 10**(subList.length - 1 - idx);
        if(memo[subList[idx]] === undefined){
            memo[subList[idx]] = digit;
            continue;
        }
        memo[subList[idx]] += digit;
    }
}
let temp = 9;
console.log(
    JSON.stringify(memo)
    .replace(/^\{|[A-Z]|\:|"|\}$/g, '').split(',')
    .map(ele => parseInt(ele)).sort((a, b)=> b - a)
    .reduce((a, b) => {
        temp--;
        return a + (b * (temp+ 1));
    }, 0)
);

/*
처음에는 가장 큰 자릿수에 위치한 알파벳 순으로 숫자를 메기면 될 줄 알았다...
ACDEB
GCF
=>
9(A)8(C)7(D)6(E)4(B)
5(G)8(C)3(F)
--------------------
반례가 존재한다.
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB
방정식을 풀때, 같은 미지수끼리 합치듯이 계산한 뒤에 소팅후 reduce를 이용해 풀이가 가능하다.

==> 머리 비우고 아 그리디니까 대충풀면 되지라고 생각하면서 풀지 말자...
*/
