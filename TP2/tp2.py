import sys
import re

html = """
<!DOCTYPE html>
<html>
<head>
<title>Traducao MD</title>
</head>
<body>
"""

in_oli = False
in_uli = False

for line in sys.stdin:
    make_p = True

    line = line.strip()

    pattern = re.compile(r'^#+')
    match = pattern.match(line)
    if match:
        make_p = False
        count = len(match.group(0))
        line = f"<h{count}>{line[count+1:]}</h{count}>\n"

    line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
    line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)

    match = re.match(r'^(\d+\.|-)', line)
    if match:
        make_p = False
        if match.group(1).endswith('.'):
            if not in_oli:
                if in_uli:
                    html += "</ul>\n"
                    in_uli = False
                html += "<ol>\n"
                in_oli = True
        elif match.group(1) == '-':
            if not in_uli:
                if in_oli:
                    html += "</ol>\n"
                    in_oli = False
                html += "<ul>\n"
                in_uli = True
        line = f"<li>{line[3 if match.group(1).endswith('.') else 2:]}</li>\n"
    elif not match:
        if in_oli:
            html += "</ol>\n"
            in_oli = False
        elif in_uli:
            html += "</ul>\n"
            in_uli = False

    line = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>\n', line)
    line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)

    if make_p and line:
        line = "<p>" + line + "</p>\n"

    html += line

html += """<footer>
<p><i>Ficheiro de teste gerado, a pedido, pelo ChatGPT</i></p>
</footer>
</body>
</html>\n"""

with open('traducao.html', 'w') as file:
    file.write(html)
