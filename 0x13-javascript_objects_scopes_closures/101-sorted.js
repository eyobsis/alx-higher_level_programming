#!/usr/bin/node
const originalDictionary = require('./101-data').dict;

const entriesList = Object.entries(originalDictionary);
const valuesList = Object.values(originalDictionary);
const uniqueValues = [...new Set(valuesList)];
const modifiedDictionary = {};

for (const uniqueValue of uniqueValues) {
  const keyList = [];

  for (const entry of entriesList) {
    if (entry[1] === uniqueValue) {
      keyList.unshift(entry[0]);
    }
  }

  modifiedDictionary[uniqueValue] = keyList;
}

console.log(modifiedDictionary);
