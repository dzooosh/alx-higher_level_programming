#!/usr/bin/node
// prints the no of movies
//+ where "Wedge Antilles" is present

const process = require('process');
const request = require('request');
const url = process.argv[2];
const person_id = "https://swapi-api.hbtn.io/api/people/18/"
let count = 0;
request(url, (error, response, body) => {
  if (error) console.log(error);
  const obj = JSON.parse(body);
  //console.log(obj.results[0]["characters"]);
  for (let result of obj.results) {
    if (result["characters"].includes(person_id)) {
      count+=1;
    }
  }
  console.log(count);
});
