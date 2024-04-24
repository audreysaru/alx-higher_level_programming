#!/usr/bin/node
// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer
const x = parseInt(arg);

// Check if the conversion resulted in a valid number
if (!isNaN(x)) {
  // Use a loop to print "C is fun" x times
  for (let i = 0; i < x; i++) {
    console.log("C is fun");
  }
} else {
  // Print "Missing number of occurrences" if the argument cannot be converted
  console.log("Missing number of occurrences");
}
