#!/usr/bin/node

const myVar = process.argv[2];

if (parseInt(myVar)) {
  for (let i = 0; i < parseInt(myVar); i++) {
    let stringVar = '';
    for (let a = 0; a < parseInt(myVar); a++) {
      stringVar = stringVar + 'X';
    }
    console.log(stringVar);
  }
} else console.log('Missing size');
