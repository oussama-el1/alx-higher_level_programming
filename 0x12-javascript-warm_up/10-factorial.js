#!/usr/bin/node
function factorial (n) {
  let p = 1;
  for (let i = 1; i <= n; i++) {
    p *= i;
  }
  return p;
}
console.log(factorial(Number(process.argv[2])));
