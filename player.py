import socket

class Player(object):
  def __init__(self, ip_address, name, browser_ui, hand):
    self.ip_address = ip_address
    self.name = name
    self.browser_ui = browser_ui
    self.hand = hand

  def connect_to_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((config.SERVER_HOST, config.SERVER_PORT))
    s.listen(1)
    conn, _ = s.accept()
    return conn

  def join_game():
    conn = self.connect_to_server()
    self.hand = conn.send(self.name, config.GAME_REQUEST_TOKEN)

  def quit_game():
    conn = self.connect_to_server()
    conn.send(self.name, config.GAME_LEAVE_REQUEST)

  def play_card(card):
    conn = self.connect_to_server()
    conn.send(self.name, card)