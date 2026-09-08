#!/usr/bin/node
const nums = process.argv.slice(2).map(Number);

if (nums.length < 2) {
  console.log(0);
  process.exit(0);
}

const max = Math.max(...nums);
const secondMax = Math.max(...nums.filter(n => n !== max));

console.log(secondMax);

// const arr = [];
// let temp;
// let newTemp;
// if (process.argv.length <= 3) {
//  console.log(0);
// } else {
//  for (let i = 0; i < process.argv.length - 2; i++) {
//    arr[i] = process.argv[2 + i] - 0;
//  }
//  temp = arr[0];
//  for (let i = 0; i < arr.length; i++) {
//    if (temp <= arr[i]) {
//      temp = arr[i];
//    }
//  }
//  const newArr = arr.filter((n) => n !== temp);
//  newTemp = newArr[0];
//  for (let i = 0; i < newArr.length; i++) {
//    if (newTemp <= newArr[i]) {
//      newTemp = newArr[i];
//    }
//  }
//  console.log(newTemp);
// }
