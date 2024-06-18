[![Issues](https://img.shields.io/github/issues/open-lifeworlds/open-lifeworlds-data-product-berlin-15-minute-city)](https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-15-minute-city/issues)

<br />
<p align="center">
  <a href="https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-15-minute-city">
    <img src="logo_with_text.png" alt="Logo" height="80">
  </a>

  <h1 align="center">{{ cookiecutter.data_product_owner_name }} Data Product - {{ cookiecutter.data_product_name }}</h1>

  <p align="center">
    Data product providing TODO</a>
  </p>
</p>

## About The Project

See [data product canvas](docs/data-product-canvas.md).

### Built With

* [Python](https://www.python.org/)

## Installation

Install the following dependencies to fulfill the requirements for this project to run.

```shell script
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

### Transformation

Run this command to start the main script.

```shell script
python main.py [OPTION]...

  -h, --help                           show this help
  -c, --clean                          clean intermediate results before start
  -q, --quiet                          do not log outputs

Examples:
  python main.py -c
```

## Roadmap

See the [open issues](https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-15-minute-city/issues) for a list of proposed features (and
 known issues).

## License

Distributed under the GPLv3 License. See [LICENSE.md](./LICENSE.md) for more information.

## Contact

{{ cookiecutter.data_product_owner_email }}
