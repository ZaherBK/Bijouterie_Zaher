import os, re
path = 'd:/VbBirka/Bijouterie_Zaher/app/main.py'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'templates\.TemplateResponse\(\s*([\'\"][^\'\"]+[\'\"])\s*,\s*'

new_text = re.sub(pattern, r'templates.TemplateResponse(request=request, name=\1, context=', text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Done replacing.')
