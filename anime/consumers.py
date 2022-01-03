import json
from random import randint
from time import sleep

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class WSConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.room_name = "event"
		self.room_group_name = self.room_name+"_amr"
		
		await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

		# print(self.room_group_name)
		await self.accept()
		
		print("#######CONNECTED############")
		

	
	async def disconnect(self, code):
		print("DISCONNECED CODE: ",code)


	async def receive(self, text_data=None, bytes_data=None):
		print(" MESSAGE RECEIVED")
		# Receive message from room group
		text_data_json = text_data
		message = text_data_json['message']
		# Send message to WebSocket
		await self.send(text_data=json.dumps({
		    'message': message
		}))
