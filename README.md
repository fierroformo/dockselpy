## dockselpy

Dockerfile example on how to *"assemble"* together Selenium (with support for Chrome, Firefox and PhantomJS), Python and Xfvb.

### Information

Recent struggle with finding a docker image for Selenium that supports headless versions for both Firefox and Chrome,
led to the process of building my own version.

The image is build with the following dependencies:
- latest Chrome and chromedriver
- latest Firefox and geckodriver
- latest stable PhantomJS webkit (v2.1.1)
- Selenium
- Python 3
- Xvfb and the python wrapper - pyvirtualdisplay


### Running:

- docker
    ```
    docker build -t selenium_docker .
    docker run --privileged -p 4000:4000 -d -it selenium_docker
    ```

- docker-compose

    ```
    docker-compose stop && docker-compose build && docker-compose up -d
    ```


### Run Tests

```bash
docker exec -it dockselpy_selenium_1 bash -c "python3 tests.py firefox https://dragon.dev.justo.cloud/account/login/"

docker exec -it dockselpy_selenium_1 bash -c "python3 tests.py chrome https://dragon.dev.justo.cloud/account/login/"
```
