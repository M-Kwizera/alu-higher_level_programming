#!/usr/bin/node
const arg = process.argv;
const conversion = Number(arg[2]);
if (conversion) {
    console.log(`My number: ${arg[2]}`);
} else {
    console.log('Not a number');
}
