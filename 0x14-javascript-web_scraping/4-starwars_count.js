#!/usr/bin/node

const request = require('request');
const ch = process.argv[2];
request.get(ch, function (err, response, body) {
  if (!err) {
    const results = JSON.parse(body).resultsi;
    console.log(results.reduce((count, content) => {
      return content.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
