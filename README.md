# MyPackage

Welcome to MyPackage! 
This library was created as an example of how to publish your own python package

## Building this package locally

`python setup.py sdist`

## Installation

You can install MyPackage using pip:

```bash
pip install git+https://github.com/tam-dcreator/mypackage.git
```

If you need to **install a later version** of your package, then use:  

```bash
pip install --upgrade git+https://github.com/your-name/your-repo.git
```

## Usage

Here is a simple example to get you started:

```python
>>>> from mypackage import myModule

# Example usage
>>>> myModule.top_n([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
>>>> [9, 8, 7] 
```

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or feedback, please feel free to reach out.