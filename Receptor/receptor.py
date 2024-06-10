import socket
import plotly.graph_objects as go
from tkinter import ttk
import tkinter as tk
import socket

def diferentialManchesterDecoding(data):
    decoded_signal = []
    print(data)
    return decoded_signal

def generateGraph(data):
    encoded_signal = diferentialManchesterDecoding(data)

    x = list(range(len(encoded_signal)))
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x,
        y=encoded_signal,
        mode='lines+markers',
        line=dict(shape='hv'),
        name='Manchester Differential'
    ))

    fig.update_layout(
        title='Gráfico de Codificação Manchester Diferencial',
        xaxis_title='Tempo',
        yaxis_title='Nível de Sinal',
        yaxis=dict(
            tickvals=[0, 1],
            ticktext=['Low (0)', 'High (1)']
        )
    )

    fig.show()

def inverseProcess(data):
    generateGraph(data)
    # binary_string = decrypt(data)
    # text = binaryToASCII(binary_string)
    # showOnScreen(text)

def start_server(host='10.181.5.79', port=1234):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Servidor escutando em {host}:{port}')

    while True:
        client_socket, client_address = server_socket.accept()
        try:
            data = client_socket.recv(1024)
            if data:
                print(f'Mensagem recebida: {data}')
        finally:
            client_socket.close()
            inverseProcess(data.decode('utf-8'))

if __name__ == "__main__":
    start_server()