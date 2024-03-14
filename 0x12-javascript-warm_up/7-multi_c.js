#!/usr/bin/node

const numOccurrences = parseInt(process.argv[2]);

let i = 0;

if (isNaN(numOccurrences)) {
  console.log('Missing number of occurrences');
} else if (numOccurrences > 0) {
  while (i < numOccurrences) {
    console.log('C is fun');
    i++;
  }
}
