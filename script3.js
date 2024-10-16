// Given a nested array of arbitrary depth, write a function flatten that returns a new array with all the values flattened into a single level.

function flatten(arr) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    if (Array.isArray(arr[i])) {
      result = result.concat(flatten(arr[i]));
    } else {
      result.push(arr[i]);
    }
  }
  return result;
}
const nestedArr = [1, [2, [3, [4, 5]]]];
console.log(flatten(nestedArr));
