# Arbin Toolbox
## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Supported Arbin Objects](#supported-arbin-objects)
- [Usage Examples](#usage-examples)
- [Development](#Development)

## About
This toolbox aims to simplify the integration of **ArbinCTI** and **ArbinClient** with Python applications by leveraging `pythonnet`. While `pythonnet` enables the use of C# objects defined in the DLL, interacting with these objects directly can be unintuitive for Python developers. This toolbox provides Python wrappers for these C# objects, offering a more Pythonic and user-friendly interface.

For example, to call `PostTimeSensitiveSetMV(IArbinSocket socket, TimeSensitiveSetMVArgs args)` in ArbinCTI:

![](resource/compare.png)

By abstracting away C# object interactions, developers can focus on their core application logic rather than wrestling with language-specific intricacies.

### Additional Benefits
- **Easy Py-C# Data structure conversions** are backed by `CSConv` in this toolbox.
- **Beautified feedback objects** with full serializability and quick inspection method. 
- **Support for keyword arguments**, compared to using `pythonnet` directly.
- **Object attributes are discoverable by Pylance**, reducing human error when programming. \
    ![](resource/pylance.png)

## Installation
### Requirements
- 64-bit Python >= 3.7
- System
    - Windows: .NET Framework >=4.7.2
    - Linux: Mono is used by default
- ArbinCTI permission on MITS
### Installation
- **ArbinCTI** Users
    1. Switch to branch `arbinctitools`
    2. Run `pip install dist/arbinctitools-{version}-py3-none-any.whl` in your development environment.

- **ArbinClient** Users
    1. Switch to branch `arbinclienttools`
    2. Run `pip install dist/arbinclienttools-{version}-py3-none-any.whl` in your development environment.

## Supported Arbin Objects
- For **ArbinCTI** object, see [`arbinctitools/README.md`](https://github.com/shoufang-w-arbin/Arbin-Toolbox-Python/blob/arbinctitools/README.md).
- For **ArbinClient** object, see [`arbinclienttools/README.md`](https://github.com/shoufang-w-arbin/Arbin-Toolbox-Python/blob/arbinclienttools/README.md).

## Usage
Refer to [EXAMPLE.md](EXAMPLE.md) for:
- Basic usage examples
- An overview of `CSConv` functionality
- Common pitfalls in `pythonnet` development

## Development
### Testing
To run unittest
```sh
python -m unittest
```

To view feedback output while running test, set env variable before running unittest:
- Windows Powershell
    ```sh
    $env:UNITTEST_VIEW_DICT="True"
    ```
- Linux Cmd
    ```sh
    UNITTEST_VIEW_DICT="True"
    ```

### To-Do
> We are adding more wrapper classes. If you require immediate implementation of a certain object, please create an issue or submit a pull request with your work.
