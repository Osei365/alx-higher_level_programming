#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let stringVar = '';
      for (let a = 0; a < this.width; a++) {
        stringVar = stringVar + 'X';
      }
      console.log(stringVar);
    }
  }
}

module.exports = Rectangle;
