#!/bin/bash

# Create and add content to each file

# Task 0
echo -e '#!/usr/bin/node\nconst myVar = "JavaScript is amazing";\nconsole.log(myVar);' > 0-javascript_is_amazing.js

# Task 1
echo -e 'console.log("C is fun");\nconsole.log("Python is cool");\nconsole.log("JavaScript is amazing");' > 1-multi_languages.js

# Task 2
echo -e 'const args = process.argv.slice(2);\n\nif (args.length === 0) {\n  console.log("No argument");\n} else if (args.length === 1) {\n  console.log("Argument found");\n} else {\n  console.log("Arguments found");\n}' > 2-arguments.js

# Task 3
echo -e 'const arg = process.argv[2];\n\nif (arg === undefined) {\n  console.log("No argument");\n} else {\n  console.log(arg);\n}' > 3-value_argument.js

# Task 4
echo -e 'const arg1 = process.argv[2];\nconst arg2 = process.argv[3];\n\nconsole.log(arg1 + " is " + arg2);' > 4-concat.js

# Task 5
echo -e 'const arg = process.argv[2];\n\nif (isNaN(arg)) {\n  console.log("Not a number");\n} else {\n  console.log("My number:", parseInt(arg));\n}' > 5-to_integer.js

# Task 6
echo -e 'const languages = ["C is fun", "Python is cool", "JavaScript is amazing"];\n\nfor (const language of languages) {\n  console.log(language);\n}' > 6-multi_languages_loop.js

# Task 7
echo -e 'const x = parseInt(process.argv[2]);\n\nif (isNaN(x)) {\n  console.log("Missing number of occurrences");\n} else {\n  for (let i = 0; i < x; i++) {\n    console.log("C is fun");\n  }\n}' > 7-multi_c.js

# Task 8
echo -e 'const size = parseInt(process.argv[2]);\n\nif (isNaN(size)) {\n  console.log("Missing size");\n} else {\n  for (let i = 0; i < size; i++) {\n    console.log("X".repeat(size));\n  }\n}' > 8-square.js

# Task 9
echo -e 'const a = parseInt(process.argv[2]);\nconst b = parseInt(process.argv[3]);\n\nfunction add(a, b) {\n  return a + b;\n}\n\nconsole.log(add(a, b));' > 9-add.js

# Task 10
echo -e 'const n = parseInt(process.argv[2]);\n\nfunction factorial(n) {\n  if (isNaN(n)) {\n    return 1;\n  }\n  if (n === 0 || n === 1) {\n    return 1;\n  } else {\n    return n * factorial(n - 1);\n  }\n}\n\nconsole.log(factorial(n));' > 10-factorial.js

# Task 11
echo -e 'const numbers = process.argv.slice(2).map(Number);\n\nif (numbers.length < 2) {\n  console.log(0);\n} else {\n  const sortedNumbers = numbers.sort((a, b) => b - a);\n  console.log(sortedNumbers[1]);\n}' > 11-second_biggest.js

# Task 12
echo -e '#!/usr/bin/node\nconst myObject = {\n  type: "object",\n  value: 12\n};\nconsole.log(myObject);\n\n// Update the value property\nmyObject.value = 89;\n\nconsole.log(myObject);' > 12-object.js

# Task 13
echo -e 'module.exports = {\n  add: function (a, b) {\n    return a + b;\n  }\n};' > 13-add.js

# Task 14 (Additional task to create the 13-main.js file)
echo -e '#!/usr/bin/node\nconst add = require("./13-add").add;\nconsole.log(add(3, 5));' > 13-main.js

# Make the scripts executable
chmod +x *.js

echo "Files created successfully."

