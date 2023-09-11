#!/usr/bin/node

const myVar = process.argv[2];
if (parseInt(myVar)) {
  for (let i = 0; i < parseInt(myVar); i++) {
    console.log('C is fun');
  }
} else console.log('Missing number of occurrences');
