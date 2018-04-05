from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from tutorial.security import groupfinder


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authn_policy = AuthTktAuthenticationPolicy('sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings,
                          root_factory='tutorial.models.RootFactory')

    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.include('pyramid_jinja2')
    config.include('.models')
    # チュートリアルからの変更点：ルーティングはroutes.pyに追加
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
