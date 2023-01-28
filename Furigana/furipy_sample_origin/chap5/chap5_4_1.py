from pathlib import Path
rfile = Path('sample.txt')
rtext = rfile.read_text(encoding='utf-8')
print(rtext)
