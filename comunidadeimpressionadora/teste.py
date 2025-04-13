from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario, Post
from comunidadeimpressionadora.routes import usuarios

# from comunidadeimpressionadora.routes import usuarios

# with app.app_context():
#    database.create_all()

# with app.app_context():
#     usuarios = Usuario(username="jailson", email= "jkçl@gmail.com", senha= "123456")
#     database.session.add(usuarios)
#     database.session.commit()

with app.app_context():
    meus_usuarios = Usuario.query.all()
    print(meus_usuarios)
    # primeiro = Usuario.query.first()
    # print(primeiro.username)
    usuario_teste3 = Usuario.query.filter_by(username="jailson2").first()
    print(usuario_teste3.email)

