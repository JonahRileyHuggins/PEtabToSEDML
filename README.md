# SED-ML Builder from PEtab Files

This project provides a set of Python scripts to generate SED-ML files from PEtab data, allowing for streamlined modeling and simulation setup for biological experiments. The tools help automate the process of loading PEtab data, extracting relevant parameters, and building a SED-ML file for further computational analysis.

## Project Structure

- **`builders.py`**: Constructs elements, classes, and objects necessary for the SED-ML file from PEtab data.
- **`extractors.py`**: Extracts essential details such as simulation times for building SED-ML files.
- **`loader.py`**: Loads PEtab files and extracts SBML models, parameters, and experimental conditions.

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:JonahRileyHuggins/PEtabToSEDML.git
   cd PEtabToSEDML
   ```
2. Requirements are provided in both a TOML file:
   ```bash
   pip install -r pyproject.toml
   ```

    As well as an Anaconda environment yaml, located in the 'env' directory.

```
conda env create -f env/environment.yml
```

### Dependencies

The project requires the following Python packages:

- `pandas`
- `lxml`
- `libsbml`
- `yaml`
- `phrasedml`

## Usage

### Build SED-ML File

Use `builders.py` to build SED-ML elements and output a SED-ML file:

```python
import source.builders as builders
builders.build_sedml_file(yaml_file='test_benchmark/test_benchmark.yml')
```

## License

This project is licensed under the MIT License.
