#!/usr/bin/node
console.log(process.argv);

const args = process.argv.slice(2);

if (args.length > 1)
{
    console.log('Arguments found');
}
else if (args.length === 1)
{
    console.log('Argument found');
}
else 
{
    console.log('No argument');
}