# CS451R Project

### Structure
- Frontend
    - Node and React
- Backend Server
    - Python Flask
- Database
    - MongoDB Community (local development \& testing)

### Required Dependencies
1. NodeJS v18.13.0 (LTS: Hydrogen)
2. Python 3.8.*
3. MongoDB Community v6.0.4 (local development)
4. MongoDB Compass v1.35.0

### Local Development Setup
1. Make sure the required dependencies are installed by running the command `npm run install-depend` in the project directory.
2. Make sure MongoDB community is running locally. Open MongoDB Compass and make sure there is an active connection on mongodb://localhost:27017/ (the default connection).
3. Run the command `npm run fullstack-test` to verify the whole project is working correctly.
4. Run the command `npm run fullstack-dev` to start the fullstack development environment.

### Development
| Command               | Functionality                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| npm run install-depend    | Installs dependencies for the entire project.                                                                                         |
| npm run frontend-test     | Runs automated tests associated with the frontend.                                                                                    |
| npm run backend-test      | Runs automated tests associated with the backend.                                                                                     |
| npm run fullstack-test    | Runs automated tests associated with the frontend, backend, and additional acceptance tests.                                          |
| npm run frontend-dev      | Builds and runs the frontend in a development environment. When changes are saved, the frontend automatically reloads.                |
| npm run backend-dev       | Builds and runs the backend in a development environment. When changes are saved, the backend server is rebuilt.                      |
| npm run fullstack-dev     | Builds and runs both the frontend and backend in a development environment. Both are automatically reloaded when changes are saved.   |


