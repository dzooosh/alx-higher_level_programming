#!/usr/bin/node

const process = require('process');
const args = process.argv;
let total = 1;

function fact (num) {
  if ((num <= 1) || isNaN(num)) {
    console.log(total);
    return (1);
  } else {
    total *= num;
    fact(num - 1);
  }
}

fact(args[2]);
