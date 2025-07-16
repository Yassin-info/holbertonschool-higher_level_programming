#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const argsNumbers = args.map(e => parseInt(e));
  argsNumbers.sort((a, b) => b - a);
  console.log(argsNumbers[1]);
}
