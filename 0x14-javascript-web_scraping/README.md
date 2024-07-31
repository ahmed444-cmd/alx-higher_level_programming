## 0x14. JavaScript - Web Scraping

This project focuses on using JavaScript to perform web scraping tasks, addressing various objectives such as manipulating JSON data, working with APIs, and managing files using the `fs` module.

### Learning Objectives

- Understand the power of JavaScript programming.
- Learn how to manipulate JSON data.
- Master the use of `request` and `fetch` APIs.
- Gain proficiency in reading and writing files using the `fs` module.

### Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS with Node.js (version 14.x)
- **File Format**: 
  - End with a new line.
  - Begin with `#!/usr/bin/node`.
- **Documentation**: A `README.md` file in the project root is mandatory.
- **Code Standards**: Code should be semistandard compliant, using Standard rules with semicolons.
- **File Permissions**: All files must be executable.

### Setup Instructions

#### Install Node 14
```bash
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### Install semi-standard
```bash
sudo npm install semistandard --global
```

#### Install request module
```bash
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

### Tasks Overview

1. **Readme**: Write a script that reads and prints the content of a file.
2. **Write me**: Write a script that writes a string to a file.
3. **Status code**: Write a script that displays the status code of a GET request.
4. **Star Wars Movie Title**: Write a script that prints the title of a Star Wars movie based on the provided episode number.
5. **Star Wars Wedge Antilles**: Write a script that prints the number of movies where the character "Wedge Antilles" appears.
6. **Loripsum**: Write a script that retrieves the contents of a webpage and stores it in a file.
7. **How Many Completed?**: Write a script that computes the number of tasks completed by user ID.
8. **Who Was Playing in This Movie? (Advanced)**: Write a script that prints all characters of a Star Wars movie.
9. **Right Order (Advanced)**: Write a script that prints all characters of a Star Wars movie in the same order as the "characters" list in the response.
