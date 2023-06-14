#!/usr/bin/node
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

function add(num1, num2) {
    let summ = num1 + num2;
    console.log(summ)
}

add(arg1, arg2);