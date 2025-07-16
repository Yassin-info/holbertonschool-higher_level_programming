#!/usr/bin/node

const argv = process.argv[2];

if (!isNaN(parseInt(argv))) {
  console.log('My number: ' + parseInt(argv));
} else {
  console.log('Not a number');
}
