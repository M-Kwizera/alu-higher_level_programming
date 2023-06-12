#!/usr/bin/node
const arguments = process.argv - 2;
if (arguments === 0) {
    console.log('No argument');
}else {
    console.log (arguments);
}