#!/usr/bin/node

function factorial (num) {
  if (num === 0 || !num) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const myVar = parseInt(process.argv[2]);

console.log(factorial(myVar));
