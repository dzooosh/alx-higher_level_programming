#!/usr/bin/node

const process = require('process');
const args = process.argv;
const first = parseInt(args[2]);
let str = '';

if (!args[2] || isNaN(first)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < first; i++) {
    for (let i = 0; i < first; i++) {
      str += 'X';
    }
    console.log(str);
    str = '';
  }
}
