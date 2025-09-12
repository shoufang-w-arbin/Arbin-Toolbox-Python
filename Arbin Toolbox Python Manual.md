# Arbin Toolbox Python Manual

## 1. Introduction
This manual provides step-by-step instructions for installing and using the Arbin Toolbox Python package to integrate with Arbin battery test hardware. It is designed for integration users who want to automate or monitor Arbin hardware using Python scripts. No programming or internal code knowledge is required.

## 2. System Requirements
- Arbin hardware and software (MITS 10.5.2 patch or later, or MITS 11)
- Windows OS (MITS 10.5.2+) or Windows/Linux OS (MITS 11)
- Python 3.7 or newer
- Arbin Toolbox Python package (provided by Arbin)
- Required DLLs: ArbinClient.dll, ArbinDataModel.dll (provided by Arbin)

## 3. Installation Instructions

### Step 1: Install the Python Package
- Obtain the package file (e.g., arbinclienttools-0.1.2-py3-none-any.whl) from Arbin.
- Open a command prompt or PowerShell window.
- Run:
  - `pip install arbinclienttools-0.1.2-py3-none-any.whl`

### Step 2: Install Required DLLs
- Copy ArbinClient.dll and ArbinDataModel.dll to the same folder as your Python script, or add their location to your system PATH.
- If you downloaded the DLLs, right-click each file, select Properties, and click "Unblock" if available.

### Step 3: Install Python Dependencies
- If you received a requirements.txt file, run:
  - `pip install -r requirements.txt`
- If prompted, also run:
  - `pip install pythonnet`

### Step 4: Verify Installation
- Open Python and type:
  - `import arbinclienttools`
- If no errors appear, installation is successful.

## 4. Using the Toolbox
- After installation, you can use the provided example scripts or instructions from Arbin to connect, control, and monitor your hardware.
- Programming knowledge is required to use this toolbox, but you do not need to know any .NET DLL details or internal code. You can focus on writing Python scripts and logic for your integration tasks.

## 5. Troubleshooting & FAQ

### Troubleshooting
- **DLL Not Found:**
  - Ensure DLLs are in the same folder as your script or in your PATH.
  - Unblock DLLs if downloaded from the internet.
- **Connection Failed:**
  - Verify IP address, username, password, and network connectivity.
  - Check for error messages and contact Arbin support if needed.
- **Python Import Errors:**
  - Ensure all dependencies are installed.
  - Use a compatible Python version.
- **No Data Received:**
  - Confirm the client is connected and hardware is running.
  - Contact Arbin support for help with configuration.

### FAQ
- **Can I use this toolbox on Linux?**
  - MITS 11 supports Linux, but additional setup may be required. Contact Arbin support for details.
- **How do I update the DLLs?**
  - Replace the DLL files with the latest versions provided by Arbin.
- **Where do I find error code meanings?**
  - Refer to Arbin documentation or contact support.
- **Can I run multiple clients in parallel?**
  - Yes, but ensure each client uses separate connection settings.

## 6. Support
If you encounter any issues or need help, contact Arbin support or refer to the official documentation provided with your hardware.

## 7. Example Script: Basic Usage

Below is a simple example script to help you get started with the Arbin Toolbox Python package. This script demonstrates how to:
- Connect to Arbin hardware
- Check connection status
- Subscribe to monitor data

```python
from arbinclienttools.src.argument.connection import CreateArbinClientArgs
from arbinclienttools.src.argument.request_info import SubscribeMonitorDataArgs
import ArbinClient.Core as ArbinClient

# Step 1: Set up connection arguments
args = CreateArbinClientArgs(
    timeout=30,
    ip_address="192.168.1.100",  # Replace with your Arbin server IP
    user_name="your_username",   # Replace with your username
    password="your_password"     # Replace with your password
)

# Step 2: Create ArbinClient instance and connect
cs_args = args.to_cs()
m_client, nErrorCode = ArbinClient.ArbinClient.CreateArbinClient(cs_args, 0)
if nErrorCode == 0:
    print("Connection established successfully.")
else:
    print(f"Connection failed with error code: {nErrorCode}")
    exit(1)

# Step 3: Check connection status
if m_client.IsConnected():
    print("Client is connected to the server.")
else:
    print("Client is not connected.")
    exit(1)

# Step 4: Subscribe to monitor data
args_monitor = SubscribeMonitorDataArgs()
subscription = m_client.SubscribeMonitorData(args_monitor.to_cs())
for data in subscription:
    print(data)  # Data is updated every second
    # Add your own logic to process or save the data
```

---

Replace the IP address, username, and password with your actual Arbin system credentials. For more advanced usage, contact Arbin support or refer to additional documentation.

## 8. Module Structure and Class Purpose

The Arbin Toolbox Python package is organized into three main modules, each with specific roles for integration tasks:

### 8.1 argument
Contains classes for sending commands and requests to the Arbin hardware. Submodules include:
- **channel_management**: For starting, stopping, and managing test channels.
- **common**: Shared argument classes used across different operations.
- **connection**: For setting up and managing connections to Arbin hardware.
- **formation_management**: For managing tray engagement and formation operations.
- **request_info**: For requesting and subscribing to data (e.g., monitor data, barcode info).
- **ttest_management**: For test management operations, such as file uploads and schedule modifications.

### 8.2 common
Provides shared utilities and base classes used throughout the toolbox. Includes:
- **base**: Base classes for object representation and serialization.
- **cs_conv**: Utilities for converting between Python and .NET data types.

### 8.3 feedback
Contains classes for handling responses and feedback from the Arbin hardware. Submodules mirror those in `argument`:
- **channel_management**: For receiving feedback about channel operations.
- **common**: Shared feedback classes.
- **connection**: For connection status and feedback.
- **formation_management**: For feedback on tray engagement and formation.
- **request_info**: For feedback on data requests and subscriptions.
- **ttest_management**: For feedback on test management operations.

**How to Use:**
- Use the `argument` module to send commands and requests.
- Use the `feedback` module to handle responses and monitor results.
- Use the `common` module for shared utilities and base functionality.

## 9. Class and Method Reference (Argument Submodules)

### channel_management
- **ChannelResumeData**: Holds data for resuming a channel/test.
  - Required: channel_id, test_id, test_names, schedule_name, step_id, sub_step_id, cycle_id, test_time, step_time, charge_capacity, discharge_capacity, charge_energy, discharge_energy, etc. (all default to 0 or empty)
- **StartChannelArgs**: Arguments to start a test channel.
  - Required: sn, creator, comment, channel_resume_data (list of ChannelResumeData)
- **StopChannelArgs**: Arguments to stop a test channel.
  - Required: sn, channel_id, is_stop_all_channel
- **JumpStepArgs**: Arguments to jump to a specific step in a test channel.
  - Required: sn, step_id, sub_step_id, channel_id
- **ResumeChannelArgs**: Arguments to resume a test channel.
  - Required: sn, resume_data (list of ChannelResumeData)
- **ContinueChannelArgs**: Arguments to continue a test channel.
  - Required: sn, channel_id (list)

### common
- **AIMetaVariableInfo**: Meta variable information for Arbin tests.
  - Required: global_id, meta_variable_type, index_, value
- **BarcodeInfo**: Barcode information for Arbin tests.
  - Required: barcode_type, barcode, global_id, info, result, barcode_result
- **GetBarcodeInfo**: Arguments to get barcode info.
  - Required: barcode_type, global_id

### connection
- **CreateArbinClientArgs**: Connection parameters for Arbin hardware.
  - Required: timeout, ip_address, user_name, password

### formation_management
- **SPTTEngageTray**: Tray engagement parameters.
  - Required: global_id, engage, result, engagement_result
- **GetEngagementStatusArgs**: Arguments to get engagement status.
  - Required: sn, engagement_id (list)
- **EngageTrayArgs**: Arguments to engage tray.
  - Required: sn, engage_tray (list of SPTTEngageTray)

### request_info
- **GetMonitorDataArgs**: Arguments to request monitor data.
  - Required: sn, need_type, channel_id, filter_monitor_channel_type
- **GetResumeDataArgs**: Arguments to request resume data.
  - Required: sn, channel_id (list)
- **GetStartDataArgs**: Arguments to request start data.
  - Required: sn, channel_id (list)
- **GetMetaVariablesArgs**: Arguments to request meta variables.
  - Required: sn, meta_variable_type (list of AIMetaVariableInfo)
- **GetBarcodeInfoArgs**: Arguments to request barcode info.
  - Required: sn, barcode_info (list of GetBarcodeInfo)
- **GetMappingAuxArgs**: Arguments to request mapping aux data.
  - No required parameters.
- **SubscribeMonitorDataArgs**: Arguments to subscribe to monitor data.
  - No required parameters.
- **SubscribeChannelDataArgs**: Arguments to subscribe to channel data.
  - No required parameters.
- **SubscribeTestInfoDataArgs**: Arguments to subscribe to test info data.
  - No required parameters.
- **SubscribeEventDataArgs**: Arguments to subscribe to event data.
  - No required parameters.
- **SubscribeDiagnosticEventDataArgs**: Arguments to subscribe to diagnostic event data.
  - No required parameters.
- **SubscribeSPTTEQCellDataArgs**: Arguments to subscribe to SPTTEQCell data.
  - No required parameters.

### ttest_management
- **SafetyScope**: Safety scope for test management.
  - Required: low, high
- **AuxChannelRequirementBase**: Base requirements for auxiliary channels.
  - Required: enable, aux_count
- **AuxChannelRequirement**: Requirements for auxiliary channels with safety scope.
  - Required: enable, aux_count, safety_scope
- **AuxSafetyRequirement**: Safety requirements for auxiliary channels.
  - Required: enable, aux_count, temperature_safety_scope, current_safety_scope, voltage_safety_scope
- **ScheduleModifyInfo**: Information for schedule modification.
  - Required: schedule_name, aux_do_requirement, aux_ao_requirement, canbms_requirement, smb_requirement, aux_voltage_requirement, aux_temperature_requirement, aux_pressure_requirement, aux_di_requirement, aux_external_charge_requirement, aux_humidity_requirement, aux_safety_requirement
- **UploadFileArgs**: Arguments to upload a file.
  - Required: remote_relative_file_name, local_full_file_name, is_overwrite, callback_func
- **BrowseFileListArgs**: Arguments to browse file list.
  - Required: sn, file_type
- **ModifyScheduleArgs**: Arguments to modify schedule.
  - Required: schedule_modify_info (list of ScheduleModifyInfo)
- **AssignFileArgs**: Arguments to assign a file.
  - Required: sn, channel_id (list), file_name, file_type
- **UpdateMetaVariablesArgs**: Arguments to update meta variables.
  - Required: sn, meta_variable_info (list of AIMetaVariableInfo)
- **AssignBarcodeInfoArgs**: Arguments to assign barcode info.
  - Required: sn, barcode_info (list of BarcodeInfo)
- **TimeSensitiveSetMV**: Arguments for time-sensitive meta variable setting.
  - Required: mvud, value
- **TimeSensitiveSetMVChannel**: Arguments for time-sensitive meta variable setting per channel.
  - Required: channel_id, mv_list (list of TimeSensitiveSetMV), log
- **TimeSensitiveSetMVArgs**: Arguments for time-sensitive meta variable setting (all channels).
  - Required: timeout, channel_list (list of TimeSensitiveSetMVChannel), sn


## 10. Feedback Class Reference (Feedback Submodules)

### channel_management
- **StartChannelFeedback**: Provides feedback after starting a channel. Includes successful channel IDs, failed results, status, and SN.
- **StopChannelFeedback**: Provides feedback after stopping a channel. Includes channel ID, result, stop result, and SN.
- **JumpStepFeedback**: Feedback for jump step operation. Includes channel ID, result, jump step result, and SN.
- **ResumeChannelFeedback**: Feedback for resume channel operation. Includes successful channel IDs, failed results, status, and SN.
- **ContinueChannelFeedback**: Feedback for continue channel operation. Includes successful channel IDs, failed results, status, and SN.

### common
- **CANMonitorInfo**: CAN monitor information (alias name, meta name).
- **SMBMonitorInfo**: SMB monitor information.
- **AuxData**: Auxiliary data feedback.
- **SPTTEQMonitorData**: SPTTEQ monitor data feedback.
- **SPTTCellMonitorData**: SPTT cell monitor data feedback.
- **SubChannelInfo**: Sub-channel information feedback.
- **ShowUDSMessageValue**: UDS message value feedback.
- **SimulationInfo**: Simulation information feedback.
- **AuxMapping**: Auxiliary mapping feedback.
- **ChannelMonitorData**: Channel monitor data feedback.
- **BarcodeInfo**: Barcode information feedback.
- **AIMetaVariableInfo**: Meta variable information feedback.

### connection
- **LoginFeedback**: Feedback after login operation. Includes user info, system config file, server info, and SN.

### formation_management
- **GetEngagementStatusFeedback**: Feedback for engagement status. Includes engagement status, meta values, and SN.
- **EngageTrayFeedback**: Feedback for tray engagement operation.

### request_info
- **GetStartDataFeedback**: Feedback for start data request.
- **GetResumeDataFeedback**: Feedback for resume data request.
- **GetMonitorDataFeedback**: Feedback for monitor data request.
- **GetBarcodeInfoFeedback**: Feedback for barcode info request.
- **SubscribeMonitorDataFeedback**: Feedback for monitor data subscription.
- **SubscribeChannelDataFeedback**: Feedback for channel data subscription.
- **SubscribeTestInfoDataFeedback**: Feedback for test info data subscription.
- **SubscribeEventDataFeedback**: Feedback for event data subscription.
- **SubscribeDiagnosticEventDataFeedback**: Feedback for diagnostic event data subscription.
- **SubscribeSPTTEQCellDataFeedback**: Feedback for SPTTEQCell data subscription.

### ttest_management
- **UploadFileResult**: Feedback for file upload operation. Includes result, upload result, cancel status, and progress rate.
- **BrowseFileListFeedback**: Feedback for browsing file list. Includes directory/file info.
- **AssignFileFeedback**: Feedback for file assignment operation.
- **UpdateMetaVariableFeedback**: Feedback for meta variable update operation.
- **GetMetaVariablesFeedback**: Feedback for meta variable request.
- **AssignBarcodeInfoFeedback**: Feedback for barcode info assignment.
- **TimeSensitiveSetMVFeedback**: Feedback for time-sensitive meta variable setting.

---



