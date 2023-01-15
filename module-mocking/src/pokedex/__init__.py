from importlib.metadata import PackageNotFoundError, version

try:
    name = "python_template"
    __version__ = version(name)
except PackageNotFoundError:
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
