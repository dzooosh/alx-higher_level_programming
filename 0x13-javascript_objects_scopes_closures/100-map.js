#!/usr/bin/node
const list = require('./100-data');
let i = 0;
console.log(list);
console.log(list.map(x => x * list.indexOf(x)));
