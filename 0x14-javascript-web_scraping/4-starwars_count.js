#!/usr/bin/node
// prints the no of movies
// + where "Wedge Antilles" is present

const process = require('process');
const request = require('request');
const url = process.argv[2];
const personId = 18;
let count = 0;
request(url, (error, response, body) => {
  if (error) console.log(error);
  const obj = JSON.parse(body);
  for (const result of obj.results) {
    for (const x of result.characters) {
      if (x.split('/').includes(personId.toString())) {
        count += 1;
      }
    }
  }
  console.log(count);
}
);
