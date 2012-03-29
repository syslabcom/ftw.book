from zope.publisher.browser import BrowserView
from plone.app.layout.navigation.navtree import buildFolderTree
from ftw.book.browser.toc_tree import BookTocTree
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class BookView(BrowserView):

    template = ViewPageTemplateFile('book_view.pt')

    def renderindex(self):
        return self.context.restrictedTraverse('@@index_view')()

