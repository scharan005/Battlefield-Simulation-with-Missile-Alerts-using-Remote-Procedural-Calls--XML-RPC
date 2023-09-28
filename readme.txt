

Instructions to Run the Code:
-----------------------------
Prerequisites:
- Ensure you have Python 3.x installed on your machine.
- Ensure you have the `xmlrpc` library installed. If not, you can install it using pip:

Note: for running in the local machine you have to change the server.py and client.py files
In server.py.......client_url = "http://localhost:8000/" and in client.py.........client_server = xmlrpc.server.SimpleXMLRPCServer(
        ("localhost", 8000), allow_none=True)

copy these statements to run in the localmachine....run python server.py and python client.py in different terminals.

For outputs: The values can be changed in the config file.



Steps:
1. Navigate to the project directory.
2. Start the server using the command:
3. In a separate terminal, navigate to the project directory again and run the client using the command:
4. The server will simulate missile strikes and the client will respond with soldier actions.
5. Observe the logs and interactions between the server and client in their respective terminals.

Note: for running in the local machine you have to change the server.py and client.py files
In server.py.......client_url = "http://localhost:8000/" and in client.py.........client_server = xmlrpc.server.SimpleXMLRPCServer(
        ("localhost", 8000), allow_none=True)

copy these statements to run in the localmachine....run python server.py and python client.py in different terminals.


