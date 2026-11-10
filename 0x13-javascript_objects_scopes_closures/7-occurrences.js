#!/usr/bin/node

const nbOccurences = (list, searchElement) => {
  const matches = list.filter((element) => element === searchElement);
  return matches.length;
};
module.exports.nbOccurences = nbOccurences;
