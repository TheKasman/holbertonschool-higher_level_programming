#!/usr/bin/node
const args = process.argv.slice(2);
const num = parseInt(args[0], 10); //  turn to base 10
if (num === 'NaN') {
  console.log('Not a Number');
} else {
  console.log('My number: ' + num);
}
