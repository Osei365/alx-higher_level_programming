#!/usr/bin/node

const request = require('request');
const ch = process.argv[2];
request.get(ch, function (err, response, body) {
  if (!err) {
    const results = JSON.parse(body).results;
    const total = results.reduce((count, content) => {
      if (content.characters.find((character) => character.endsWith('/18/'))) {
        return count + 1;
      } return count;
    }, 0);
    console.log(total);
  }
});
