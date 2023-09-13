#!/usr/bin/node

const fs = require('fs');

const data = fs.readFileSync(process.argv[2], 'utf8');
const data2 = fs.readFileSync(process.argv[3], 'utf8');
const data3 = data + '\n' + data2;
fs.writeFileSync('fileC', data3);
