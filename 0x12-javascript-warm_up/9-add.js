#!/usr/bin/node
function add (a, b) {
  return (a - 0) + (b - 0);
}
console.log(add(process.argv[2], process.argv[3]));
