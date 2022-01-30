import unittest, os, shutil
import unittest.mock
from unittest.mock import MagicMock, patch

import logging

logging.basicConfig(format = '%(asctime)s %(module)s %(levelname)s: %(message)s',
                datefmt = '%m/%d/%Y %I:%M:%S %p', level = logging.DEBUG)
logger = logging.getLogger(__name__)

import src.kodi_tools.update_news as target

class Test_update_news(unittest.TestCase):
    
    def test_changing_markdown_to_kodi_txt(self):
        # arrange
        test_dir = os.path.dirname(os.path.abspath(__file__))
        test_assets_dir = os.path.abspath(os.path.join(test_dir,'assets/'))
        test_output_dir = os.path.abspath(os.path.join(test_dir,'output/'))
        
        input_file  = os.path.join(test_assets_dir, 'input.md')
        output_file = os.path.join(test_output_dir, 'addon.xml')
        origin_file = os.path.join(test_assets_dir, 'addon.xml')

        if not os.path.exists(test_output_dir): os.makedirs(test_output_dir)
        if os.path.exists(output_file): os.unlink(output_file)
        shutil.copy(origin_file, output_file)

        # act
        target.update_news(output_file, input_file)

        # assert
        with open(output_file, 'r') as f:
            actual = f.read()
        print(actual)

        assert len(actual) > 0
        assert 'Kermit' in actual
        