from http.server import BaseHTTPRequestHandler, HTTPServer
import os

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """ Специальный класс для обработки GET-запросов """

    def do_GET(self):
        """ Метод для обработки GET-запросов """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            try:
                with open("contact.html", "r", encoding="utf-8") as file:
                    html_content = file.read()
                self.wfile.write(bytes(html_content, "utf-8"))
            except FileNotFoundError:
                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("<h1>404 Not Found</h1>", "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<h1>404 Not Found</h1>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")