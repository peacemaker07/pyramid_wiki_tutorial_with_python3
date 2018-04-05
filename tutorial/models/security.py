"""
チュートリアルから変更したところ

・models.pyがないので、本ファイルを新規に作成しclass追加
"""

from pyramid.security import (
    Allow,
    Everyone,
)


class RootFactory(object):
    __acl__ = [(Allow, Everyone, 'view'), (Allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass
