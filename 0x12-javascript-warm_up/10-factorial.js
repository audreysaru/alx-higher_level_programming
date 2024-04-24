#!/usr/bin/node
// Define a function to compute the factorial recursively
function factorial (n) {
  // Base case: factorial of 0 or NaN is 1
  if (isNaN(n) || n === 0) {
    return 1;
  }

  // Recursive case: factorial of n is n times factorial of (n - 1)
  return n * factorial(n - 1);
}

// Get the first argument passed to the script
const arg = parseInt(process.argv[2]);

// Compute the factorial of the provided integer
const result = factorial(arg);

// Print the result
console.log(result);
