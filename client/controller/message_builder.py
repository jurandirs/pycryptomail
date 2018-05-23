class MessageBuilder:
    def __init__(self):
        self.message = {}

    def set_from_email(self, email):
        self.message['from'] = email
        return self

    def set_cc_emails(self, emails):
        self.message['cc'] = emails
        return self

    def set_attachaments(self, attachments):
        self.message['attachments'] = attachments
        return self

    def set_subject(self, subject):
        self.message['subject'] = subject
        return self

    def set_msg(self, message):
        self.message['message'] = message
        return self

    def set_priority(self, priority):
        self.message['priority'] = priority
        return self

    def build(self):
        return self.message
