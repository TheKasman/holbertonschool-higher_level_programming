#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  let largest = -Infinity;
  let second = -Infinity;
  for (let i = 0; i < args.length; i++) {
    if (i === 0) {
      largest = args[i];
    } else if (args[i] > largest) { //  largest
      second = largest;
      largest = args[i];
    } else if (args[i] > second && args[i] !== largest) { //  inbetween largest and second largest
      second = args[i];
    }
  }
  console.log(second);
}
