from flask import Flask, request, send_file, make_response
import requests
import translater
this_url = "http://127.0.0.1:684/"
proxy_url = "https://ballistica.net/"
app = Flask(__name__)

@app.route('/signin/static/<filename>') 
@app.route('/static/ace/<filename>') 
def ace_catch(filename):
    try:
        print("尝试使用缓存返回"+filename)
        return send_file("static/"+filename,), 200
    except:
        pass
    print(filename+"缓存不存在")
    # 获取原始请求的方法、URL、请求头和正文
    original_method = request.method
    original_url = request.url
    original_headers = dict(request.headers)
    original_body = request.get_data()
    # 构建转发请求
    if original_url == this_url:
        forward_url = proxy_url
    else:
        forward_url = proxy_url+original_url.split("/",3)[3]  #此处增加新地址
    forward_headers = original_headers
    forward_method = original_method
    # 发送转发请求
    forward_headers["Host"] = "ballistica.net"
    print("正在连接到"+forward_url)
    if forward_method == 'GET':
        response = requests.get(forward_url, headers=forward_headers)
    elif forward_method == 'POST':
        response = requests.post(forward_url, headers=forward_headers, data=original_body)
    # 打印转发请求的响应内容

    # 返回响应
    new_headers = dict(response.headers)
    news_headers = {"Content-Type":new_headers["Content-Type"]}
    print("9类型为"+str(news_headers))
    with open("static/"+filename,"wb") as file:
        file.write(response.content)
        print(filename+"写入缓存成功")
    return response.content, response.status_code, news_headers

@app.route('/static/<filename>') #请求静态文件
def catch_static(filename):
    try:
        print("尝试使用缓存返回"+filename)
        if ".css" in filename:
            raise RuntimeError
        return send_file("static/"+filename,), 200
    except:
        pass
    # 获取原始请求的方法、URL、请求头和正文
    original_method = request.method
    original_url = request.url
    original_headers = dict(request.headers)
    
    original_body = request.get_data()
    # 构建转发请求
    if original_url == this_url:
        forward_url = proxy_url
    else:
        forward_url = proxy_url+original_url.split("/",3)[3]  #此处增加新地址
    forward_headers = original_headers
    forward_method = original_method
    # 发送转发请求
    forward_headers["Host"] = "ballistica.net"
    print("正在连接到"+forward_url)
    if forward_method == 'GET':
        response = requests.get(forward_url, headers=forward_headers)
    elif forward_method == 'POST':
        response = requests.post(forward_url, headers=forward_headers, data=original_body)
    # 打印转发请求的响应内容

    # 返回响应
    new_headers = dict(response.headers)
    news_headers = {"Content-Type":new_headers["Content-Type"]}
    print("9类型为"+str(news_headers))
    with open("static/"+filename,"wb") as file:
        file.write(response.content)
        print(filename+"写入缓存成功")
    return response.content, response.status_code, news_headers
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
def catch_all(path):
    # 获取原始请求的方法、URL、请求头和正文
    original_method = request.method
    original_url = request.url
    original_headers = dict(request.headers)
    original_body = request.get_data()
    original_cookie = request.cookies
    # 构建转发请求
    if original_url == this_url:
        forward_url = proxy_url
    else:
        forward_url = proxy_url+original_url.split("/",3)[3]  
    forward_headers = original_headers
    forward_method = original_method
    forward_cookie = original_cookie
    # 发送转发请求
    forward_headers["Host"] = "ballistica.net" # 修正Host
    if "https://ballistica.net/signin" in forward_url:
        if "?display=signinprogress" in forward_url:
            forward_url = proxy_url + forward_url[36:]
        else:
            forward_url = "https://ballistica.net?signinproxy="+forward_url[-6:]
    print("正在连接到"+forward_url)
    if forward_method == 'GET':
        response = requests.get(forward_url, headers=forward_headers, cookies=forward_cookie)
    elif forward_method == 'POST':
        response = requests.post(forward_url, headers=forward_headers, data=original_body, cookies=forward_cookie)
    ###### 然后我们获取到了内容 #######
    # 修headers
    new_headers = dict(response.headers)
    news_headers = {"Content-Type":new_headers["Content-Type"]}
    # 此部分处理cookie
    cookie = dict(response.cookies)
    if "https://ballistica.net/devicesmsg" in forward_url:
        new_html = response.content
    else:
        new_html = translater.translate_html(response.text)
    res = make_response(new_html)
    for i in cookie:
        res.set_cookie(i,cookie[i])
    
    if response.status_code == 200:
        return res
    
    # 如果状态码非200，代表请求有问题，应该按照原样返回
    return response.content, response.status_code, news_headers ,

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=684)
