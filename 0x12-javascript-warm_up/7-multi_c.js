#!/usr/bin/node

const process = require('process');
const args = process.argv;
const str = 'C is fun';

if (!args[2]) {
  console.log('Missing number of occurrences');
} else if (args[2] > 1) {
  for (let i = 0; i < args[2]; i++) {
    console.log(str);
  }
}
