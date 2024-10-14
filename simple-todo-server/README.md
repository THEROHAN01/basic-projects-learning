# Todo Server Project

Welcome to the Todo Server Project! This project demonstrates how to create a simple Todo server using Express.js. It allows you to manage your todos with basic CRUD operations: Create, Read, Update, and Delete.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

This Todo server provides the following functionalities:

1. **Display Statistics**: 
   - Retrieve the total number of todos, as well as the count of completed and incomplete todos using a GET request.
  
2. **Add Todos**: 
   - Add new todos (either complete or incomplete) using a POST request.
  
3. **Update Todos**: 
   - Replace an incomplete todo using a PUT request.
  
4. **Delete Incomplete Todos**: 
   - Remove all incomplete todos using a DELETE request.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:


2. Install the required libraries:
   ```bash
   npm run doit
   ```

## Usage

Once you have installed the necessary dependencies, you can start the server:

```bash
npm start
```

After starting the server, you can access it in your browser at `http://localhost:3000`.

### Important Note:
It is recommended to use Postman or any similar API testing tool to perform GET, POST, PUT, and DELETE requests.

## API Endpoints

Here are the available API endpoints for interacting with the Todo server:

- **GET /todos/stats**
  - Returns the total number of todos, completed todos, and incomplete todos.

- **POST /todos**
  - Adds a new todo. You need to send a JSON body with the structure:

- **PUT /todos**
  - Updates an existing todo by ID. You need to send a JSON body with the new title and completion status.

- **DELETE /todos/incomplete**
  - Deletes all incomplete todos.

## Technologies Used

This project is built with:

- [Node.js](https://nodejs.org/)
- [Express.js](https://expressjs.com/)

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Thank you for checking out the Todo Server Project! Happy coding!
