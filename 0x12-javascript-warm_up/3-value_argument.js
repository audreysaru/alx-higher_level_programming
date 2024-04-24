#!/usr/bin/node
// Get the arguments passed to the script
const args = process.argv.slice(2);

// Check if any arguments were passed
if (args[0] !== undefined) {
  // Print the first argument
  console.log(args[0]);
} else {
  // No arguments were passed
  console.log('No argument');
}
