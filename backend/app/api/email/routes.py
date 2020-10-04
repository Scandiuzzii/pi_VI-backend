from . import bp
from . import mail as m
from . import queue
from flask import jsonify,request
from app import cross_origin

@bp.route('/',methods=['POST'])
@cross_origin()
def enviar_email():
    data = request.get_json()
    if data['cadastro'] ==1:
        subject = 'Cadastro Efetuado com sucesso'
        body = f"""Seu cadastro foi efetuado com sucesso
            login:{data['email']}
            senha:{data['senha']}

            Pedimos por gentileza para trocar sua senha no seu primeiro acesso.
            Ir na are de perfil para trocar sua senha
            link: www.uol.com.br
        """
    elif data['cadastro'] == 0:
        subject = 'Feedback aula'
        body = """
            Segue link do Formulario para nos contar como estava a sala apos a aula
            link: www.uol.com.br
        """
    elif data['cadastro'] == 2:
        subject = 'Alteração de senha'
        body = f"""
            Foi solicitado uma alteração de senha,
            login:{data['email']}
            senha:{data['senha_nova']}
            Pedimos por gentileza para trocar sua senha no seu primeiro acesso.
            Ir na are de perfil para trocar sua senha
        """
    d = m.Mail(data['email'],body,subject)
    d.enviar()
    queue.queue(d.email,d.msg)
    return jsonify({
        'message':'adsasda'
    }),200
    