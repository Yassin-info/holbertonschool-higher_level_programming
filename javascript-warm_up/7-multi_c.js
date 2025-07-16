#!/usr/bin/node

const argv = 'C is fun';
const argc = process.argv[2];

if (isNaN(parseInt(argc))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(argc); i++) {
    console.log(argv);
  }
}
