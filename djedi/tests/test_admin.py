from django.core.urlresolvers import reverse
from djedi.utils.encoding import smart_str
from djedi.tests.base import ClientTest


class PanelTest(ClientTest):

    def test_embed(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertIn(b'Djedi Test', response.content)
        self.assertIn(b'window.DJEDI_NODES', response.content)

    def test_cms(self):
        url = reverse('admin:djedi:cms')
        response = self.client.get(url)
        self.assertIn(b'<title>djedi cms</title>', response.content)

    def test_django_admin(self):
        # Patch django admin index
        from django.contrib.admin.templatetags.log import AdminLogNode
        _render = AdminLogNode.render
        AdminLogNode.render = lambda x, y: None

        url = reverse('admin:index')
        response = self.client.get(url)
        link = ''.join(('<a href="', reverse('admin:djedi:cms'), '">CMS</a>'))
        self.assertIn(smart_str(link), response.content)

        # Rollback patch
        AdminLogNode.render = _render
