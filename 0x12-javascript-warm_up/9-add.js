#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const myVar1 = parseInt(process.argv[2]);
const myVar2 = parseInt(process.argv[3]);

add(myVar1, myVar2);
