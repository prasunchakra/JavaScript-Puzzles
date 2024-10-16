//Write a custom implementation of the map method called customMap

Array.prototype.customMap = function (callback) {
  const result = [];
  for (let i = 0; i < this.length; i++) {
    result.push(callback(this[i], i, this));
  }
  return result;
};

const arr = [1, 2, 3, 4];
const newArr = arr.customMap((item) => item * 2);
console.log(newArr);
