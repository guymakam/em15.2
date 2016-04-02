# -*- coding: utf-8 -*-
import os, shutil
import xbmc, xbmcaddon

IsraeLiveAddon = xbmcaddon.Addon("plugin.video.israelive")
IsraeLiveProfileDir = xbmc.translatePath(IsraeLiveAddon.getAddonInfo("profile")).decode("utf-8")
IsraeLiveLogosDir = os.path.join(IsraeLiveProfileDir, "logos")
if not os.path.exists(IsraeLiveLogosDir):
	os.makedirs(IsraeLiveLogosDir)
	
SkinAddon = xbmcaddon.Addon("skin.eminence.zeev")
SkinAddonPath = xbmc.translatePath(SkinAddon.getAddonInfo("path")).decode("utf-8")
SkinLogosDir = os.path.join(SkinAddonPath, 'extras', 'icons', 'israelive_logo')

iptvLogos = [
	["���� ����� 2", "channel_news_logo.png", "0ebda83cbbc38a17e49810ed33e1dcac.bmp"],
	["���� 2", "channel_22_logo.png", "9b45cef7fa2628cd36665b1bf55fce99.jpg"],
	["���� �����", "channel_knesset_logo.png", "9dd9aa238fa6fe90205cdc97e8a48df9.jpg"],
	["���� �������", "channel_hidabroot_logo.png", "9ab46a62d98275ee65c392474a48194b.jpg"],
	["���� 9", "channel_9_logo.png", "51dc4d7eaf924a7ef11e37ba45438556.png"],
	["���� ������", "channel_33_logo.png", "269a908ece2a41cf50cdb8392ab757d7.png"],
	["���� �����", "channel_meir_logo.png", "446f83c197fe7f0dd917cab8a0daf56b.jpg"],
	["����� ������", "channel_1_logo.png", "45140b5df5b02c324aab643ce4613035.jpg"],
	["���� 10", "channel_10_logo.png", "453391caae5b0a6fc4e80964f78a7452.png"],
	["���� ������", "channel_21_logo.png", "803596021c6fc4fca1b3329879931811.jpg"],
	["���� ������", "channel_20_logo.png", "c6579e888c5182c3d76a5c2b61630075.jpg"],
["���� �������", "channel_24_logo.png", "d8e4bbcfdb499174e2836f5e200e52e0.jpg"], 
["���� �����", "radio_morest.png", "7ce5dccfffc2bd8278bbd405e5fd7098.png"], 
["���� 102", "radio_102fm.png", "35e657c6ec6fc2abdaae8b2c176b02d6.jpg"], 
["���� ���", "radio_ glz.png", "45c57478a2775bfa7524153baac314b3.jpg"], 
]

for iptvLogo in iptvLogos:
	try:
		shutil.copyfile(os.path.join(SkinLogosDir, iptvLogo[1]), os.path.join(IsraeLiveLogosDir, iptvLogo[2]))
	except Exception as ex:
		print ex
