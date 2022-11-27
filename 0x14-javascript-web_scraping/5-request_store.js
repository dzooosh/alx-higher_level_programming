#!/usr/bin/node
// gets the contents of a webpage and stores it in a file

const fs = require('fs');
const process = require('process');
const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) console.log(err);
  fs.writeFile(fileName, body, 'utf-8', (error) => {
    if (error) console.log(error);
  });
}
);
