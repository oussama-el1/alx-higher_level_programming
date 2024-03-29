#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    const tem = this.height;
    this.height = this.width;
    this.width = tem;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
