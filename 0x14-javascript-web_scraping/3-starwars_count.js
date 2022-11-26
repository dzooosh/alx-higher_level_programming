#!/usr/bin/node
// prints title of a Star Wars movie
// + where episode nuumber matches a given integer

const process = require('process');
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, (error, response, body) => {
  if (error) console.log(error);
  const obj = JSON.parse(body);
  console.log(obj.title);
});
