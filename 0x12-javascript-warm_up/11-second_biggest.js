#!/usr/bin/node
let arr = [];
let temp;
for (let i = 0; i < process.argv.length - 2; i++) {
	arr[i] = process.argv[2 + i] -0;
}
console.log(arr);
temp = (arr[0] > arr[1]) ? arr[0] : arr[1];
for (let i = 2; i < arr.length; i++) {
	if (temp < arr[i]) {
		temp = arr[i];
	}
}
console.log(temp);
