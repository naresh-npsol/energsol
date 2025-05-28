import os
import re

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file_content(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def extract_header_footer(content):
    # Extract header
    header_pattern = r'<!-- start header -->(.*?)<!-- end header -->'
    header_match = re.search(header_pattern, content, re.DOTALL)
    header = header_match.group(0) if header_match else None

    # Extract footer
    footer_pattern = r'<!-- start footer -->(.*?)<!-- end footer -->'
    footer_match = re.search(footer_pattern, content, re.DOTALL)
    footer = footer_match.group(0) if footer_match else None

    return header, footer

def remove_search_icon(header):
    # Remove the search icon section
    search_pattern = r'<div class="header-search-icon icon">.*?</div>'
    return re.sub(search_pattern, '', header, flags=re.DOTALL)

def update_copyright_year(footer):
    # Update copyright year to 2025
    copyright_pattern = r'&copy; \d{4}'
    return re.sub(copyright_pattern, '&copy; 2025', footer)

def update_file(file_path, new_header, new_footer):
    content = read_file_content(file_path)
    
    # Extract existing header and footer
    header_pattern = r'<!-- start header -->(.*?)<!-- end header -->'
    footer_pattern = r'<!-- start footer -->(.*?)<!-- end footer -->'
    
    # Replace header
    content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
    
    # Replace footer
    content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL)
    
    write_file_content(file_path, content)

def main():
    # Read index.html
    index_content = read_file_content('index.html')
    
    # Extract header and footer
    header, footer = extract_header_footer(index_content)
    
    # Remove search icon from header
    header = remove_search_icon(header)
    
    # Update copyright year in footer
    footer = update_copyright_year(footer)
    
    # Get all HTML files
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
    
    # Update each file
    for file in html_files:
        print(f"Updating {file}...")
        update_file(file, header, footer)
        print(f"Updated {file} successfully!")

if __name__ == "__main__":
    main() 