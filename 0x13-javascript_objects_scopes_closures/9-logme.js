#!/usr/bin/node

exports.logMe = function (item) {
  this.count = (this.count || 0) + 1;
  console.log((this.count - 1) + ': ' + item);
};
