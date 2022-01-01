const fs = require('fs');
let input = fs.readFileSync("dev/stdin").toString().trim();
//let input = '00009-00009';
input = input.split(/\+|(\-)/).map(e=>/[0-9]/.test(e) ? parseInt(e) : e).filter(e=> e !== undefined).toString().split(/,\-,/).map(e=>e.split(',')).map(e=> e.map(arr=> parseInt(arr))).map(e=> e.reduce((a, b)=> a + b, 0));
console.log(input[0] - (input.slice(1,).reduce((a, b) => a + b, 0)));