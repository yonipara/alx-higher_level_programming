#!/usr/bin/node
function logmeCounter () {
  let i = 0;
  function logMe (item) {
    console.log(`${i}: ${item}`);
    i++;
  }
  return logMe;
}

const logMe = logmeCounter();
module.exports.logMe = logMe;
