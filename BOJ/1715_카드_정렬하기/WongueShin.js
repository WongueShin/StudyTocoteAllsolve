const fs = require('fs');

let input = fs.readFileSync('dev/stdin')
.toString()
.trim()
.split('\n').slice(1, )
.map(e => parseInt(e));
/*
let input = `3
10
20
40`.split('\n').slice(1, ).map(e => parseInt(e));
*/

class MinHeap{ 
    constructor(){
        this.heap = [0];
    }
    log(){
        console.log(this.heap);
    }
    insert = (v) => { 
        this.heap.push(v);
        let p = this.heap.length - 1; 
        while (p > 1 && this.heap[Math.floor(p / 2)] > this.heap[p]) { 
            let tmp = this.heap[Math.floor(p / 2)]; 
            this.heap[Math.floor(p / 2)] = this.heap[p]; 
            this.heap[p] = tmp; p = Math.floor(p / 2); 
            } 
        }; 
    getLength = () => this.heap.length; ; 
    
    delete = () => { 
        if (this.heap.length - 1 < 1) return 0; 
        let deletedItem = this.heap[1]; 
        this.heap[1] = this.heap[this.heap.length - 1]; 
        this.heap.pop(); let p = 1; 
        while (p * 2 < this.heap.length) { 
            let min = this.heap[p * 2]; 
            let minP = p * 2; 
            if (p * 2 + 1 < this.heap.length && min > this.heap[p * 2 + 1]) { 
                min = this.heap[p * 2 + 1]; minP = p * 2 + 1; 
            } 
            if (this.heap[p] < min) break; 
            let tmp = this.heap[p]; 
            this.heap[p] = this.heap[minP]; 
            this.heap[minP] = tmp; 
            p = minP; } 
            return deletedItem; 
        }; 
}


let minheap = new MinHeap();
for(ele of input){
    minheap.insert(ele);
}
let count = 0;

while(minheap.getLength() > 2){
    let temp = minheap.delete() + minheap.delete();
    minheap.insert(temp);
    count += temp;
}


console.log(count);