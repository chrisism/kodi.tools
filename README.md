# kodi.tools
Collection of python tools for building Kodi addons

[![kodi.tools package in akl_libs feed in Azure Artifacts](https://feeds.dev.azure.com/jnpro/5e7cdfe4-c213-4214-8723-2fd88a4f7525/_apis/public/Packaging/Feeds/0097d2bd-739f-41d5-a1b6-bed6a76a2929/Packages/6e328cc5-ca01-4b69-8ce9-3a2ab5befec7/Badge)](https://dev.azure.com/jnpro/AKL/_packaging?_a=package&feed=0097d2bd-739f-41d5-a1b6-bed6a76a2929&package=6e328cc5-ca01-4b69-8ce9-3a2ab5befec7&preferRelease=true)

## Commands:
The following commands are supported.

### Publishing addon to local kodi
```bash
publish_addon
```
Command to publish your development directory addon to the actual addons directory in kodi.
When invoking this tool you need to have the following environment variables set:
- PWD (working directory, linux automatically takes current dir. Needs to be your dev addon dir)
- ADDON_NAME (addon id as in addon.xml)
- ADDON_KODI_DIR (location of your kodi addons directory)
- ADDON_SRCPATHS (glob pattern of files to copy)

### Package images in your addon
```bash
pack_addon
```
- PWD (working directory, linux automatically takes current dir. Needs to be your dev addon dir)
- PACKER_FILES_SRC
- PACKER_FILES_DEST

### Updates the news element in addon xml
```bash
update_addon__news
```
Updates the news element in the addon xml with a changelog txt file or markdown file.  
Will try to change the markdown syntax to kodi specific markup.

### Merge addon xml into addons xml
```bash
merge_addon_xml
```