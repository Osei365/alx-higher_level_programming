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

  rotate () {
    const exVar = this.width;
    this.width = this.height;
    this.height = exVar;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
