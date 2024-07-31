#!/usr/bin/node

// Importing the necessary modules.
const fs = require('fs');
const request = require('request');

// Utilizing command line arguments to retrieve the source URL and specify the destination file path.
const sourceURL = process.argv[2];
const destinationFilePath = process.argv[3];

// Sending a request to the source URL and directing the response to a writable stream.
request(sourceURL).pipe(fs.createWriteStream(destinationFilePath));
