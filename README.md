# About
Wrappers of C# objects, providing smoother programming experience. 

## Table of Contents
- [About](#about)
- [Requirements](#requirements)
- [Installation](#install-from-wheel-file)
- 

## Requirements
- 64-bit Python >= 3.7
- System
    - Windows: .NET Framework >=4.7.2
    - Linux: Mono is used by default

## Install from wheel file
`pip install dist/ctitoolbox-python-1.0.0-py3-none-any.whl`

## Testing
Run unittest
```sh
python -m unnitest
```

To view feedback output while running test, set env variable before running unittest:
```sh
$env:UNITTEST_VIEW_DICT = "True"
```
