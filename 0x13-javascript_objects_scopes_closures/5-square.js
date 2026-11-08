#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super();
    this.size = size;
    this.width = this.size;
    this.height = this.size;
  }
}
module.exports = Square;
