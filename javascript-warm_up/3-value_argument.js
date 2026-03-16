#!/usr/bin/node
const args = process.argv.slice(2);

if (args[0]) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
