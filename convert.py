import os
import markdown

# Directory where your Markdown files are stored
input_folder = "_posts"
output_folder = "html_pages"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through each Markdown file
for filename in os.listdir(input_folder):
    if filename.endswith(".md"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".md", ".html"))

        # Read the Markdown file
        with open(input_path, "r", encoding="utf-8") as md_file:
            md_content = md_file.read()

        # Convert to HTML
        html_content = markdown.markdown(md_content)

        # Save the HTML file
        with open(output_path, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)

        print(f"Converted {filename} to {output_path}")

print("✅ Conversion completed!")
