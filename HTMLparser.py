def parse_html(html):
    """Parse HTML string into a nested dictionary while preserving order."""
    html = html.strip()
    position = 0

    def parse(position):
        content = []
        while position < len(html):
            if html[position] == '<':
                if html[position + 1] == '/':  # Closing tag
                    position = html.find('>', position) + 1
                    return content, position
                else:  # Opening tag
                    tag_name, position = get_tag_name(position)
                    child_content, position = parse(position)
                    content.append({tag_name: child_content})
            else:
                text, position = get_text_content(position)
                if text:
                    content.append({"text_node": text})  # Add text to the list
        return content, position

    def get_tag_name(position):
        start = position + 1
        end = html.find('>', start)
        tag_name = html[start:end].strip()
        return tag_name, end + 1

    def get_text_content(position):
        start = position
        end = html.find('<', start)
        text = html[start:end].strip()
        return text, end

    parsed_content, _ = parse(position)
    return {"html": parsed_content}

def print_hierarchy(content, depth=0):
    """Print the hierarchical structure of the parsed HTML."""
    if isinstance(content, list):
        for element in content:
            for key, value in element.items():
                if key == "text_node":  # Print text directly
                    print('  ' * depth + f'-"{value}"')
                else:  # Print tag name and recurse for children
                    print('  ' * depth + f"-{key}")
                    print_hierarchy(value, depth + 1)
    elif isinstance(content, dict):  # Handle top-level dictionary
        for key, value in content.items():
            print('  ' * depth + f"-{key}")
            print_hierarchy(value, depth + 1)

# Input HTML
html_code = open("index.html", encoding="UTF-8" )
html_code = html_code.read()
# Parse and display the result
parsed_html = parse_html(html_code)
print_hierarchy(parsed_html)