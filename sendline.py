import requests

class Sendline:
	'''
	#download sticker http://cons-robotics.com/LINEAPI/sticker.pdf

	#generate token from https://notify-bot.line.me/my/
	Example:
	----------------------------------
	token = 'xdkakfdjksjdfayfdyaodf'
	messenger = Sendline(token)

	#send message
	messenger.sendtext('Hello world')

	#send sticker
	messenger.sticker(1,1)

	#send image
	messenger.sendimage('https://img.pngio.com/python-logo-python-logo-png-268_300.png')
	----------------------------------
	'''

	def __init__(self,tok):
		self.tok = tok

	def Lineconfig(self,command):
		url = 'https://notify-api.line.me/api/notify'
		token = self.tok ## EDIT
		header = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
		return requests.post(url, headers=header, data = command)

	def sendtext(self,message):
		# send plain text to line
		command = {'message':message}
		return self.Lineconfig(command)


	def sticker(self,sticker_id,package_id,message=' '):
		command = {'message':message,'stickerPackageId':package_id,'stickerId':sticker_id}
		return self.Lineconfig(command)


	def sendimage(self,url):
		command = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
		return self.Lineconfig(command)


if __name__ == '__main__':
	
	token = 'N8V9EwCTTqmSjnWAXxdadfadffadsfasdfasdfasfWK8KxKJ'
	messenger = Sendline(token)

	#send message
	messenger.sendtext('Hello world')

	#send sticker
	messenger.sticker(1,1)

	#send image
	messenger.sendimage('https://img.pngio.com/python-logo-python-logo-png-268_300.png')