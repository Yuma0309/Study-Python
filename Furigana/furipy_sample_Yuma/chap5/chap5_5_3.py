from pathlib import Path
terms = {'for': 0, 'if': 0, 'else': 0}
current = Path()
for rfile in current.glob('*.py'):
    text = rfile.read_text(encoding='utf-8')
    for term in terms:
        cnt = text.count(term)
        terms[term] += cnt
print(terms)