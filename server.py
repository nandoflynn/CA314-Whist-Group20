# Create a PodSixNet to make sure everything is working
# Put this file in the same folder as the game
# Creates a bare bones connection that listens for connections on a default port
# add next few lines to whist.py
"""
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep
"""
# make the whist game extend connectionlistener
"""
class WhistGame(ConnectionListener):
"""
# Add next to bottom of whist game class init method
"""
self.Connect()
"""
# Add next to beginning of the update function so server looks for new events/messages
"""
connection.Pump()
self.Pump()
"""
# Add next to class on client side
"""
def network_startgame(self, data):
	self.running = True
	self.num = data["player"]
	self.gameid = data["gameid"]
"""
# the client should wait untill it receives the message to start the game
# Add next to the end of __init__
"""
self.running = False
while not self.running:
	self.Pump()
	connection.Pump()
	sleep(0.01)
# determine attributes from player
if self.num == 0
	self.turn = True
	self.handOne = self.player1
	self.handTwo = self.player2
	self.handThree = self.player3
	self.handFour = self.player4
else:
	self.turn = False
	self.handOne = self.player4
	self.handTwo = self.player3
	self.handThree = self.player2
	self.handFour = self.player1
"""
# Add next to the self.drawHUD() in the update method
"""
self.drawOwnermap()
"""
# Client doesnt know what to do with information, add next to client file
"""
def network_place(self, data):
	# get attributes
	x = data[""]
	y = data[""]
	z = data[""]
	if z:
		self. = True
	else:
		self. = True
"""
# need to create a delay function of 10 frames before game allows player to play card, Add next to the game.py
"""
self.justPlayed = 10
"""
# reset to 10 each time, Add next to game to check if it is the players turn and they havent already played
"""
if pygame.mouse.get_pressed()[0] and not isoutofbounds:
#---------------change to------------------#
if pygame.mouse.get_pressed()[0] and not isoutofboundsand self.turn == True and self.justPlayed <= 0:
	self.justPlayed = 10
"""
# add next to top of the update function, decrements variable by 1 every frame
"""
self.justPlayed -= 1
"""
# find screen.blit function that draws and inside drawHUD() method change it to
"""
self.screen.blit(self.greenindicator if self.turn else self.reindicator, (130, 395))
"""
# implement yourturn on client side game.py
"""
def network_yourturn(self, data):
	self.turn = data["torf"]
"""
# Add next methods to client side to tell whether they won or lost, updating the game state appropriately
"""
def Network_win(self, data):
    # game logic here
    #add one point to my score
    self.me+=1
def Network_lose(self, data):
	# game logic here
    #add one to other players score
    self.otherplayer+=1
"""
# Add next at the top of update function
"""
if self.me + self.otherplayer == 36:
    self.didiwin = True if self.me > self.otherplayer else False
    return 1
"""
# Add next to very bottom of bg.update()
"""
if bg.update() == 1:
    break
"""
# Add to very end with no indentation
"""
bg.finished()
"""
# Add to client class
"""
def Network_close(self, data):
    exit()
"""
import PodSixNet.Channel
import PodSixNet.Server
from time import sleep

class ClientChannel(PodSixNet.Channel.Channel):
	def network(self, data):
		print(data)

	def Close(self):
    self._server.close(self.gameid)
	
	def network_place(self, data):
		# deconsolidate all of the data from the dictionary
		z = data[""]
		x = data[""]
		y = data[""]
		# player number ( 1, 2, 3, 4)
		num = data["num"]
		#id of game given by server at start of game
		self.gameid = data["gameid"]
		# tells server to place line
		self._server.playCard(z, x, y, data, self.gameid, num)

	def close(self, gameid):
		try:
			game = [a for a in self.games if a.gameid==gameid][0]
			game.player0.Send({"action":"close"})
			game.player1.Send({"action":"close"})
		except:
			pass


class WhistServer(PodSixNet.Server.Server):
	channelClass = ClientChannel
	def __init__(self, *args, **kwargs):
		# Calling the init of the class we are extending
		PodSixNet.Server.Server.__init__(self, *args, **kwargs)
		self.games = []
		self.queue = None
		self.currentIndex = 0
	
	def connected(self, channel, addr):
		# Prints when a connection is made
		print("New Connection: {}".format(channel))
		# Puts a client in a queue or they join a game
		# Server checks if game in queue if not creates one
		# sends a start game message to payers
		if self.queue == None:
			self.currentIndex += 1
			channel.gameid = self.currentIndex
			self.queue = Game(channel, self.currentIndex)
		else:
			channel.gameid = self.currentIndex
			self.queue.player1 = channel
			self.queue.player0.send({"action": "startgame","player": 0, "gameid": self.queue.gameid})
			self.queue.player1.send({"action": "startgame","player": 1, "gameid": self.queue.gameid})
			self.queue.player2.send({"action": "startgame","player": 2, "gameid": self.queue.gameid})
			self.queue.player3.send({"action": "startgame","player": 3, "gameid": self.queue.gameid})
			self.games.append(self.queue)
			self.queue = None
	
	# this enables the server to call playcard() method
	# Loops through all the games and finds the one with the same gameid as the client then relays the information to the game
	def playCard(self, is_h, x, y, data, gameid, num):
		game = [a for a in self.games if a.gameid == gameid]
		if len(game) == 1:
			game[0].playCard(is_h, x, y, data, num)
	# game logic to determine whether player has won during their turn
	def trump(self):
	# 1
		index = 0
		change = 3
		# 2
		for game in self.games:
			#put game logic here

		self.games[index].turn = change if change != 3 else self.games[index].turn
		game.player1.Send({"action":"yourturn", "torf":True if self.games[index].turn == 1 else False})
		game.player0.Send({"action":"yourturn", "torf":True if self.games[index].turn == 0 else False})
		index += 1
		self.Pump()

class WhistGame(self):
	def __init__(self):
	
	# This will check if it is a clients turn and add piece to 
	def playCard(self, is_h, x, y, data, num):
		# make sure it is their turn
		if num == self.turn:
			self.turn = 0 if self.turn else 1
			# place card in game
			# logic here
			
			self.player0.Send(data)
			self.player1.Send(data)
			self.player2.Send(data)
			self.player3.Send(data)
			# sending client a message tork stands for true or false
			self.player0.send({"action":"yourturn", "torf":True if self.turn == 1 else False})
			self.player1.send({"action":"yourturn", "torf":True if self.turn == 1 else False})
			self.player2.send({"action":"yourturn", "torf":True if self.turn == 1 else False})
			self.player3.send({"action":"yourturn", "torf":True if self.turn == 1 else False})


print("Starting server on localhost")
whistServe = WhistServer()
while True:
	whistServe.trump()
	sleep(0.01)