#!/usr/bin/node
const args = process.argv.slice(2);
const num = parseInt(args[0], 10);

for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
