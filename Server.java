import java.io.*;
import java.net.*;

class Server
{
    public static void main(String args[])throws Exception{
        DatagramSocket serverSocket = new DatagramSocket(9876);
        byte[] receiveData = new byte[1024];
        byte[] sendData;

        while(true)
        {
            DatagramPacket packet = new DatagramPacket(receiveData, receiveData.length);
            serverSocket.receive(packet);

            String message = new String(packet.getData(), 0, packet.getLength());
            String new_message = message + "!";
            sendData = new_message.getBytes();
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, packet.getAddress(), packet.getPort());
            serverSocket.send(sendPacket);

           //Uzupełnij pętle tak aby serwer zwracał wiadomość wysłaną przez klienta
        }
    }
}