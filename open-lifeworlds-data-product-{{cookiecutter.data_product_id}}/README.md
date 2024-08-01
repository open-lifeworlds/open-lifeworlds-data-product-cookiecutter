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
* [uv](https://docs.astral.sh/uv/)

## Installation

Install uv, see https://github.com/astral-sh/uv?tab=readme-ov-file#installation.

```shell
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Usage

Run this command to generate and activate a virtual environment.

```shell
uv venv
```

Run this command to start the main script.

```shell
python3 main.py [OPTION]...

  -h, --help                           show this help
  -c, --clean                          clean intermediate results before start
  -q, --quiet                          do not log outputs

Examples:
  python3 main.py -c
```

## Roadmap

See the [open issues](https://github.com/open-lifeworlds/{{ cookiecutter.data_product_id }}/issues) for a list of
proposed features (and
known issues).

## License

Distributed under the GPLv3 License. See [LICENSE.md](./LICENSE.md) for more information.

## Contact

{{ cookiecutter.data_product_owner_email }}
