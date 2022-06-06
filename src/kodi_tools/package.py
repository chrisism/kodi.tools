# -*- coding: utf-8 -*-
#
# Addon Package Tool
# 

# --- Python standard library ---
from __future__ import unicode_literals
from __future__ import division

import os
import sys
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

def main():
    try:
        packer_src_files = None
        packer_dst_files = None

        if len(sys.argv) > 2:
            packer_src_files = sys.argv[1]
            packer_dst_files = sys.argv[2]

        working_directory    = os.getenv('PWD')
        
        if not packer_src_files:
            packer_src_files = os.getenv('PACKER_FILES_SRC')
        if not packer_dst_files:
            packer_dst_files = os.getenv('PACKER_FILES_DEST')

        print('Applying arguments:')
        print(f'PWD:               {working_directory}')
        print(f'PACKER_FILES_SRC:  {packer_src_files}')
        print(f'PACKER_FILES_DEST: {packer_dst_files}')

        if not working_directory.endswith(os.path.sep):
            working_directory = f'{working_directory}{os.path.sep}'

        pack(working_directory, packer_src_files, packer_dst_files)
    except Exception as ex:
        logger.fatal('Exception in tool', exc_info=ex)

if __name__ == '__main__':
    main()