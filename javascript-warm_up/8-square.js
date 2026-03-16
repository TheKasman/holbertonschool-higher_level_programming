const args = process.argv.slice(2);
const num = parseInt(args[0], 10);

if (isNaN(num)) {
    console.log('Missing size');
}

for (let i = 0; i < num; i++) {
  let line = '';
  for (let j = 0; j < num; j++) {
    line += 'X';
  }
  console.log(line);
}
