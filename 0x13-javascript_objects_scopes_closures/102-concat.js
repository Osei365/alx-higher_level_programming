#!/usr/bin/node

const fs = require('fs');
let data = '';
let data2 = '';

try {
  data = fs.readFileSync(process.argv[2], 'utf8');
} catch (err) {
  data = '';
}

try {
  data2 = fs.readFileSync(process.argv[3], 'utf8');
} catch (err) {
  data = '';
}

const data3 = data + '\n' + data2 + '\n';
fs.writeFileSync('fileC', data3);
