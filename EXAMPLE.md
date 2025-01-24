# Usage and Examples
## About
Here are some examples and notes on how to use `pythonnet` and `arbintoolbox` to interact smoothly with **ArbinCTI** and **ArbinClient**.

- [Data Type Casting in Pythonnet](#data-type-casting-in-pythonnet)
  - [Handling TypeError](#handling-typeerror)
- [Arbin Object Creation](#arbin-object-creation)
- [C# `List` Conversion](#c-list-conversion)
- [C# `SortedDictionary` Conversion](#c-sorteddictionary-conversion)
- [Arbin Feedback Accessing](#arbin-feedback-accessing)

## Data Type Casting in Pythonnet
Pythonnet doesn't handle casting between Python and C# data types perfectly. Explicit casting is recommended for certain data types. Below is a known data type casting compatibility in Pythonnet.

| Python Type | Pythonnet Type    | C# Type  | Implicit Casting       |
|-------------|-------------------|----------|------------------------|
| `bool`      | `Boolean`         | `bool`   | Yes                    |
| `int`       | `Int32`           | `int`    | Yes                    |
| `int`       | `UInt32`          | `uint`   | Yes                    |
| `float`     | `Single`          | `float`  | Yes                    |
| `float`     | `Double`          | `double` | Yes                    |
| `str`       | `String`          | `string` | Yes                    |
| `bytearray` | `Array` of `Byte` | `byte[]` | **No**                 |
| `int`       | `Int16`           | `short`  | **No**                 |
| `int`       | `UInt16`          | `ushort` | **No**                 |
| `int`       | `Int64`           | `long`   | **No**                 |


#### Safe Implicit Casting Examples
```python
# bool PostNewFolder (IArbinSocket socket, string strPath)
control.PostNewFolder(client, "hello world")

# bool PostResumeChannel (IArbinSocket socket, bool AllResume, int ChannelIndex) 
control.PostResumeChannel(client, True, 0)
```

### Handling TypeError
Some operations may lead to `TypeError` if not properly cast. For example:
```python
# bool PostGetChannelsDataMminimalistMode(IArbinSocket socket, short onlyGetChannelNumber = -1)
control.PostGetChannelsDataMminimalistMode(
    client,
    0        # py 'int' -> cs 'short'
) 
```
This code will raise a TypeError with a message similar to:
```
TypeError: No method matches given arguments for PostGetChannelsDataMminimalistMode: ...
```

To resolve this issue, use explicit casting. Here's an example using the `CSConv`:
```python
control.PostGetChannelsDataMminimalistMode(
    client,   
    CSConv.to_short(0)
) 
```
By applying these explicit casts, you can ensure proper data type compatibility between Python and C# when using ArbinCTI.

## Arbin Object Creation
Creating **ArbinCTI general objects** ([ArbinCTI](arbintoolbox/src/arbincti/ArbinCTI.md#general-objects), [ArbinClient](arbintoolbox/src/arbinclient/ArbinClient.md#general-objects)) is straightforward:
1. Create the corresponding Python wrapper object. 
2. Convert the object to a C# instance by calling `to_cs`:

```python
from arbintoolbox import MetaVariableInfo, TE_DATA_TYPE
info = MetaVariableInfo(
    channel_index = 0,
    mv_meta_code  = 0,
    mv_data_type  = TE_DATA_TYPE.MP_DATA_TYPE_MetaValue
)
info_cs = info.to_cs()  # Now it is a C# 'MetaVariableInfo' instance
```

Same method applies to C# Enum types required when sending ArbinCTI commands.
```python
from arbintoolbox import NewOrDeleteFeedback
control.PostNewOrDelete(
    client, 
    "file_path", 
    NewOrDeleteFeedback.ENewOrDeleteType.CTI_NEW.to_cs()
)
```

## C# `List` Conversion
This section explains how to create C# `List` instances from Python data using the `CSConv` class.

### List Conversion of Basic Data Types
To create a C# List instance of basic data types:
```python
# Create a C# 'List<ushort>' instance containing items [1, 2, 3]
ushort_list = CSConv.to_list([1, 2, 3], CSConv.EDataType.USHORT)

# Create a C# 'List<string>' instance containing items ["a", "b", "c"]
string_list = CSConv.to_list(["a", "b", "c"], CSConv.EDataType.STRING)
```

### List Conversion of Arbin General Objects
All supported Arbin general objects have a `to_cs` method, which allows `CSConv.to_list` to convert them without requiring a data type flag (`EDataType`), using the following approach:
```python
"""
Example - Calling 'PostStartChannelEx(IArbinSocket socket, List<StartResumeEx> resumeEx, string Creators, string Comments)'
"""
from arbintoolbox import CSConv, StartResumeEx

# Create StartResumeEx objects
a = StartResumeEx(
    # Initialize as needed
)
b = StartResumeEx(
    # Initialize as needed
)

# Convert to C# List<StartResumeEx> instance
resumeEx_list = CSConv.to_list([a, b])

# Send command
control.PostStartChannelEx(client, resumeEx_list, "-", "-")
```

## C# `SortedDictionary` Conversion
This section explains how to create C# `SortedDictionary` instances from Python data using the `CSConv` class, specifically for the `PostUpdateParameters` method in ArbinCTI.

### Example

```python
from arbintoolbox import CSConv
from arbintoolbox.UpdateParameterFeedback import EParameterDataType

# Create a list of key-value pairs. Ensure that the list consists of tuples, each of size 2.
obj_list = [
    (EParameterDataType.NormCapacity, 1.2), 
    (EParameterDataType.IMax, 2.3), 
    (EParameterDataType.VMin, 4.5)
]

# Convert to C# SortedDictionary<ushort, double>
sorted_dict = CSConv.to_cs_sorted_dict(obj_list, CSConv.EDataType.USHORT, CSConv.EDataType.DOUBLE)

# Use the sorted dictionary in a method
control.PostUpdateParameters(client, _, _, sorted_dict)
```

This method ensures that the key-value pairs are properly converted to the specified C# data types, allowing seamless integration with ArbinCTI methods that require `SortedDictionary` instances.

## Arbin Feedback Accessing
When feedback is received, it is a C# instance. You can convert it to a Python object using the feedback wrapper class in `arbintoolbox`, enabling user-friendly access. Additionally, all wrapper classes come with two methods:
- `to_dict` converts the object to a serializable format, easily transformable to JSON, with enum objects represented by their names.
- `__repr__` is defined for quick data inspection.

```python
from arbintoolbox import BrowseDirectoryFeedback

def OnBrowseDirectoryBack(feedback):
    # Convert ArbinCommandBrowseDirectoryFeed to a pythonic BrowseDirectoryFeedback
    feedback = BrowseDirectoryFeedback(feedback)

    # Access attributes
    result = feedback.result
    dir_file_info = feedback.dir_file_info
    for info in dir_file_info:
        size = info.size
        last_modify_time = info.last_modify_time

    # Verify result by enum type
    if feedback.result == BrowseDirectoryFeedback.EResult.CTI_BROWSE_DIRECTORY_SUCCESS:
        # Export as a JSON String
        logger.info(feedback)
        print("Feedback:\n", feedback)

        # Export as a Python dictionary
        print("Python dictionary:\n", feedback.to_dict())
```

Output:
```
Feedback instance:
{
  "result": "CTI_BROWSE_DIRECTORY_SUCCESS",
  "dir_file_info": [
  {
    "type": 1,
    "parent_dir_path": "file1.txt",
    "size": 2048,
    "last_modify_time": "2024-01-01T12:00:00"
  },
  {
    "type": 0,
    "parent_dir_path": "folder1",
    "size": 0,
    "last_modify_time": "2024-01-02T15:30:00"
  }
  ]
}

Python dictionary:
{'result': 'CTI_BROWSE_DIRECTORY_SUCCESS', 'dir_file_info': [{'type': 1, 'parent_dir_path': 'file1.txt', 'size': 2048, 'last_modify_time': '2024-01-01T12:00:00'}, {'type': 0, 'parent_dir_path': 'folder1', 'size': 0, 'last_modify_time': '2024-01-02T15:30:00'}]}
```
