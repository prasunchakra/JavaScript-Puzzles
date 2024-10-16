//Write a custom implementation of the reduce method called customReduce

Array.prototype.customReduce = function (callback, initialValue) {
  let accumulator = initialValue;
  let startIndex = 0;
  if (accumulator === undefined) {
    accumulator = this[0];
    startIndex = 1;
  }
  for (let i = startIndex; i < this.length; i++) {
    accumulator = callback(accumulator, this[i], i, this);
  }
  return accumulator;
};
const arr = [1, 2, 3, 4];
const sum = arr.customReduce(
  (accumulator, currentValue) => accumulator + currentValue,
  0
);
console.log(sum);
