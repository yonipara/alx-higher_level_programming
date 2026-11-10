#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  // constructor (size) { // Works but no need for the constructor since it uses the parents constructor.
  //   super(size);
  // }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let string = '';
      for (let j = 0; j < this.width; j++) {
        string += c;
      }
      console.log(string);
    }
  }
}
module.exports = Square;
