class Message:
    def __init__(self):
        pass

    def msg_email(self, email, token):
        msg                 = {}
        msg['header']       = "get_client_key"
        body                = {}
        body['token']       = token
        body['email']       = email
        msg['body']         = body

        return msg

    def msg_send_key(self, key, token):
        msg                 = {}
        msg['header']       = "get_client_key"
        body                = {}
        body['key']         = key
        body['token']       = token
        msg['body']         = body

        return msg

    def msg_get_client_key(self, email, token):
        msg                 = {}
        msg['header']       = "get_client_key"
        body                = {}
        body['token']       = token
        body['email']       = email
        msg['body']         = body

        return msg

    def msg_authentication(self, email, password):
        msg                 = {}
        msg['header']       = "authentication"
        body                = {}
        body['email']       = email
        body['password']    = password
        msg['body']         = body

        return msg
