# -*- coding: utf-8 -*-
#
# Addon Publish Tool
#
# This tool publishes the local dev folder as a proper
# addon to your kodi test environment.
# 
# Needs the following OS vars (.env)
#
# ADDON_NAME=plugin.program.akl
# ADDON_SRCPATHS=**/*.py:**/*.md:**/*.xml:media/**/*.*:!tests/**/*.*:!build/**/*.*
# ADDON_KODI_DIR=<kodi addons dir>
#
# ADDON_SRCPATHS is a path separator list of glob patterns of files to deploy.
# 

# --- Python standard library ---
from __future__ import unicode_literals
from __future__ import division

import os, sys
import glob
import typing
import shutil
import logging
import subprocess

logger = logging.getLogger(__name__)
def publish(addon_name: str, working_directory: str, source_paths_str:str, kodi_addon_directory:str):
    
    source_paths = source_paths_str.split(os.pathsep)
    source_files = _get_files_for_addon(working_directory, source_paths)
    dest_directory = f'{kodi_addon_directory}{addon_name}/'
    
    if not dest_directory:
        print('No destination directory set. Cancelling')
        return
    
    # cleanup old addon
    shutil.rmtree(dest_directory, ignore_errors=True)
    
    alt_sep = '/' if os.path.sep == '\\' else '\\'
    
    print(f'Copying files to {dest_directory}')
    for source_file in source_files:
        dest_file = source_file.replace(working_directory, dest_directory)        
        dest_file = dest_file.replace(alt_sep, os.path.sep)
        source_file = source_file.replace(alt_sep, os.path.sep)
        
        print(f'Source: {source_file} to des: {dest_file}')
        
        parent_dir = os.path.dirname(dest_file)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
                    
        shutil.copy(source_file, dest_file)

def _get_files_for_addon(working_directory:str, source_paths:typing.List[str]) -> typing.List[str]:     
    source_files = []
    for source_path in source_paths:
        if source_path.startswith('!'): continue
        glob_expression = working_directory + source_path
        matching_files = glob.glob(glob_expression, recursive=True)
        source_files.extend(matching_files)
    
    # remove excluded files    
    for source_path in source_paths:
        if not source_path.startswith('!'): continue
        glob_expression = working_directory + source_path[1:]
        for match in glob.iglob(glob_expression, recursive=True):
            if match in source_files: source_files.remove(match)
    
    for source_file in source_files:
        if not os.path.isfile(source_file):
            source_files.remove(source_file)
    
    return source_files

def main():
    try:
        working_directory    = os.getenv('PWD')
        addon_name           = os.getenv('ADDON_NAME')

        source_paths_str     = os.getenv('ADDON_SRCPATHS')
        kodi_addon_directory = os.getenv('ADDON_KODI_DIR')
        
        if not working_directory.endswith(os.path.sep):
            working_directory = f'{working_directory}{os.path.sep}'

        print('Applying arguments:')
        print(f'PWD:            {working_directory}')
        print(f'ADDON_NAME:     {addon_name}')
        print(f'ADDON_SRCPATHS: {source_paths_str}')
        print(f'ADDON_KODI_DIR: {kodi_addon_directory}')

        publish(addon_name, working_directory, source_paths_str, kodi_addon_directory)
    except Exception as ex:
        logger.fatal('Exception in tool', exc_info=ex)

if __name__ == '__main__':
    main()