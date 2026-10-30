"""Traduz o gráfico gerado e só o publica no README quando estiver disponível."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

source = Path("profile-3d-contrib/profile-night-green.svg")
if not source.is_file():
    raise SystemExit("O gráfico 3D não foi gerado.")
translations = {
    "Commit": "Commits",
    "Issue": "Tarefas",
    "PullReq": "PRs",
    "Review": "Revisões",
    "Repo": "Repos",
    "other": "outras",
    "contributions": "contribuições",
}
svg = re.sub(r">([^<>]+)<", lambda m: ">" + translations.get(m.group(1), m.group(1)) + "<", source.read_text(encoding="utf-8"))
ET.fromstring(svg)
Path("assets/contribuicoes-3d.svg").write_text(svg, encoding="utf-8")
readme = Path("README.md")
marker = "<!-- CONTRIBUICOES_3D -->"
image = '<p align="center">\n  <img src="./assets/contribuicoes-3d.svg" width="100%" alt="Gráfico 3D das contribuições de Emerson Victor no GitHub" />\n</p>'
content = readme.read_text(encoding="utf-8")
if marker in content:
    readme.write_text(content.replace(marker, image), encoding="utf-8")
