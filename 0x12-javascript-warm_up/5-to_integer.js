#!/usr/bin/node

const process = require('process');
const arg = process.argv;
const num = parseInt(arg[2]);

if (typeof (num) === 'number') {
  if (!isNaN(num)) {
    console.log(`My number: ${num}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
