# Python Mocking Patterns

Showcase for different mocking patterns in Python.

## Patterns by Organizational

The patterns will be broken out into their own project folder with a `README.md` detailing the example mock.  A pattern will focus on where to patch, <https://docs.python.org/3/library/unittest.mock.html#where-to-patch>, in the context of the organizationl structure.

These patterns will use `pytest` and `pytest-mock` but can easliy be converted to the base `unittest` and `unittest.mock` modules.

### Script

The definition of `script` organizational structure from <https://docs.python.org/3/tutorial/modules.html#modules>.

> If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost. Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the input for the interpreter and running it with that file as input instead. This is known as creating a script.

This example will use the most basic of configuration:

- `venv` - Setup a virtual environment for segregating dependencies in this example
- `requirements.txt` - Define the dependencies for the example

### Module

The definition of `module` organizational structure from <https://docs.python.org/3/tutorial/modules.html#modules>

> Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module.

This example will use an opinionated project conifguration:

- `venv` - Setup a virtual environment for segregating dependencies in this example
- `poetry` - Dependency management using `pyproject.toml`
- `tox`- Quality gate orchestration and execution of the tests

## References

- pytest - <https://docs.pytest.org/en/7.1.x/getting-started.html>
- pytest-mock - <https://pytest-mock.readthedocs.io/en/latest/index.html>
- venv - <https://docs.python.org/3/library/venv.html>
- poetry  - <https://python-poetry.org/docs/pyproject/>
- tox - <https://tox.wiki/en/latest/config.html>
