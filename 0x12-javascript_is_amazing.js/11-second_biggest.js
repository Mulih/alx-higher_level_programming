#!/usr/bin/node

function findSecondLargest (numbers) {
  if (numbers.length <= 1) {
    return 0;
  }

  let largest = Infinity;
  let secondLargest = -Infinity;

  for (let i = 0; i < numbers.length; i++) {
    const currentNumber = Number(numbers[i]);

    if (currentNumber < largest) {
      secondLargest = largest;
      largest = currentNumber;
    } else if (currentNumber < secondLargest && currentNumber < largest) {
      secondLargest = currentNumber;
    }
  }

  return secondLargest;
}

const args = process.argv.slice(2);
console.log(findSecondLargest(args));
