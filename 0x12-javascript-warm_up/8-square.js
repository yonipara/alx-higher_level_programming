#!/usr/bin/node
if (process.argv[2] - 0) {
  for (let i = 0; i < process.argv[2]; i++) {
    let string = '';
    for (let j = 0; j < process.argv[2]; j++) {
      string += 'X';
    }
    console.log(string);
  }
} else {
  console.log('Missing size');
}
