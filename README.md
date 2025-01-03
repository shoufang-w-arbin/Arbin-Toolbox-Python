# Table of Contents
- [About](#about)
- [Requirements](#requirements)
- [Installation](#install-from-wheel-file)
- 

# About
Wrappers of C# objects, providing a smoother and more Pythonic programming experience for users who want to use ArbinCTI in Python.

## Usage Example
When calling `public bool PostTimeSensitiveSetMV(IArbinSocket socket, TimeSensitiveSetMVArgs args)`, creating a `TimeSensitiveSetMVArgs` object in C# without the toolbox can be quite cumbersome. Here's an example:

### With Toolbox
Using the toolbox, the same task becomes much simpler and more intuitive:

```python
from ctitoolbox import TimeSensitiveSetMVArgs, EMVUD

mv1 = TimeSensitiveSetMV(EMVUD.MVUD1, 12.3)
mv2 = TimeSensitiveSetMV(EMVUD.MVUD2, 4.56)

mv_channel1 = TimeSensitiveSetMVArgs.TimeSensitiveSetMVChannel(1, [mv1, mv2]) # (global_index, mv_list)

mv_args = TimeSensitiveSetMVArgs(5.0, [mv_channel1]) # (timeout, channel_list)

control.PostTimeSensitiveSetMV(client, mv_args.to_cs())
```

Additional Benefits:
- Positional arguments are allowed in this toolbox, compared to using `pythonnet` directly. 
- Attributes are discoverable by Pylance, reducing human error when programming.
    ![](resource/pylance.png)

### Without Toolbox
```python
import clr
clr.AddReference("ArbinCTI")

from System.Collections.Generic import List
from ArbinCTI.Core import TimeSensitiveSetMVArgs, TimeSensitiveSetMV

mv1 = TimeSensitiveSetMV()
mv1.MVUD  = TimeSensitiveSetMV.EMVUD.MVUD1
mv1.Value = 12.3

mv2 = TimeSensitiveSetMV()
mv2.MVUD  = TimeSensitiveSetMV.EMVUD.MVUD2
mv2.Value = 5.46

mv_list = List[TimeSensitiveSetMV]()
mv_list.Add(mv1)
mv_list.Add(mv2)

mv_channel1 = TimeSensitiveSetMVArgs.TimeSensitiveSetMVChannel(
    1,
    mv_list, 
    True
)

mv_args = TimeSensitiveSetMVArgs()
mv_args.Channels.Add(mv_channel1)

control.PostTimeSensitiveSetMV(client, mv_args)
```


As you can see, the toolbox provides a smoother and more Pythonic way to interact with C# objects, making your code cleaner and easier to maintain.



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
python -m unittest
```

To view feedback output while running test, set env variable before running unittest:
```sh
$env:UNITTEST_VIEW_DICT = "True"
```
