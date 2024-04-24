#!/usr/bin/node
// Get the arguments passed to the script
const args = process.argv.slice(2);

// Check if both arguments are provided
if (args.length === 2) {
// Print the arguments in the specified format
  console.log(`${args[0]} is ${args[1]}`);
} else if (args.length === 1) {
// Print message if only one argument is provided
  console.log(`${args[0]} is undefined`);
} else {
// Print message if no arguments are provided
  console.log('undefined is undefined');
}
