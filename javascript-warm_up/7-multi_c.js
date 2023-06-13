#!/usr/bin/node
const key_word = 'C is fun';
const argument = process.argv;
const conversion = Number(argument[2]);

// console.log(typeof(conversion))

if (typeof(conversion) != 'number') {
    console.log('Missing number of occurrences');
} else {
    console.log((key_word + '\n'). repeat(conversion));
}
