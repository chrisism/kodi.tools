import sys, re

def update_news(addon_file:str, changelog_file:str):
    addon_xml = '' 
    changelog_txt = ''

    with open(addon_file, 'r') as f:
        addon_xml = f.read()
    with open(changelog_file, 'r') as f:
        changelog_txt = f.read()

    changelog_txt = changelog_txt.replace('\n', '[CR]')
    addon_xml = re.sub(r'<news>(.*)?</news>', f'<news>{changelog_txt}</news>', addon_xml)
    with open(addon_file, 'w') as f:
        f.write(addon_xml)

def main():
    addon_file = sys.argv[1]
    changelog_file = sys.argv[2]

    update_news(addon_file, changelog_file)

if __name__ == '__main__':
    main()