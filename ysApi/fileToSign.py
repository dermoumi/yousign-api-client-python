import os
import base64


class FileToSign(dict):
    def __init__(self, file_name, file_content_base64, visibleOptions, password, **kwargs):
        super(FileToSign, self).__init__(**kwargs)
        self["name"] = file_name
        self["content"] = file_content_base64
        self["visibleOptions"] = visibleOptions
        self["pdfPassword"] = password


class Signer(dict):
    def __init__(self, firstName, lastName, phone, mail, authenticationMode="sms", **kwargs):
        super(Signer, self).__init__(**kwargs)
        self["firstName"] = firstName
        self["lastName"] = lastName
        self["phone"] = phone
        self["mail"] = mail
        self["authenticationMode"] = authenticationMode


class VisibleOptions(dict):
    def __init__(self, visibleSignaturePage=1, isVisibleSignature=True, visibleRectangleSignature="0,39,99,0", mail="", **kwargs):
        super(VisibleOptions, self).__init__(**kwargs)
        self["visibleSignaturePage"] = visibleSignaturePage
        self["isVisibleSignature"] = isVisibleSignature
        self["visibleRectangleSignature"] = visibleRectangleSignature
        self["mail"] = mail