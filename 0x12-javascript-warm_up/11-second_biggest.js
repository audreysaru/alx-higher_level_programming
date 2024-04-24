#!/usr/bin/node
// Get the list of arguments passed to the script excluding the first two elements
const args = process.argv.slice(2);

// Convert each argument to an integer and sort them in descending order
const integers = args.map(arg => parseInt(arg)).sort((a, b) => b - a);

// If there are no arguments or only one argument, print 0
if (integers.length < 2) {
  console.log(0);
} else {
  // Find the second biggest integer
  const secondBiggest = integers[1];
  console.log(secondBiggest);
}
