#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cpp = 0;
  for (const elt of list) {
    if (elt === searchElement) {
      cpp += 1;
    }
  }
  return cpp;
};
