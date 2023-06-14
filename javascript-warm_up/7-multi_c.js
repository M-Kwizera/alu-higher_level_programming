#!/usr/bin/node

const { argv } = process;

const numArg = Number(argv[2]);

const printMessage = (num) => {
  if (!num) {
    console.log('Missing number of occurrences');
  } else {
    Array(num).fill('C is fun').forEach((message) => {
      console.log(message);
    });
  }
};

printMessage(numArg);
