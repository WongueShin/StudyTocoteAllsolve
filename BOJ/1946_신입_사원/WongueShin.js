const fs = require('fs');
const stdin = fs.readFileSync('dev/stdin').toString().trim().split('\n')

const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();

const testCase = parseInt(input());

for(let i = 0; i < testCase; i++){
    let N = parseInt(input());
    const silcedList = [];
    for(idx = 0; idx < N; idx ++){
        silcedList.push(input().split(' ').map(e=> parseInt(e)));
    }
    silcedList.sort((a, b) => a[0] - b[0]);
    let maxlank = silcedList[0][1];
    let counter = 0;
    for(ele of silcedList){
        if(ele[1] <= maxlank){
            maxlank = ele[1];
            counter++;
        }
        if(maxlank === 1){
            break;
        }
    }
    console.log(counter);
}