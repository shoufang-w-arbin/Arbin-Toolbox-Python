import os
import unittest
import base64

from System.Collections.Generic import List  # type: ignore
import ArbinCTI.Core as ArbinCTI  # type: ignore

from ctitoolbox.src.feedback.file_management import (
    UploadFileFeedback,
    DownloadFileFeedback,
    BrowseDirectoryFeedback,
    CheckFileExistFeedback,
    NewFolderFeedback,
    DeleteFileFeedback,
    NewOrDeleteFeedback,
)

UNITTEST_VIEW_DICT = os.getenv("UNITTEST_VIEW_DICT", False)

class TestFileManagementFeedbackClasses(unittest.TestCase):

    def test_UploadFileFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandUpLoadFileFeed()
        cs_instance.Result = ArbinCTI.ArbinCommandUpLoadFileFeed.UPLOAD_RESULT.CTI_UPLOAD_SUCCESS
        cs_instance.UploadTime = 12.34
        cs_instance.uGeneralPackage = 5
        cs_instance.uPackageIndex = 2

        feedback_instance = UploadFileFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, UploadFileFeedback.EResult.CTI_UPLOAD_SUCCESS)
        self.assertEqual(feedback_instance.upload_time, 12.34)
        self.assertEqual(feedback_instance.packet_count, 5)
        self.assertEqual(feedback_instance.packet_index, 2)

        if UNITTEST_VIEW_DICT:
            print("UploadFileFeedback:", feedback_instance.to_dict())

    def test_DownloadFileFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandDownLoadFileFeed()
        cs_instance.Result = ArbinCTI.ArbinCommandDownLoadFileFeed.DOWNLOAD_RESULT.CTI_DOWNLOAD_MD5_ERR
        cs_instance.m_MD5 = "abcd1234efgh5678"
        cs_instance.dwFileLength = 1024
        cs_instance.byData = b'\x00\x01\x02\x03'
        cs_instance.DownloadTime = 23.45
        cs_instance.UploadTime = 34.56
        cs_instance.uGeneralPackage = 10
        cs_instance.uPackageIndex = 3

        feedback_instance = DownloadFileFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, DownloadFileFeedback.EResult.CTI_DOWNLOAD_MD5_ERR)
        self.assertEqual(feedback_instance.md5, "abcd1234efgh5678")
        self.assertEqual(feedback_instance.file_length, 1024)
        self.assertEqual(base64.b64decode(feedback_instance.data_in_base64), bytearray(b'\x00\x01\x02\x03'))
        self.assertEqual(feedback_instance.download_time, 23.45)
        self.assertEqual(feedback_instance.upload_time, 34.56)
        self.assertEqual(feedback_instance.package_count, 10)
        self.assertEqual(feedback_instance.package_index, 3)

        if UNITTEST_VIEW_DICT:
            print("DownloadFileFeedback:", feedback_instance.to_dict())

    def test_BrowseDirectoryFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandBrowseDirectoryFeed()
        cs_instance.Result = ArbinCTI.ArbinCommandBrowseDirectoryFeed.BROWSE_DIRECTORY_RESULT.CTI_BROWSE_DIRECTORY_SUCCESS
        cs_instance.DirFileInfoList = List[ArbinCTI.ArbinCommandBrowseDirectoryFeed.DirFileInfo]()

        # Create DirFileInfo instances
        dir_file_info_1 = ArbinCTI.ArbinCommandBrowseDirectoryFeed.DirFileInfo()
        dir_file_info_1.Type = 1
        dir_file_info_1.DirFileName = "file1.txt"
        dir_file_info_1.dwSize = 2048
        dir_file_info_1.wcModified = "2024-01-01T12:00:00"

        dir_file_info_2 = ArbinCTI.ArbinCommandBrowseDirectoryFeed.DirFileInfo()
        dir_file_info_2.Type = 0
        dir_file_info_2.DirFileName = "folder1"
        dir_file_info_2.dwSize = 0
        dir_file_info_2.wcModified = "2024-01-02T15:30:00"

        [cs_instance.DirFileInfoList.Add(info) for info in [dir_file_info_1, dir_file_info_2]]

        feedback_instance = BrowseDirectoryFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, BrowseDirectoryFeedback.EResult.CTI_BROWSE_DIRECTORY_SUCCESS)
        self.assertEqual(len(feedback_instance.dir_file_info), 2)

        # Validate first DirFileInfo
        self.assertEqual(feedback_instance.dir_file_info[0].type_, 1)
        self.assertEqual(feedback_instance.dir_file_info[0].parent_dir_path, "file1.txt")
        self.assertEqual(feedback_instance.dir_file_info[0].size, 2048)
        self.assertEqual(feedback_instance.dir_file_info[0].last_modify_time, "2024-01-01T12:00:00")

        # Validate second DirFileInfo
        self.assertEqual(feedback_instance.dir_file_info[1].type_, 0)
        self.assertEqual(feedback_instance.dir_file_info[1].parent_dir_path, "folder1")
        self.assertEqual(feedback_instance.dir_file_info[1].size, 0)
        self.assertEqual(feedback_instance.dir_file_info[1].last_modify_time, "2024-01-02T15:30:00")

        if UNITTEST_VIEW_DICT:
            print("BrowseDirectoryFeedback:", feedback_instance.to_dict())

    def test_CheckFileExistFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandCheckFileExFeed()
        cs_instance.bRelativePathExist = True
        cs_instance.bFileNameExist = False
        cs_instance.bMD5Exist = True
        cs_instance.FilePath = "/path/to/file.txt"
        cs_instance.Reason = "File partially exists."

        feedback_instance = CheckFileExistFeedback(cs_instance)

        self.assertTrue(feedback_instance.relative_path_exist)
        self.assertFalse(feedback_instance.file_name_exist)
        self.assertTrue(feedback_instance.MD5_exist)
        self.assertEqual(feedback_instance.file_path, "/path/to/file.txt")
        self.assertEqual(feedback_instance.reason, "File partially exists.")

        if UNITTEST_VIEW_DICT:
            print("CheckFileExistFeedback:", feedback_instance.to_dict())

    def test_NewFolderFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandNewFolderFeed()
        cs_instance.Result = ArbinCTI.ArbinCommandNewFolderFeed.RESULT_TYPE.CTI_NEW_FAILED_ADD_FOLDER

        feedback_instance = NewFolderFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, NewFolderFeedback.EResult.CTI_NEW_FAILED_ADD_FOLDER)

        if UNITTEST_VIEW_DICT:
            print("NewFolderFeedback:", feedback_instance.to_dict())

    def test_DeleteFileFeedback_instantiation(self):
        cs_instance = ArbinCTI.ArbinCommandDeleteFileFeed()
        cs_instance.Result = ArbinCTI.ArbinCommandDeleteFileFeed.DELETE_RESULT.CTI_DELETE_SUCCESS

        feedback_instance = DeleteFileFeedback(cs_instance)

        self.assertEqual(feedback_instance.result, DeleteFileFeedback.EResult.CTI_DELETE_SUCCESS)

        if UNITTEST_VIEW_DICT:
            print("DeleteFileFeedback:", feedback_instance.to_dict())

    def test_NewOrDeleteFeedback_instantiation(self):
        # Test for CTI_NEW
        cs_instance_new = ArbinCTI.ArbinCommandNewOrDeleteFeed()
        cs_instance_new.Result = ArbinCTI.ArbinCommandNewOrDeleteFeed.NEW_OR_DELETE_RESULT.CTI_DELETE_FAILED

        feedback_instance = NewOrDeleteFeedback(cs_instance_new)

        self.assertEqual(feedback_instance.result, NewOrDeleteFeedback.EResult.CTI_DELETE_FAILED)

        if UNITTEST_VIEW_DICT:
            print("NewOrDeleteFeedback:", feedback_instance.to_dict())

    def test_AssignFileFeedback_EFileKind_to_cs(self):
        for kind in NewOrDeleteFeedback.ENewOrDelete:
            with self.subTest(kind=kind):
                cs_kind = kind.to_cs()
                self.assertEqual(cs_kind, ArbinCTI.ArbinCommandNewOrDeleteFeed.NEW_OR_DELETE_TYPE(kind.value))

    def test_to_async_callback(self):
        def mock_callback(result):
            self.assertIsInstance(result, ArbinCTI.ArbinCommandUpLoadFileFeed.CUpLoadFileResult)
            self.assertEqual(result.ResultCode, ArbinCTI.ArbinCommandUpLoadFileFeed.UPLOAD_RESULT.CTI_UPLOAD_SUCCESS)
            self.assertFalse(result.IsCancelUploadFile)
            self.assertEqual(result.ProgressRate, 100.0)

        # Valid callback
        async_callback = UploadFileFeedback.UploadFileResult.to_async_callback(mock_callback)
        self.assertIsInstance(async_callback, ArbinCTI.ArbinCommandUpLoadFileFeed.CUpLoadFileResult.AsyncCallback)

        # Simulate C# callback execution
        cs_result = ArbinCTI.ArbinCommandUpLoadFileFeed.CUpLoadFileResult()
        cs_result.ResultCode = ArbinCTI.ArbinCommandUpLoadFileFeed.UPLOAD_RESULT.CTI_UPLOAD_SUCCESS
        cs_result.IsCancelUploadFile = False
        cs_result.ProgressRate = 100.0
        async_callback(cs_result)

        # Invalid callback: not callable
        with self.assertRaises(TypeError):
            UploadFileFeedback.UploadFileResult.to_async_callback("not a callable")

        # Invalid callback: wrong argument count
        def invalid_callback():
            pass

        with self.assertRaises(ValueError):
            UploadFileFeedback.UploadFileResult.to_async_callback(invalid_callback)
