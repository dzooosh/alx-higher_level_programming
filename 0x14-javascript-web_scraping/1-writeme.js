#!/usr/bin/node
// writes a string to a file

const fs = require('fs');
const process = require('process');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    return console.error(err);
  }
});
