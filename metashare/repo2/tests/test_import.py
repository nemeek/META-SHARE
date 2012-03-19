import os
from django.test import TestCase
from metashare import test_utils
from metashare.settings import ROOT_PATH
from metashare.repo2.models import resourceInfoType_model

class ImportTest(TestCase):
    """
    Tests the import procedure for resources
    """
    def setUp(self):
        """
        Set up the import test
        """        
        test_utils.setup_test_storage()
        
    def tearDown(self):
        """
        Clean up the test
        """
        resourceInfoType_model.objects.all().delete()
    
    if False:
        def testImportELRA(self):      
            """
            run tests on ELRA resources
            """
            _path = '{0}/../misc/testdata/ELRAResources/'.format(ROOT_PATH)
            
            _files = os.listdir(_path)
            for _file in _files:
                _currfile =  "%s%s" % (_path, _file)
                successes, failures = test_utils.import_xml_or_zip(_currfile)
                self.assertEqual(1, len(successes), 'Could not import file {}'.format(_currfile))
                self.assertEqual(0, len(failures), 'Could not import file {}'.format(_currfile))
            
    def test_import_xml(self):
        _currfile = '{}/repo2/fixtures/testfixture.xml'.format(ROOT_PATH)
        successes, failures = test_utils.import_xml_or_zip(_currfile)
        self.assertEqual(1, len(successes), 'Could not import file {}'.format(_currfile))
        self.assertEqual(0, len(failures), 'Could not import file {}'.format(_currfile))

    def test_broken_xml(self):
        _currfile = '{}/repo2/fixtures/broken.xml'.format(ROOT_PATH)
        successes, failures = test_utils.import_xml_or_zip(_currfile)
        self.assertEqual(0, len(successes), 'Should not have been able to import file {}'.format(_currfile))
        self.assertEqual(1, len(failures), 'Should not have been able to import file {}'.format(_currfile))
        
    def test_import_zip(self):
        _currfile = '{}/repo2/fixtures/tworesources.zip'.format(ROOT_PATH)
        successes, failures = test_utils.import_xml_or_zip(_currfile)
        self.assertEqual(2, len(successes), 'Could not import file {}'.format(_currfile))
        self.assertEqual(0, len(failures), 'Could not import file {}'.format(_currfile))
    