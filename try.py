class HTMLParser:
    def __init__(self, html):
        self.html = html.strip()
        self.index = 0

    def parse(self):
        return self._parse_element()

    def _parse_element(self):
        tag_name = self._get_next_tag()
        if not tag_name:
            return None

        children = {}
        while True:
            next_tag = self._get_next_tag(peek=True)
            if not next_tag:
                break

            if next_tag == f'/{tag_name}':
                self._get_next_tag()  # Consume closing tag
                break
            elif next_tag.startswith('/'):
                raise ValueError("Malformed HTML")
            else:
                child_name = next_tag
                child = self._parse_element()
                if child_name in children:
                    # Handle duplicate tags by converting to list
                    if not isinstance(children[child_name], list):
                        children[child_name] = [children[child_name]]
                    children[child_name].append(child)
                else:
                    children[child_name] = child

        # Check for text between tags
        text_content = self._get_text_until_next_tag()
        if text_content.strip():
            children["text_node"] = text_content.strip()

        return {tag_name: children}

    def _get_next_tag(self, peek=False):
        start_index = self.html.find('<', self.index)
        if start_index == -1:
            return None
        end_index = self.html.find('>', start_index)
        if end_index == -1:
            raise ValueError("Malformed HTML")

        tag = self.html[start_index + 1:end_index].strip()
        if not peek:
            self.index = end_index + 1
        return tag

    def _get_text_until_next_tag(self):
        start_index = self.index
        next_tag_index = self.html.find('<', start_index)
        if next_tag_index == -1:
            next_tag_index = len(self.html)
        text = self.html[start_index:next_tag_index]
        self.index = next_tag_index
        return text

    def print_tree(self, tree, indent=0):
        for key, value in tree.items():
            print('  ' * indent + f"-{key}")
            if isinstance(value, dict):
                self.print_tree(value, indent + 1)
            elif isinstance(value, list):
                for item in value:
                    self.print_tree(item, indent + 1)
            else:
                print('  ' * (indent + 1) + f"-\"{value}\"")


# Test the parser
html_code = """
<html>
    <body>
        <div>
            <h1>Joku otsikko</h1>
            <p>Jotain tekstiä</p>
        </div>
        <div>
            <p>Lisää tekstiä mutta <strong>tässä</strong> on korostus</p>
        </div>
    </body>
</html>
"""

parser = HTMLParser(html_code)
parsed_html = parser.parse()
parser.print_tree(parsed_html)