from enum import IntEnum
import base64
import copy

import ArbinCTI.Core as ArbinCTI # type: ignore

"""""""""""""""""""""""""""
File Management Feedback
- UploadFileFeedback
- DownloadFileFeedback
- BrowseDirectoryFeedback
- CheckFileExistFeedback
- NewFolderFeedback
- DeleteFileFeedback
- NewOrDeleteFeedback
"""""""""""""""""""""""""""

class UploadFileFeedback:
    class EResult(IntEnum):
        CTI_UPLOAD_SUCCESS = 1
        CTI_UPLOAD_FAILED = 2
        CTI_UPLOAD_MD5_ERR = 3
        CTI_UPLOAD_FAILED_TEXT_RUNNING = 4
        CTI_UPLOAD_FILE_EXIST_WITH_DIFFERENT_MD5 = 5
        CTI_UPLOAD_FILE_EXIST_WITH_SAME_MD5 = 6
        CTI_UPLOAD_FILE_EXIST_NOT_OVERRIDE = 7
        CTI_UPLOAD_FAILED_USER_CANCEL = 8
        CTI_UPLOAD_FAILED_TIMEOUT = 9
        CTI_UPLOAD_FAILED_CHECK_FILE_TIMEOUT = 10
        CTI_UPLOAD_IN_PROGRESS = 11

    class UploadFileResult:
        def __init__(self, upload_file_result: ArbinCTI.ArbinCommandUpLoadFileFeed.CUpLoadFileResult):  
            self.result_code    = UploadFileFeedback.EResult(int(upload_file_result.ResultCode))
            self.canceled       = bool(upload_file_result.IsCancelUploadFile)
            self.progress_rate  = float(upload_file_result.ProgressRate)
        
        def to_dict(self):
            data = copy.deepcopy(self.__dict__)
            data['result_code'] = self.result_code.name
            return data

    def __init__(self, feedback: ArbinCTI.ArbinCommandUpLoadFileFeed): 
        self.result       = UploadFileFeedback.EResult(int(feedback.Result))
        self.upload_time  = float(feedback.UploadTime)
        self.packet_count = int(feedback.uGeneralPackage)
        self.packet_index = int(feedback.uPackageIndex)
    
    def to_dict(self):
        data = copy.deepcopy(self.__dict__)
        data['result'] = self.result.name
        return data
    
class DownloadFileFeedback:
    class EResult(IntEnum):
        CTI_DOWNLOAD_SUCCESS = 1,
        CTI_DOWNLOAD_FAILED = 2,
        CTI_DOWNLOAD_MD5_ERR = 3,
        CTI_DOWNLOAD_MAX_LENGTH_ERR = 4

    def __init__(self, feedback: ArbinCTI.ArbinCommandDownLoadFileFeed):
        self.result         = DownloadFileFeedback.EResult(int(feedback.Result))
        self.md5            = str(feedback.m_MD5)
        self.file_length    = int(feedback.dwFileLength)
        self.data_in_base64 = base64.b64encode(bytearray(feedback.byData)).decode("utf-8") # Convert to base64 for JSON
        self.download_time  = float(feedback.DownloadTime)
        self.upload_time    = float(feedback.UploadTime)
        self.package_count  = int(feedback.uGeneralPackage)
        self.package_index  = int(feedback.uPackageIndex)

    def to_dict(self):
        data = copy.deepcopy(self.__dict__)
        data['result'] = self.result.name
        return data

class BrowseDirectoryFeedback:
    class EResult(IntEnum):
        CTI_BROWSE_DIRECTORY_SUCCESS = 1,
        CTI_BROWSE_SCHEDULE_SUCCESS = 2,
        CTI_BROWSE_SCHEDULE_VERSION1_SUCCESS = 3,
        CTI_BROWSE_DIRECTORY_FAILED = 4
    
    class DirFileInfo:
        def __init__(self, info: ArbinCTI.ArbinCommandBrowseDirectoryFeed.DirFileInfo): 
            self.type_              = int(info.Type)
            self.parent_dir_path    = str(info.DirFileName)
            self.size               = int(info.dwSize)
            self.last_modify_time   = str(info.wcModified)
        
        def to_dict(self):
            return self.__dict__

    def __init__(self, feedback: ArbinCTI.ArbinCommandBrowseDirectoryFeed):
        self.result         = BrowseDirectoryFeedback.EResult(int(feedback.Result))
        self.dir_file_info  = [BrowseDirectoryFeedback.DirFileInfo(info) for info in feedback.DirFileInfoList]

    def to_dict(self):
        data = {
            "result": self.result.name,
            "dir_file_info": [info.to_dict() for info in self.dir_file_info]
        }
        return data
    
class CheckFileExistFeedback:
    def __init__(self, feedback: ArbinCTI.ArbinCommandCheckFileExFeed):
        self.relative_path_exist = bool(feedback.bRelativePathExist)
        self.file_name_exist     = bool(feedback.bFileNameExist)
        self.MD5_exist           = bool(feedback.bMD5Exist)
        self.file_path           = str(feedback.FilePath)
        self.reason              = str(feedback.Reason)

    def to_dict(self):
        return self.__dict__
    
class NewFolderFeedback:
    class EResult(IntEnum):
        CTI_NEW_SUCCESS = 1
        CTI_DELETE_SUCCESS = 2
        CTI_NEW_FAILED = 3
        CTI_NEW_FAILED_ADD_FOLDER = 4
        CTI_DELETE_FAILED = 5
        CTI_DELETE_FAILED_EXTENSION = 6
        CTI_DELETE_FAILED_TEXT_RUNNING = 7
        CTI_DELETE_FAILED_EXIST = 8

    def __init__(self, feedback: ArbinCTI.ArbinCommandNewFolderFeed):
        self.result = NewFolderFeedback.EResult(int(feedback.Result))

    def to_dict(self):
        data = copy.deepcopy(self.__dict__)
        data['result'] = self.result.name
        return data
    
class DeleteFileFeedback:
    class EResult(IntEnum):
        CTI_NEW_SUCCESS = 1
        CTI_DELETE_SUCCESS = 2
        CTI_NEW_FAILED = 3
        CTI_NEW_FAILED_ADD_FOLDER = 4
        CTI_DELETE_FAILED = 5
        CTI_DELETE_FAILED_EXTENSION = 6
        CTI_DELETE_FAILED_TEXT_RUNNING = 7
        CTI_DELETE_FAILED_EXIST = 8

    def __init__(self, feedback: ArbinCTI.ArbinCommandDeleteFileFeed):
        self.result = DeleteFileFeedback.EResult(int(feedback.Result))

    def to_dict(self):
        data = copy.deepcopy(self.__dict__)
        data['result'] = self.result.name
        return data
    
class NewOrDeleteFeedback:
    class EResult(IntEnum):
        CTI_NEW_SUCCESS = 1
        CTI_DELETE_SUCCESS = 2
        CTI_NEW_FAILED = 3
        CTI_NEW_FAILED_ADD_FOLDER = 4
        CTI_DELETE_FAILED = 5
        CTI_DELETE_FAILED_EXTENSION = 6
        CTI_DELETE_FAILED_TEXT_RUNNING = 7
        CTI_DELETE_FAILED_EXIST = 8

    class ENewOrDelete(IntEnum):
        CTI_NEW = 0
        CTI_DELETE = 1

    def __init__(self, feedback: ArbinCTI.ArbinCommandNewOrDeleteFeed):
        self.result = NewOrDeleteFeedback.EResult(int(feedback.Result))

    def to_dict(self):
        data = copy.deepcopy(self.__dict__)
        data['result'] = self.result.name
        return data