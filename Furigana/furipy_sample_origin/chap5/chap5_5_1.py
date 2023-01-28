from pathlib import Path
current = Path()
for rfile in current.glob('*.py'):
    print(rfile)
