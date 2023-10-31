import json
from bs4 import BeautifulSoup
from bs4 import NavigableString

def translate_html(html_str):
    # 读取JSON翻译文件
    with open("cn.json", 'r', encoding='utf-8') as file:
        translations = json.load(file)

    # 使用BeautifulSoup解析HTML字符串
    soup = BeautifulSoup(html_str, 'html.parser')

    # 遍历HTML中的文本节点，并进行翻译
    for element in soup.find_all(text=True):
        text = element.strip()
        if text in translations:
            element.replace_with(translations[text])
        elif "Account not found for" in text:
            element.replace_with("未找到此账户！请检查邮箱是否正确")
    for input_element in soup.find_all('input'):
        # 检查输入元素的类型是否为"text"或"password"等，并且它具有"value"属性
        if input_element.get('type') in ['text', 'password','submit'] and input_element.has_attr('value'):
            original_value = input_element['value']
            if original_value in translations:
                input_element['value'] = translations[original_value]
            elif "Link Login to" in original_value and len(original_value) < 20:
                input_element['value'] = "确定关联"
    for input_element in soup.find_all('input'):
        if input_element.has_attr('value'):
            if input_element['type'] == "hidden":
                continue
            original_value = input_element['value']
            if original_value in translations:
                input_element['value'] = translations[original_value]
        if input_element.has_attr('placeholder'):
            original_value = input_element['placeholder']
            if input_element['type'] == "hidden":
               continue
            if original_value in translations:
                input_element['placeholder'] = translations[original_value]

    # 在<body>的尾部插入特定的HTML代码
    body = soup.find_all('div',class_ = "faded")
    if body:
        new_html = """<div class="faded" style="text-align:center"><br/>本页面由<a href="https://www.bombsquad.cn"><img src="https://cncdn.nappig.com/pic/bomblogo.png" alt="炸队资源站" width="10" height="10">炸队资源站</a>代理<br/>这是一个公益性网站，如果出现任何问题，请及时联系我们，我们期待你的反馈！</div>"""  # 在这里替换为你要插入的内容

        new_tag = BeautifulSoup(new_html, 'html.parser')

    # 插入新标签到<div>之前
        body[-1].insert_before(new_tag)

    # 返回修改后的HTML字符串
    return str(soup)
