from pathlib import Path
current = Path()
for rfile in current.glob('*.py'):
    text = rfile.read_text(encoding='utf-8')
    cnt = text.count('for')
    print(rfile, cnt)