#!/usr/bin/node

const process = require('process');
const args = process.argv;
const str = [];

if (!args[2]) {
  console.log('0');
} else if (args.length === 3) {
  console.log('0');
} else {
  args.forEach((arg) => {
    str.push(arg);
  });
  str.sort(function (a, b) {
    return (a - b);
  });
  console.log(str[str.length - 2]);
}
