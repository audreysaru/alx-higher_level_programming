#!/usr/bin/node
// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer
const number = parseInt(arg);

// Check if the conversion resulted in a valid number
if (!isNaN(number)) {
  // Print the number
  console.log(`My number: ${number}`);
} else {
  // Print "Not a number" if the argument cannot be converted
  console.log('Not a number');
}
