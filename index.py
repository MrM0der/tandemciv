import base64
import gzip
import json


def unciv_save(savename, mode='r', preview=False, savedict=None):
    def unciv_decode(text: str):
        text = base64.b64decode(text)
        gzip_text = gzip.decompress(text)
        result = str(gzip_text, "utf-8")
        return result

    def unciv_encode(text: str):
        text = text.encode(encoding="utf-8")
        gzip_text = gzip.compress(text)
        result = base64.b64encode(gzip_text)
        return str(result, encoding='utf-8')

    def read(file: str):
        f = open(file, 'r')
        text = f.read()
        f.close()
        return text

    def write(file: str, text: str):
        f = open(file, 'w')
        f.write(text)
        f.close()

    def save2dict(save: str):
        return json.loads(save)

    def dict2save(dict: dict):
        return json.dumps(dict)
    if mode == "r":
        if preview == True:
            save_read = read(f"files/{savename}_Preview")
        else:
            save_read = read(f"files/{savename}")
        save_decode = unciv_decode(save_read)
        save = save2dict(save_decode)
        return save
    if mode == "w":
        savetext = dict2save(savedict)
        saveencode = unciv_encode(savetext)
        if preview == True:
            write(f"files/{savename}_Preview", saveencode)
        else:
            write(f"files/{savename}", saveencode)


def autowriter(savename, savedict):
    for i in [True, False]:
        print(i)


def initializer():
    pass


save_preview = unciv_save(
    "1ce48a9f-3b8c-403f-8681-73699a2da954", preview=True)


for i in save_preview:
    print(i)
print(save_preview)
