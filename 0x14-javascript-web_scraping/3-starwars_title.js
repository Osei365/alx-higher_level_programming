#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const ind = process.argv[2];
request.get(url + ind, function (err, response, body) {
  if (err) {
    console.error(err);
  } console.log(JSON.parse(body).title);
});
