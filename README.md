# Glia API Take Home Assessment

## Description
This project contains code to run a web server for two APIs written in Python's FastAPI:
* /jumble - given a word in a JSON body, this endpoint rearranges the letters of the word randomly
* /audit - returns the last 10 API calls to the server

The steps below provide the following details:
* Test - instructions for testing this repository with `pytest`
* Build - instructions for updating and building this image with the `Dockerfile`
* Deploy - instructions for deploying this image with `helm`

## Prerequisites
Ensure you have installed the following programs to successfully run the remaining sections in this README.md:

* python3
* docker
* helm
* minikube

## Local development/testing
### Running webserver on Docker
In a terminal, enter `docker-compose up`. Add `-d` to the end if you want to detach from the log output. When finished, run `docker-compose down` to stop and remove the container.

### Running tests
First, ensure the necessary package dependencies are installed to run this program on your machine. You can install directly with `python3 -m pip install -r ./app/requirements.txt` or you can use virtualenv instead (see https://docs.python.org/3/library/venv.html for further details on setting that up).

Once installed, you can run `pytest` from the root folder to run all of the tests under the `app/tests` folder.

### Build
Use the `makefile` to build the Docker image for this app.

By default, running `make build` will build a Docker image with a `latest` tag.

`make build` will also pre-load your minikube cluster with this image so it can be later deployed with `helm`.

### Deploy
Use the `makefile` to deploy the Docker image to your minikube cluster.

Run `make install-dev` to deploy the chart.

To uninstall the chart, run `make uninstall` which will remove the deployment from minikube.

## Deploy a production release
To deploy a versioned production release, you must update the `values.yaml` file under `./helm/vars/production` with the version of your choice in the `image.tag` value. This repository uses a x.x.x versioning strategy (i.e: 1.0.0).

After that value is changed, run `make IMAGE_TAG=<release-tag> release` to build and deploy your image to minikube.

## Accessing the app
Run `minikube service glia-app --url` to get an endpoint you can reach.
