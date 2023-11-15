#!/usr/bin/node
const fs = require('fs');

const firstFilePath = process.argv[2];
const secondFilePath = process.argv[3];
const outputFilePath = process.argv[4];

const firstFileContent = fs.readFileSync(firstFilePath).toString();
const secondFileContent = fs.readFileSync(secondFilePath).toString();

fs.writeFileSync(outputFilePath, firstFileContent + secondFileContent);
