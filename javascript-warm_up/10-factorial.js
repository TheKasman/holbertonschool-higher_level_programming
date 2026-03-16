#!/usr/bin/node

const args = process.argv.slice(2);
const num1 = parseInt(args[0], 10);

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(num1));
