# Ballistica Network Proxy

**Languages: [中文](#中文版本) | [English](#English-Version)**

# English Version

The Ballistica Proxy is a tool designed to allow Chinese users to access Ballistica servers through a proxy.

## Project Description

The Ballistica Proxy can be deployed on a server, enabling Chinese users to connect to this server as a proxy to access Ballistica servers, thus providing a better user experience.

## Installation Instructions

1. Clone this repository to your local computer.

2. Run the `listen.py` script to start request listening.

## Example

Site Example: [ba.nappig.com](https://ba.nappig.com)

This site is accelerated using Tencent Cloud's next-generation edge computing CDN, has obtained government filing, and is a legal and compliant website with filing number: SuICP备2023020191.

## Additional Features

The project is optimized for Ballistica Website and now supports automatic translation from English to Chinese, greatly improving the experience for Chinese users!
Due to the lack of support for Google services in mainland China, including Chrome and Google Translate, most browsers used on Chinese mainland smartphones and computers are the built-in system browsers. The user experience varies widely, with browser translators often producing incorrect or conflicting translations, or translating the meaning of words into something else, making it difficult to use (personal experience, really frustrating), and some browsers may not even have translation capabilities!

## Contribution Guidelines

Thank you for your interest, but all development work is done solely by Medic.

## Copyright Information

This project is for reference and learning purposes only. It is strictly prohibited to set up this service and provide it to others without explicit permission from Ballistica developers.

## Contact Information

- Discord: "inkmedic" or "super_susu"
- Email: me@Gura.top

## Additional Information
After conducting research, we have identified the reasons for network congestion, as outlined in the report below:

1. `ballistica.net` and `legacy.ballistica.net` both use CDN services provided by Google Cloud, which is not active in mainland China.
2. Through domain name resolution, it was found that only four IPv4 records can be resolved within mainland China, which are `216.239.32/34/36/38.21`.
3. However, ping tests revealed that some addresses are not reachable and have been blocked (by the Great Firewall of China), especially `216.239.36.21`. A DNS resolves to this IP 70% of the time, but this IP has been blocked! (Even though BombSquad provides an alternative address (appspot.com), the Great Firewall of China (GFW) blocked this address a long time ago, so it is ineffective.)
4. As per player feedback, the "Use mobile data 4G/5G" method has been preliminarily confirmed. The principle is that mobile data provides IPv6 addresses, and Ballistica.net supports IPv6 access. Currently, the Chinese Great Firewall has not yet blocked these IPv6 addresses, allowing for smooth access.
5. If your Wi-Fi/broadband supports IPv6, you will not be affected by the firewall. However, the current adoption rate of IPv6 in China is still relatively low.

# Conclusion
1. Most of Ballistica Servers IP have been blocked by the Chinese Great Firewall.
2. IPv6 remains unaffected by firewall interference (Mobile Data 4G/5G comes with IPv6.)

---

# 中文版本

# Ballistica-代理器

Ballistica代理器是一个用于将国内用户代理访问Ballistica服务器的工具。

## 项目描述

Ballistica代理器可以部署到一台服务器，使中国用户能够通过连接该服务器代理访问Ballistica服务器，从而获得更好的访问体验。
本项目基于Python Request 和 Flask

## 安装说明

1. 克隆此存储库到本地计算机。

2. 运行 `listen.py` 脚本，以开始请求监听。

## 示例

站点示例: [ba.nappig.com](http://ba.nappig.com)

此站点采用腾讯云新一代边缘计算CDN进行加速访问，已获得政府备案，是合法合规网站，备案号：苏ICP备2023020191

## 特殊功能
本项目支持将ballistica的网页翻译成中文！
毕竟国内浏览器的臃肿和垃圾，谁用谁知道！

## 贡献指南

感谢您的支持，但所有开发工作由Medic一人完成。捐赠+QQ1503366755

## 版权信息

本项目仅供参考和学习之用。未经Ballistica游戏官方允许，严禁私自搭建此服务且提供给他人使用，除非事先获得明确的许可。但是你可以自己用。

主要是怕有不法分子使用此方法窃取玩家信息例如密码

## 联系方式

- Discord: "inkmedic" 或 "super_susu"
- 电子邮箱: me@Gura.top
- QQ：1503366755

## 额外信息
目前经过研究，已经掌握网络不畅通的原因，研究报告如下：

1.`ballistica.net`和 `legacy.ballistica.net`均使用Google Cloud所提供的CDN服务，但Google Cloud并未在中国大陆开展相关业务；

2.我们通过域名解析得知在中国大陆内只能解析到四个IPv4记录，为`216.239.32/34/36/38.21`；

3.但ping测试后发现部分地址ping不通，已经被墙（被中国GFW防火墙拦截），尤其是`216.239.36.21`，DNS有70%会解析为此IP，但此IP已经被墙！

4.根据玩家反馈所言，“打开手机流量就行”的方法得到初步印证。其原理是因为手机流量会提供IPv6地址，而ballistica.net支持IPv6访问，且目前中国GFW防火墙尚未对这些IPv6地址进行封锁，因此可以流畅访问；

5.如果WiFi/宽带支持IPv6，那么您也不会受到防火墙的干扰。但目前中国IPv6普及率还是相对较低的啦...

### 结论
1.ballistica服务器的大部分地址已经被中国GFW防火墙屏蔽！

2.IPv6则不受到防火墙屏蔽的干扰（手机流量自带IPv6）!
