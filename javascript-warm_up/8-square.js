#!/usr/bin/node

const argv = 'X';
const argc = parseInt(process.argv[2]);

if (isNaN(argc)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argc; i++) {
    console.log(argv.repeat(argc));
  }
}
