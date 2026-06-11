#!/usr/bin/node
function factorial (a) {
  if ((a - 0) && (a > 1)) {
    a = a * factorial(a - 1);
  } else {
    return 1;
  }
  return a;
}
console.log(factorial(process.argv[2]));
