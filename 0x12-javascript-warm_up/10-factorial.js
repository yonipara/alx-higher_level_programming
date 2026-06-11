#!/usr/bin/node
function factorial (a) {
  if ((a - 0) && (a > 1)) {
    var num = a * factorial(a - 1);
  } else {
    return 1;
  }
  return num;
}
console.log(factorial(process.argv[2]));
