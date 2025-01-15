# Usage Examples
## About
Here are some example how to use "pythonnet" and "ctitoolbox" in order to interact smoothly with ArbinCTI.
- [Data Type Casting in Pythonnet](#data-type-casting-in-pythonnet)
  - [Handling TypeError](#handling-typeerror)
- [C# List Conversion using `CSTypeConverter`](#c-list-conversion-using-cstypeconverter)
- [ArbinCTI Object Creation](#arbincti-object-creation)
- [ArbinCTI Feedback Accessing](#arbincti-feedback-accessing)

## Data Type Casting in Pythonnet
Pythonnet doesn't handle casting between Python and C# data types perfectly. Explicit casting is recommended for certain data types. Below is a known data type casting compatibility in Pythonnet.

| Python Type | Pythonnet Type    | C# Type  | Implicit Casting       | Explicit Casting |
|-------------|-------------------|----------|------------------------|------------------|
| `bool`      | `Boolean`         | `bool`   | Yes                    | Yes              |
| `int`       | `Int32`           | `int`    | Yes                    | Yes              |
| `int`       | `UInt32`          | `uint`   | Yes                    | Yes              |
| `float`     | `Single`          | `float`  | Yes                    | Yes              |
| `float`     | `Double`          | `double` | Yes                    | Yes              |
| `str`       | `String`          | `string` | Yes                    | Yes              |
|-|-|-|-|-|
| `bytearray` | `Array` of `Byte` | `byte[]` | **No**                 | Yes              |
| `int`       | `Int16`           | `short`  | **No**                 | Yes              |
| `int`       | `UInt16`          | `ushort` | **No**                 | Yes              |


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
# bool PostUpLoadFile(IArbinSocket socket, string strPath, byte[] FileData, double time, uint uGeneralPackage, uint PackageIndex)
control.PostUpLoadFile(
    client, 
    "path",         # -
    b'filedata',    # 'bytearray' -> 'byte[]'
    0.0,            # -
    1,              # 'int' -> 'uint'          
    0               # 'int' -> 'uint'        
) 
```
This code will raise a TypeError with a message similar to:
```
TypeError: No method matches given arguments for PostUpLoadFile: ...
```

To resolve this issue, use explicit casting. Here's an example using the CSTypeConverter:
```python
control.PostUpLoadFile(
    client, 
    "path",     
    CSTypeConverter.to_cs_byte_array(b'filedata'),  
    0.0,        
    CSTypeConverter.to_uint(1),
    CSTypeConverter.to_uint(0) 
) 
```
By applying these explicit casts, you can ensure proper data type compatibility between Python and C# when using ArbinCTI.

## C# List Conversion using `CSTypeConverter`
This section explains how to create C# List instances from Python data using the CSTypeConverter class.
### Basic Data Types
To create a C# List instance of basic data types:
```python
# Create a C# 'List<ushort>' instance containing items [1, 2, 3]
ushort_list = CSTypeConverter.to_list([1, 2, 3], CSTypeConverter.EDataType.USHORT)

# Create a C# 'List<string>' instance containing items ["a", "b", "c"]
string_list = CSTypeConverter.to_list(["a", "b", "c"], CSTypeConverter.EDataType.STRING)
```
### ArbinCTI General Objects
For creating a C# List of supported [ArbinCTI general objects](README.md#general-objects), use the following approach:
```python
"""
Example: Calling 'bool PostStartChannelEx (IArbinSocket socket, List<StartResumeEx> resumeEx, string Creators, string Comments)'
"""
from ctitoolbox import CSTypeConverter, StartResumeEx

# Create StartResumeEx objects
a = StartResumeEx(
    # Initialize as needed
)
b = StartResumeEx(
    # Initialize as needed
)

# Convert to C# List
resumeEx_list = CSTypeConverter.to_list([a, b]) # Now it is a C# List<StartResumeEx> instance

# Send command
control.PostStartChannelEx(client, resumeEx_list, "-", "-")
```
All supported ArbinCTI general objects have a `to_cs` method, which allows `CSTypeConverter.to_list` to convert them without requiring a data type flag (`EDataType`). This simplifies the conversion process for these objects when creating C# Lists.

## ArbinCTI Object Creation
Creating **ArbinCTI general objects** is straightforward. First, create a Python wrapper object defined in `ctitoolbox`. Then, convert the object to the required C# instance by calling `to_cs`:
```python
from ctitoolbox import MetaVariableInfo, TE_DATA_TYPE

info = MetaVariableInfo(
    channel_index = 0,
    mv_meta_code  = 0,
    mv_data_type  =TE_DATA_TYPE.MP_DATA_TYPE_MetaValue
)

info_cs = info.to_cs()  # Now it is a C# 'MetaVariableInfo' instance
```

In addition to general objects, certain **C# Enum types** required when sending ArbinCTI commands are also supported and can be accessed using `to_cs`. For example:
```python
from ctitoolbox import NewOrDeleteFeedback

control.PostNewOrDelete(
    client, 
    "file_path", 
    NewOrDeleteFeedback.ENewOrDeleteType.CTI_NEW.to_cs()
)
```

## ArbinCTI Feedback Accessing
When feedback is received, it is a C# instance. You can convert it to a Python object using the feedback wrapper class in `ctitoolbox`. 

As mentioned in the [README.md](README.md#feedback-objects), the wrapper class converts C# ArbinCTI feedback objects to Python objects, enabling user-friendly access. Additionally, all wrapper classes come with two methods:
- `to_dict` converts the object to a serializable format, easily transformable to JSON, with enum objects represented by their names.
- `__repr__` is defined for quick data inspection.

```python
from ctitoolbox import BrowseDirectoryFeedback

def OnBrowseDirectoryBack(feedback):
# Convert the feedback to a Python object
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
