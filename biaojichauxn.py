#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：YFWang time:2022/3/2
import requests
import ddddocr
import random

def result_replace(p):
    p = p
    p = p.replace("{\"data\":\"{\\\"msg\\\":\\\"成功\\\",\\\"lookorderday\\\":-1,\\\"data\\\":[{", "")
    p = p.replace(
        "}],\\\"distributiontype\\\":5,\\\"openappeal\\\":-1,\\\"appidtrue\\\":\\\"\\\",\\\"status\\\":200}\",\"msg\":\"成功\",\"status\":200}",
        "")
    p = p.replace("\\\"", "")
    p = p.replace("{", "")
    p = p.replace("}", "")
    p = p.replace(",", "\n")
    p = p.replace("coderesult", "标记内容")
    p = p.replace("codefrom", "标记平台")
    p = p.replace("code:", "手机号:")
    p = p.replace("codeurl:", "标记来源地址：")
    return p

url = "https://www.opene164.org.cn/mark/query/captcha.html?1646120488721"

payload = 'cookie=JSESSIONID%3DC08FD052705166A9405D505615AD83BA&Host=www.opene164.org.cn&Origin=http%3A%2F%2Fwww.opene164.org.cn&Referer=http%3A%2F%2Fwww.opene164.org.cn%2Fmark%2Findex.html&User-Agent=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_12_6)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F73.0.3683.75%20Safari%2F537.36%0AX-Requested-With%3A%20XMLHttpRequest'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSESSIONID=E9B41573F6D91FD5EC2E7623A76DD014'
}
o = 1
i = 0
print("该工具有一定几率识别验证码失败，如果失败请多次尝试！退出请输入--quit")
procxy = [
    {'http':'HTTP://218.244.147.59:3128'
    },
    {'http':'HTTP://221.5.80.66:3128'
    },
    {'http':'HTTP://183.247.152.98:53281'
    },
    {'http':'HTTP://47.92.113.71:80'
    },
    {'http':'HTTP://183.247.152.98:53281'
    },
    {'http':'HTTP://221.5.80.66:3128'
    },
    {'http':'HTTP://218.7.171.91:3128'
    }
    ]

while o >= 1:
    http = random.choice(procxy)
    print(http)
    phone = input("请输入你要查询标记的手机号:")
    if phone != "quit":
        # 获取响应图片内容
        image = requests.get(url, headers=headers, data=payload).content
        # 保存到本地
        with open(str(i) + "image.jpg", "wb") as f:
            f.write(image)
        with open(str(i) + "image.jpg", 'rb') as x:
            content_captcha = x.read()
        # 通过ddddocr识别验证码
        ocr = ddddocr.DdddOcr()
        code = ocr.classification(content_captcha)
        # print(response.text)
        print (code)
        # phone = 17114311449
        print(phone)
        url_phone = "https://www.opene164.org.cn/mark/data.do?phone=%s&captcha=%s" % (phone, code)
        print(url_phone)
        r = requests.post(url_phone, proxies=http, headers=headers, data=payload, timeout=1)
        # r = requests.post(url_phone, headers=headers, data=payload, timeout=1)
        print(result_replace(r.text))
        # print(r.headers)
    else:
        o = o - 1
# os.system("pause")
