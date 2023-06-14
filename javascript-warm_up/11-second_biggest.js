#!/usr/bin/node
const arguments = process.argv.map(arg => parseInt(arg));
const length_arguments = arguments.length - 2;

let current_biggest = Number.NEGATIVE_INFINITY;
let second_biggest = Number.NEGATIVE_INFINITY;

for (let i = 2; i < arguments.length; i++) {
    const current = arguments[i];
    if (current > current_biggest) {
        second_biggest = current_biggest;
        current_biggest = current;
    } else if (current > second_biggest && current !== current_biggest) {
        second_biggest = current;
    }
}

const result = (length_arguments < 2) ? 0 : second_biggest;

console.log(result);