#!/usr/bin/node
// Check the number of arguments passed to the script
const numberOfArguments = process.argv.length - 2; // Subtracting 2 to exclude 'node' and the script file path

// Print messages based on the number of arguments
if (numberOfArguments === 0) {
  console.log('No argument');
} else if (numberOfArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
