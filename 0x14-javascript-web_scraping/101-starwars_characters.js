#!/usr/bin/node

const request = require('request');

const movieIdArg = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieIdArg}`;

request(apiUrl, (reqError, response, body) => {
  if (reqError) {
    console.error(reqError);
    return;
  }

  const movieData = JSON.parse(body);
  const charactersUrls = movieData.characters;

  charactersUrls.forEach((characterUrl, index) => {
    request(characterUrl, (charError, response, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);

      // Check if this is the last character, then print newline
      if (index === charactersUrls.length - 1) {
        console.log();
      }
    });
  });
});
