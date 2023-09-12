#!/usr/bin/node

const myVar = process.argv.length;
const myArray = [];

if (myVar === 2 || myVar === 3) {
  console.log('0');
} else {
  for (let i = 2; i < myVar; i++) {
    myArray.push(parseInt(process.argv[i]));
  }
  myArray.sort(function (a, b) { return b - a; });
  console.log(myArray[1]);
}
