#!/usr/bin/node
let arr = [];
let temp;
let newTemp;
if (process.argv.length <= 3) {
	console.log(0);
}
else {
	for (let i = 0; i < process.argv.length - 2; i++) {
		arr[i] = process.argv[2 + i] -0;
	}
	temp = (arr[0] > arr[1]) ? arr[0] : arr[1];
	for (let i = 2; i < arr.length; i++) {
		if (temp < arr[i]) {
			temp = arr[i];
		}
	}
	let newArr = arr.filter((n) => n != temp);
	newTemp = (newArr[0] > newArr[1]) ? newArr[0] : newArr[1];
	for (let i = 2; i < newArr.length; i++) {
        	if (newTemp < newArr[i]) {
                	newTemp = newArr[i];
        	}
	}
	console.log(newTemp);
}
