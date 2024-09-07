# Guide to run the application
1. Clone the repository
2. Be sure Docker engine is installed and running on your machine
3. Run the following command to build the docker image
```bash
docker build -t my_test_server .
```
4. Run the following command to run the docker container

On linux
```bash
docker run -p 8080:8080 -v $(pwd)/src:/app/src my_test_server
```
On windows
```bash
docker run -p 8080:8080 -v ${PWD}/src:/app/src my_test_server
```

The application addresses will be displayed in the terminal. You can access the application by visiting the address in your browser.

