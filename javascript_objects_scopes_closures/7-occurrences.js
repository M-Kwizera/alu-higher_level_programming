#!/usr/bin/node

const nbOccurences = (list, searchElement) => {
  let count = 0;

  for (const elem of list) {
    if (elem === searchElement) count++;
  }

  return count;
};

module.exports = { nbOccurences };
