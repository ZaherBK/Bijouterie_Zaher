import urllib.request
import re

url = 'https://raw.githubusercontent.com/ZaherBK/Bijouterie_Zaher/main/app/main.py'
print('Fetching URL:', url)
try:
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    print('Fetched Length:', len(text))
    
    # Do replacements
    pattern = r'templates\.TemplateResponse\(\s*([\'\"][^\'\"]+[\'\"])\s*,\s*'
    new_text = re.sub(pattern, r'templates.TemplateResponse(request=request, name=\1, context=', text)
    print('Replaced Length:', len(new_text))
    
    with open('d:/VbBirka/Bijouterie_Zaher/github_main.py', 'w', encoding='utf-8') as f:
        f.write(new_text)
        
    print('Done.')
except Exception as e:
    print('Error:', e)
