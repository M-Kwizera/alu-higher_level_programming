#!/usr/bin/node
const size_of_square = process.argv[2];
const int_size_of_square = parseInt(size_of_square);

if (isNaN(int_size_of_square)) {
    console.log('Missing size');
} else {
    for (let i = 0; i < int_size_of_square; i++) {
        let row = '';
        for (let j = 0; j < int_size_of_square; j++) {
            row += 'X';
        }
        console.log(row);
    }
}