#!/usr/bin/node

const esrever = (list) => {
  const reverse = [];

  for (let i = list.length - 1; i >= 0; i--) {
    reverse.push(list[i]);
  }

  return reverse;
};
module.exports.esrever = esrever;
