//На основе 3 лабы
from jinja2 import Environment, FileSystemLoader
from webob import Request, Response

css = []
js = []
assets = [
	'app.js',
	'react.js',
	'leaflet.js',
	'D3.js',
	'moment.js',
	'math.js',
	'main.css',
	'bootstrap.css',
	'normalize.css',
]
for item in assets:
	itemsplited = item.split('.')
	if itemsplited[1] == 'css':
	    css.append(item)
	elif itemsplited[1] == 'js':
	    js.append(item)

class WsgiTopBottomMiddleware(object):
	def __init__(self, app):
		self.app = app

	def __call__(self, environ, start_response):
		response = self.app(environ, start_response).decode()
		if response.find('<body>' and '<head>') > -1:   #!!!
	    		head, headstart = response.split('<head>')
	    		data1, headend = headstart.split('</head>')
	    		body, bodystart = response.split('<body>')
	    		data2, bodyend = bodystart.split('</body>')
	    		yield (head + data + bodyend).encode()
		else:
	    		yield (response).encode()


def app(environ, start_response):
    response_code = '200 OK'
    response_type = ('Content-Type', 'text/HTML')
    start_response(response_code, [response_type])
    return ''''''


app = WsgiTopBottomMiddleware(app)

req2 = Request.blank('/index.html')

env = Environment(loader=FileSystemLoader('.'))
template1 = env.get_template('index.html')

print(template1.render(javascripts=js, styles=css))
print(req2.get_response(app))
