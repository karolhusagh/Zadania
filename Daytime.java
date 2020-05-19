import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

class DateTime {

    public static void main(String[] args) {

        String address = "time.nist.gov";
        int port = 13;
        String line;

        /*
        Utwórz gniazdo na porcie przypisanym dla protokołu  DAYTIME, pobierz z niego strumień wejściowy i odczytaj odpowiedź serwera.
        Nie zapomnij o zamknięciu strumienia i gniazda.
        */
        try {
            Socket socket = new Socket(address, port);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }

            socket.shutdownInput();
            socket.close();

        }catch (IOException e){
            e.getStackTrace();
        }



    }
}
