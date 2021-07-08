from bs4 import BeautifulSoup


class PyMail:
    def __init__(self, html_input):
        self.file = BeautifulSoup(html_input, 'html.parser')

    def template(self, template_name, classes, html_id=None, content=None):
        # open corresponding template
        with open(f'core/templates/{template_name}.html') as fp:
            soup = BeautifulSoup(fp, 'html.parser')

        # create classes
        classes = ' '.join(classes)

        # get element of template
        template = soup.contents[0]

        # set classes and id
        template['class'] = classes
        if id:
            template['id'] = html_id

        # render content
        if content:
            template = str(template).replace('{{ contents }}', str(content))

        return BeautifulSoup(template, 'html.parser') #test

    def transform(self, html_tag, class_regex=None, extra_classes=None, html_id=None):
        tags = self.file.find_all(html_tag)
        for tag in tags:
            content = tag.decode_contents()
            if extra_classes:
                classes = tag['class'] + extra_classes
            else:
                classes = tag['class']
            tag.replace_with(self.template(html_tag, classes=classes, html_id=html_id, content=content))
        return self.file


