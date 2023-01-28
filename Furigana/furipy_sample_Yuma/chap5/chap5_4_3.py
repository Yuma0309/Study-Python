from pathlib import Path
rfile = Path('sample.txt')
rtext = rfile.read_text(encoding='utf-8')
wtext = rtext.replace('。', '〜♪')
print(wtext)
wfile = Path('output.txt')
wfile.write_text(wtext, encoding='utf-8')