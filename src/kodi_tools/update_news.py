import sys, re, os, re

def update_news(addon_file:str, changelog_file:str):
    addon_xml = '' 
    changelog_part = ''

    with open(addon_file, 'r') as f:
        addon_xml = f.read()

    filename, file_extension = os.path.splitext(changelog_file)
    if file_extension == '.txt':
        changelog_part = get_changelog_from_txt_file(changelog_file)
    if file_extension == '.md':
        changelog_part = get_changelog_from_markdown_file(changelog_file)

    addon_xml = re.sub(r'<news>(.*)?</news>', f'<news>{changelog_part}</news>', addon_xml)
    with open(addon_file, 'w') as f:
        f.write(addon_xml)

def get_changelog_from_txt_file(changelog_file:str) -> str:
    with open(changelog_file, 'r') as f:
        changelog_txt = f.read()

    changelog_txt = changelog_txt.replace('\n', '[CR]')
    return changelog_txt

def get_changelog_from_markdown_file(changelog_file:str) -> str:
    with open(changelog_file, 'r') as f:
        changelog_md = f.read()

    changelog_md = re.sub(r'#+\s?(.*)?\n', r'[UPPERCASE]\1[/UPPERCASE][CR]', changelog_md)
    changelog_md = re.sub(r'>\s?(.*)?\n', r'[LIGHT]\1[/LIGHT][CR]', changelog_md)
    changelog_md = re.sub(r'\*\*([^\*\n]*)?\*\*', r'[B]\1[/B]', changelog_md)
    changelog_md = re.sub(r'\*(.*)?\*', r'[I]\1[/I]', changelog_md)
    changelog_md = re.sub(r'~~(.*)?~~', r'[COLOR red]\1[/COLOR]', changelog_md)
    changelog_md = re.sub(r'\s\s\n', r'[CR]', changelog_md)
    changelog_md = changelog_md.replace('\n\n', '[CR]')
    changelog_md = re.sub(r'\n([\*|-])', r'[CR]\1', changelog_md)
    changelog_md = changelog_md.replace('\w\n\w', '[CR]')

    changelog_md = changelog_md.replace('\n', '')
    return changelog_md

def main():
    addon_file = sys.argv[1]
    changelog_file = sys.argv[2]

    update_news(addon_file, changelog_file)

if __name__ == '__main__':
    main()