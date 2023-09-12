#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const myObject = {};

  for (let i = 0; i < list.length; i++) {
    if (myObject[list[i]]) {
      myObject[list[i]] += 1;
    } else {
      myObject[list[i]] = 1;
    }
  }
  return myObject[searchElement];
};
