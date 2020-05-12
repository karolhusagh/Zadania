import socket
from _thread import *
from player import Player
from ball import Ball
from game import Game, update_game_state
import pickle
import pygame

w, h = 788, 444
players = [Player(50, 414, 30, (255, 0, 0), 30, w / 2 - 30, pygame.K_a, pygame.K_d, pygame.K_w),
           Player(w - 50, 414, 30, (0, 255, 0), w / 2 + 30, w - 30, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)]
ball = Ball(200, 250, 0, 0, 20)
game = Game()

'''
    Utwórz serwer przypisany do adresu 127.0.0.1 i portu 5555 obsługujący dwóch klientów.
    Po połączeniu z klientem wyślij tablicę obiektów [Player(gracza), Player(przeciwnika), Ball, Game].
    Odbieraj cyklicznie wysyłane przez klientów współrzędne postaci (tablica [x,y]), użyj ich do aktualizacji obiektów Player, Ball, Game oraz
    odeślij do klienta wspołrzędne postaci przeciwnika i aktualne obiekty Ball oraz Game w formie tablicy [x,y,Ball,Game].

    Player.x, Player.y przechowują współrzędne graczy.

    Aby zaktualizować obiekty Ball i Game wykonujemy funkcje:
        ball.move(players[0], players[1], game, w)
        update_game_state(ball, players[0], players[1], game, w)
    Uwaga! Aktualizacje obiektu Ball należy wykonywać tylko w jednym z wątków.

    Wysyłane i odbierane obiekty należy obsługiwać przy pomocy modułu pickle.
'''

HOST = "127.0.0.1"  # To be changed to your local IP address
PORT = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((HOST, PORT))
except socket.error as e:
    print(str(e))
try:
    s.listen(2)
except socket.error as e:
    print(str(e))
print("Waiting for a connection")


def threaded_server():
    global ball, players, game, w
    ball.move(players[0], players[1], game, w)
    update_game_state(ball, players[0], players[1], game, w)


def threaded_client(connection, player):
    global ball, players, game, w
    my_id = player
    opp_id = 0
    if my_id == 1:
        opp_id = 0
    else:
        opp_id = 1

    init_data = [players[my_id], players[opp_id], ball, game]
    connection.send(pickle.dumps(init_data))

    while True:
        data = connection.recv(2048)
        update = pickle.loads(data)

        players[my_id].x = update[0]
        players[my_id].y = update[1]

        send_data = pickle.dumps([players[opp_id].x, players[opp_id].y, ball, game])
        connection.send(send_data)

    connection.close()

start_new_thread(threaded_server, ())
my_id = 0
while True:
    client, addr = s.accept()
    start_new_thread(threaded_client, (client, my_id))
    my_id += 1
