from unittest import TestCase
from scriptingtest import checkIfRelative, checkFile, checkCreate, checkPath

class Testunittests(TestCase):
    def test_checkIfRelative(self):
        input = '/moo/cow/'
        result = checkIfRelative(input)
        assert result is True

    def test_checkIfRelativeFalse(self):
        input = 'c:/moo/cow/'
        result = checkIfRelative(input)
        assert result is False

    def test_checkFileHappy(self):
        input = 'd:test.zip.txt'
        result =checkFile(input)
        assert result is True

    def test_checkFileNotFile(self):
        input = 'd:/test'
        result = checkFile(input)
        assert result is False

    def test_checkFileNotTxt(self):
        input = 'd:/test.zip'
        result = checkFile(input)
        assert result is False

    def test_checkFileDiffRootHappy(self):
        input = 'c:/test.zip.txt'
        result = checkFile(input)
        assert result is True

    def test_checkFileDiffRootFolder(self):
        input = 'c:moo'
        result = checkFile(input)
        assert result is False

    def test_checkCreate(self):
        input = ['moo', 'cow', '-create']
        result = checkCreate(input)
        assert result is True

    def test_checkCreateFalse(self):
        input = ['moo', 'cow']
        result = checkCreate(input)
        assert result is False

    def test_checkPathHappy(self):
        input = '/foo'
        result = checkpath(input)
        assert result == True

    def test_checkPathNotAFolder(self):
        input = 'd:/test.zip'
        result = checkpath(input)
        assert result == False

    def test_checkPathDiffRoot(self):
        input = 'c:/test.zip.txt'
        result = checkpath(input)
        assert result == False

