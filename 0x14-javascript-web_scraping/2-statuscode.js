#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (err, response, body) {
  if (err) {
    return console.error(err);
  } console.log('code:', response.statusCode);
});
