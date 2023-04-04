import threading

from mcstatus import JavaServer


class MultiQuery:
    def _init_(self, host):
        self.host = host
        self.threads = []

    def find_servers(self, port_min=0, port_max=25565):
        for port in range(port_min, port_max):
            # make thread
            thread = threading.Thread(target=self.query, args=(port,))
            self.threads.append(thread)
            thread.start()

    def query(self, port):
        try:
            ip = f"{self.host}:{port}"
            #print(ip)
            server = JavaServer.lookup(ip, timeout=3)
            latency = server.ping()
            print(f"Found server on port {port} with latency {latency} ms")

            status = server.status()
            print(f"Server info: {status.raw}")
        except Exception as e:
            pass
            #print(f"Failed to query server on port {port}: {e}")

    def wait(self):
        for thread in self.threads:
            thread.join()


class Query:
    def _init_(self, host, port):
        self.host = host
        self.port = port

    def get_ping(self):
        server = JavaServer.lookup(f"{self.host}:{self.port}", timeout=0.3)
        latency = server.ping()
        return latency


multi_query = MultiQuery("168.119.143.94")
multi_query.find_servers(26110, 26500)
multi_query.wait()