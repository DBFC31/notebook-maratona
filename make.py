import os
import pypandoc
import pdfkit

notebook = "notebook.md"
text = ""

# Diretório atual
current_dir = os.getcwd()

# Listar arquivos que terminam com .cpp
algoritimos_path = os.path.join(current_dir, "algoritimos")
categories = [f for f in os.listdir(algoritimos_path) if os.path.isdir(os.path.join(algoritimos_path, f))]
categories.sort()

for category in categories:
    category_path = os.path.join(algoritimos_path, category)
    cpp_files = [f for f in os.listdir(category_path) if f.endswith('.cpp')]
    cpp_files.sort()
    text += f"\n## {category}\n"
    for file in cpp_files:
        text += f"\n### {file.split('.')[0]}\n\n"
        text += f"```cpp\n"
        with open(os.path.join(algoritimos_path, category, file), 'r') as f:
            lines = f.readlines()[2:]  # Ignorar cabecalho
            text += ''.join(lines)
        text += f"\n```\n\n"
        text += '<div style="page-break-after: always;"></div>\n'

file = "formulas.md"
with open(file, 'r') as f:
    text += f.read()

with open(notebook, 'w') as f:
    f.write(text)

# Check if the specified files exist
css_path = "style/adwaita.css"
lua_path = "style/relative_to_absolute.lua"

# Use a simpler approach with proper argument formatting
args = ["--embed-resources",
        "--standalone",
        "-s", "--webtex",
        "--metadata", "title=Notebook",
        "--wrap=none"]

# Add CSS and Lua filter only if they exist
if os.path.exists(css_path):
    args.extend(["--css", css_path])
if os.path.exists(lua_path):
    args.extend(["--lua-filter", lua_path])

try:
    pypandoc.convert_text(text, "html5", "markdown", extra_args=args, outputfile="notebook.html")
    print("HTML conversion successful!")
except Exception as e:
    print(f"Error during conversion: {e}")
# Convert the notebook.html to PDF

# Generate PDF
pdf_path = 'notebook.pdf'

try:
    pdfkit.from_file("notebook.html", pdf_path)
    print(f"PDF generated and saved at {pdf_path}")
except Exception as e:
    print(f"PDF generation failed: {e}")

# Clean up the intermediate HTML file
try:
    os.remove("notebook.html")
    print("Intermediate HTML file removed.")
except Exception as e:  
    print(f"Error removing intermediate HTML file: {e}")