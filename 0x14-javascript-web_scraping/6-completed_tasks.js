#!/usr/bin/node
// computes the number of tasks completed by user id

const process = require('process');
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const todos = JSON.parse(body);
    let userId = 1;
    let completed = 0;
    const result = {};

    for (let i = 0; i < todos.length; i++) {
      if (userId < todos[i].userId) {
        result[userId] = completed;
        completed = 0;
        userId = todos[i].userId;
      }
      if (todos[i].completed === true) {
        completed += 1;
      }
    }
    result[userId] = completed;
    console.log(result);
  }
});
