import requests
import codecs
f = codecs.open(u'post.xml', u'r', u'utf-8')
content = u''.join(f.readlines())
f.close()
res = requests.post(u'http://breadmum.com/', data=content.encode(u'utf-8'))
print(res.text)