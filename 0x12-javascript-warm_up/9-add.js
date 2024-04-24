#!/usr/bin/node
// Define a function add with parameters a and b
function add (a, b) {
  // Calculate the sum of a and b
  const sum = a + b;

  // Print the sum
  console.log(sum);
}

// Get the first and second arguments passed to the script
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

// Check if both arguments are valid numbers
if (!isNaN(arg1) && !isNaN(arg2)) {
  // Call the add function with the provided arguments
  add(arg1, arg2);
} else {
  // Print an error message if any argument is not a valid number
  console.log('NaN');
}
