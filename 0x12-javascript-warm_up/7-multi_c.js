#!/usr/bin/node
if (!isNaN((process.argv[2] - 0)) {
  let i = 0;
  while (i < process.argv[2]) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
