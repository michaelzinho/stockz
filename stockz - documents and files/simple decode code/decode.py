import urllib.parse

code = 'code_here'
decoded_code = urllib.parse.unquote(code)
print('code:', decoded_code)