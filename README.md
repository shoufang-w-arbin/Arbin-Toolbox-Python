# About
New ArbinCTI python wrapper, providing smoother programming experience. 

## Requirements
- 64-bit Python >= 3.7
- System
    - Windows: .NET Framework >=4.7.2
    - Linux: Mono is used by default

## Install from wheel file
`pip install dist/arbincti-python-1.0.0-py3-none-any.whl`

## Client Class

This `Client` class provides the necessary functionality to **establish and manage connections with the Arbin MITS server**, serving as a foundation for further interactions through the Control class.


### Supported Functions

#### Initialization and Cleanup

| Function | Description | Arguments | Function Name in Manual |
|----------|-------------|-----------| ------------------------|
| `subscribe_connection_event(event_handler)` | Subscribe to connection events | N/A |
| `connect(ipv4_addr, port, time_out=0)` | Connect to the MITS server | `ConnectAsync` |
| `is_connected()` | Check if the client is connected to the MITS server | `IsConnected` |
| `shut_down()` | Disconnect from the MITS server and clear resources | `ShutDown` |

### Usage

1. Create a Client instance and connect to the MITS server:
    ```python
    client = Client()
    client.connect("127.0.0.1", 9031)
    ```

2. Subscribe to connection events (optional):
    1. Create a custom event handler:
        ```python
        from arbincti import BaseEventHandler

        class MyEventHandler(BaseEventHandler):
            def handle_event(self, sender, event_args):
                # Implement your custom event handling logic here
                print(f"Connection status changed: {event_args}")

        my_event_handler = MyEventHandler()
        ```
    2. Subscribe to connection events
        ```python
        client.subscribe_connection_event(my_event_handler)
        ```

3. Check connection status:
    ```python
    if client.is_connected():
        print("Connected to MITS server")
    ```
    or 
    ```python
    print(repr(client)) # show connection status and destination address
    ```

4. Perform operations using the client (through the Control class)

5. Shut down the connection when done:
   ```python
   client.shut_down()
   ```


## Control Class

The Control class provides an interface to interact with the Arbin MITS (Modular Integrated Test System) using the ArbinCTI (Control Test Interface). It offers various functions for system management, connection handling, file operations, test configuration, and monitoring.

### Supported Functions

#### System

| Function | Description | Arguments | Name in Manual |
|----------|-------------|-----------|----------------|
| `version()` | Get the version of the ArbinCTI | None | GetCTIVersion |
| `post_get_serial_number()` | Get the serial number of the MITS | None | GetSerialNumber |
| `post_get_mits_version()` | Get the version of the MITS | None | PostGetServerSoftwareVersionNumber |

#### Connection and Authentication

| Function | Description | Arguments | Name in Manual |
|----------|-------------|-----------|----------------|
| `register_client(client)` | Register the client to the control | `client`: Client instance | ListenSocketRecv |
| `post_login(user_name, password)` | Login to the MITS | `user_name`: str, `password`: str | PostUserLogin |

#### File Management

| Function | Description | Arguments | Name in Manual |
|----------|-------------|-----------|----------------|
| `post_upload_file(file_path, timeout, packet_count, packet_index)` | Upload a file to the MITS | `file_path`: str, `timeout`: int (default=0), `packet_count`: int (default=1), `packet_index`: int (default=0) | PostUpLoadFile |
| `post_download_file(file_path, timeout)` | Download a file from the MITS | `file_path`: str, `timeout`: int (default=0) | PostDownloadFile |
| `post_browse_directory(dir_path)` | List files in given directory path | `dir_path`: str | PostBrowseDirectory |

#### Test Configuration

| Function | Description | Arguments | Name in Manual |
|----------|-------------|-----------|----------------|
| `post_assign_file(file_name, file_type, channel_indices, all)` | Assign a file to given channel(s) | `file_name`: str, `file_type`: str ('schedule', 'canbms', 'smb', 'simulation', 'testobject'), `channel_indices`: list of int, `all`: bool (default=False) | PostAssignFile |
| `post_set_meta_variable(channel_index, mv_code, value)` | Set a meta variable to a given channel | `channel_index`: int, `mv_code`: int, `value`: float | PostSetMetaVariable |
| `post_assign_schedule(schedule_name, barcode, capacity, MVUD1, MVUD2, MVUD3, MVUD4, all, channel_index)` | Assign a schedule to given channel(s) (Deprecated) | `schedule_name`: str, `barcode`: str, `capacity`: float, `MVUD1`: float (default=0), `MVUD2`: float (default=0), `MVUD3`: float (default=0), `MVUD4`: float (default=0), `all`: bool (default=False), `channel_index`: int (default=-1) | PostAssignSchedule |

#### Test Control

| Function | Description | Arguments | Name in Manual |
|----------|-------------|-----------|----------------|
| `post_start_test(channel_indices, test_name)` | Start a test on given channel(s) | `channel_indices`: list of int, `test_name`: str | PostStartChannel |
| `post_stop_test(channel_index, all)` | Stop a test on given channel(s) | `channel_index`: int, `all`: bool (default=False) | PostStopChannel |
| `post_resume_test(channel_index, all)` | Resume a test on given channel(s) | `channel_index`: int, `all`: bool (default=False) | PostResumeChannel |
| `post_jump_step(step_number, channel_index)` | Jump to a step on a given channel | `step_number`: int, `channel_index`: int | PostJumpChannel |
| `post_proceed_test(channel_indices)` | Continue the test after a pause step | `channel_indices`: list of int | PostContinueChannel |

#### Test Monitoring

| Function | Description | Arguments | Name in Manual |
|----------|-------------|-----------|----------------|
| `post_get_channel_data(need_type, channel_type, channel_index)` | Get the status of a channel | `need_type`: str ('all', 'aux', 'smb', 'bms'), `channel_type`: str ('all', 'running', 'unsafe'), `channel_index`: int (default=-1) | PostGetChannelData |
| `post_get_resume_data(channel_indices)` | Get the resume status of given channel(s) | `channel_indices`: list of int | PostGetResumeStatus |
| `post_get_channel_assignment(channel_indices)` | Get channel assignments | `channel_indices`: list of int | PostGetStartData |

This updated table includes the "Name in Manual" column, which shows the corresponding function names as they appear in the ArbinCTI manual or internal implementation. This should help users map between the Python wrapper functions and the original ArbinCTI functions.
