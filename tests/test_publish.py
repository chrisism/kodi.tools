import unittest, os, shutil
import unittest.mock
from unittest.mock import MagicMock, patch

import logging

logging.basicConfig(format = '%(asctime)s %(module)s %(levelname)s: %(message)s',
                datefmt = '%m/%d/%Y %I:%M:%S %p', level = logging.DEBUG)
logger = logging.getLogger(__name__)

import src.kodi_tools.publish as target

class Test_publish(unittest.TestCase):
    
    @unittest.skip("work to do")
    def test_changing_markdown_to_kodi_txt(self):
        # arrange
        work_dir = "/home/projects/kodi/skin.arctic.zephyr/skin.arctic.zephyr.2.resurrection.mod/"
        srcs = "**/*.md:**/*.xml:**/*.txt:**/*.jpg:**/*.png:1080i/*.xml"
        
        source_paths = srcs.split(os.pathsep)

        # act
        actual = target._get_files_for_addon(work_dir, source_paths)

        # assert
        assert actual is not None

