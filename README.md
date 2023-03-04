# Archipelago 

Prototype Archipelago API and dashboard.

Archipelago is a platform that ensures CO2e sequestered within recycled materials satisfies national offset regulations, achieves measurable high-integrity sustainability outcomes and supports verifiable environmental benefits.

The Archipelago dashboard is based on the following technology stack:

* [FastAPI](https://fastapi.tiangolo.com/)
* [React](https://reactjs.org/)
* [Grafana](https://grafana.com/)

## How to setup and run the dashboard

### Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Refer to https://python-poetry.org/docs/master/#installing-with-the-official-installer
   for alternative ways of installing Poetry and additional options.
   
### Install npm

For example:

```bash
sudo apt install npm
```


### Install & start Grafana

For installation instructions, refer to https://grafana.com/docs/grafana/latest/setup-grafana/installation

For instructions on how to start Grafana, refer to https://grafana.com/docs/grafana/latest/setup-grafana/installation/rpm/#2-start-the-server


### Clone this repository:

```bash
git clone git@github.com:archipelago-org/console.git
cd console
```

### Install the API dependencies:

```
poetry install
```

### Run the API
Run the API like this:

```bash
uvicorn archipelago.main:app
```

Test the API by navigating to:
http://127.0.0.1:8000/docs

### Install the front end dependencies

```bash
cd frontend
npm install
```

### Run the front end

```bash
npm start
```

Test the frontend by navigating to:
http://localhost:3006/