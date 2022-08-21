#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Rekord
# @Date: 2022-08-20


import mistune
import sys
import datetime
import time
import os


sourcePath = sys.argv[1]
fileName = sourcePath[sourcePath.rfind("/") + 1:len(sourcePath) - 2] + 'html'
# destinationPath = 'html' + sourcePath[sourcePath.find("/"):sourcePath.rfind("/") + 1] + fileName
destinationPath = sourcePath[sourcePath.find("/") + 1:sourcePath.rfind("/") + 1] + fileName

with open(sourcePath, 'r', encoding='utf-8', newline='') as file:
    mdContent = file.read()

# escape "-->"
mdContent = mdContent.replace("-->", "->")

user = "Rekord"
generateTime = str(datetime.datetime.today() + datetime.timedelta(hours=8-int(time.strftime('%z')[0:3])))
head = """<!-- Markdown Source -->
<!--
""" + mdContent + """
-->


<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
    <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>""" + fileName + """</title>
	<link rel="stylesheet" href="css/github-markdown-light.css">
	<link rel="stylesheet" href="css/custom.css">
	<script src="js/custom.js"></script>
	<link rel="icon" href="https://cdn.sxrekord.com/blog/favicon.ico">
	<style>
		.markdown-body {
			box-sizing: border-box;
			min-width: 200px;
			max-width: 980px;
			margin: 0 auto;
			padding: 45px;
		}

		@media (max-width: 767px) {
			.markdown-body {
				padding: 15px;
			}
		}

		.mode {
			position: fixed;
			width: 40px;
			height: 40px;
			border-radius: 50%;
			top: 20px;
			left: 20px;
			background-size: cover;
			background-image: url("images/sun.png");
			background-color: white;
			background-repeat: no-repeat;
		}
	</style>
</head>

<body>
	<div class="mode"></div>
	<article class="markdown-body">
"""

foot = """</article>
        <footer>
<div class="div_foot">
        <b>""" + fileName + '</b> - Generated on <b>' + generateTime[:len(generateTime) - 7] + '</b> by <b>' + user + """</b> using <a href="https://github.com/lepture/mistune">mistune</a> and <a href="https://github.com/sindresorhus/github-markdown-css">github-markdown-css</a>. Source is embedded.
    </div>
    </footer>
    </body>
</html>
"""

# if not os.path.exists(destinationPath[:destinationPath.rfind('/')]):
#     os.makedirs(destinationPath[:destinationPath.rfind('/')])

with open(destinationPath, 'w', encoding='utf-8', newline='') as file:
    file.write(head + mistune.html(mdContent) + foot)