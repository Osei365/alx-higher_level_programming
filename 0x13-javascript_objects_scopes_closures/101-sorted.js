#!/usr/bin/node
const dict = require('./101-data').dict;

const newObject = {};

for (const key in dict) {
  if (!newObject[dict[key]]) {
    newObject[dict[key]] = [key];
  } else {
    newObject[dict[key]].push(key);
  }
}

console.log(newObject);
