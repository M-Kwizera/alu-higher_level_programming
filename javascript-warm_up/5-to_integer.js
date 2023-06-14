#!/usr/bin/node
const {argv} = process;
const nArg = Number(argv[2]);
if (!nArg) console.log('Not a number');
else {
    console.log('My number:', nArg);
}