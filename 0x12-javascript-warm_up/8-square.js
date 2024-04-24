#!/usr/bin/node
// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer
const size = parseInt(arg);

// Check if the conversion resulted in a valid number
if (!isNaN(size)) {
  // Use a loop to print a square of size x
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  // Print "Missing size" if the argument cannot be converted
  console.log('Missing size');
}
