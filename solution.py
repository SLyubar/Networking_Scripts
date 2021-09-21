from socket import *

# def smtp_client(port=25, mailserver='smtp.nyu.edu'):
def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    

    recv = clientSocket.recv(1024).decode()
    # print(recv)
    # if recv[:3] != '220':
    #     print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.

    mailfromCommand = 'MAIL FROM: <sl4256@nyu.edu>\r\n'
    clientSocket.send(mailfromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    # print(recv2)
    # if recv2[:3] != '250':
    #     print('250 reply not received from server.')


    # Send RCPT TO command and print server response.
 
    rcptoCommand = 'RCPT TO: <stan.lyubarskiy@gmail.com>\r\n'
    clientSocket.send(rcptoCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    # print(recv3)
    # if recv3[:3] != '250':
    #     print('250 reply not received from server.')


    # Send DATA command and print server response.
    
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    # print(recv4)
    # if recv4[:3] != '354':
    #     print('354 reply not received from server.')
    

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    recv5 = clientSocket.recv(1024).decode()
    print(recv5)
    # Fill in end

    # Message ends with a single period.
   
    clientSocket.send(endmsg.encode())
    recv6 = clientSocket.recv(1024).decode()
    print(recv6)
    if recv6[:3] != '250':
        print('250 reply not received from server.')
    

    # Send QUIT command and get server response.
    
    quit = 'QUIT\r\n'
    clientSocket.send(quit.encode())
    recv7 = clientSocket.recv(1024).decode()
    # print(recv7)
    # if recv7[:3] != '221':
    #     print('221 reply not received from server.')


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
    # smtp_client(25, 'smtp.nyu.edu')