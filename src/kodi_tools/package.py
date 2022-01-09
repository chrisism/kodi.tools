# -*- coding: utf-8 -*-
#
# Addon Package Tool
# 

# --- Python standard library ---
from __future__ import unicode_literals
from __future__ import division

import os
import logging
import subprocess

logger = logging.getLogger(__name__)


def pack(working_directory: str, packer_src_files: str, packer_dst_files:str):
    
    tool_path = os.path.join(working_directory, '.build', 'tools', 'kodi-texturepacker', 'linux')
    tool_path = os.path.join(tool_path, 'TexturePacker')
    command = [
        tool_path, 
        '-dupecheck', 
        f'-input {os.path.join(working_directory, packer_src_files)}',
        f'-output {os.path.join(working_directory, packer_dst_files)}'
    ]

    cmd = ' '.join(command)
    logger.info(f'TexturePacker CMD: {cmd}')
    retcode = subprocess.call(cmd, shell=True, close_fds = True)
    logger.info(f'TexturePacker: {retcode}')

if __name__ == '__main__':
    try:
        working_directory    = os.getenv('PWD')
        
        packer_src_files     = os.getenv('PACKER_FILES_SRC')
        packer_dst_files     = os.getenv('PACKER_FILES_DEST')

        if not working_directory.endswith(os.path.sep):
            working_directory = f'{working_directory}{os.path.sep}'

        pack(working_directory, packer_src_files, packer_dst_files)
    except Exception as ex:
        logger.fatal('Exception in tool', exc_info=ex)