#!/usr/bin/node

const request = require('request');
const ch = 'https://swapi-api.alx-tools.com/api/people/18';
request.get(ch, function (err, response, body) {
  if (err) {
    console.error(err);
  } console.log(JSON.parse(body).films.length);
});
