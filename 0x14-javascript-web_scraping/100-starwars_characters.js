#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
request.get(url + id, function (err, response, body) {
  if (!err) {
    const chs = JSON.parse(body).characters;
    for (let i = 0; i < chs.length; i++) {
      request.get(chs[i], function (err1, response1, body1) {
        if (!err) {
          console.log(JSON.parse(body1).name);
        }
      });
    }
  }
});
