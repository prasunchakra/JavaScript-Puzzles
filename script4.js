// Write a debounce function that prevents a function from being called too quickly in succession.
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);

    timer = setTimeout(() => {
      fn.apply(this, args);
    }, delay);
  };
}

const log = debounce(() => console.log("Logged after delay"), 1000);

log();
