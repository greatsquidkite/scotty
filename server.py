#!/usr/bin/env python3

import sys, threading
from http.server import HTTPServer, SimpleHTTPRequestHandler#, httplib
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFileDialog, QPushButton, QCheckBox, QVBoxLayout, QLabel

SERVER_IP  = ""
SERVER_DIR = ""

#TODO change server launch to threading

def server():
	print(dirpath.text())
	if localOnly:
		print("launching")
		s = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
	else:
		exit()
	thread = threading.Thread(target = s.serve_forever)
	thread.daemon = True

def kill_server():
	try:
		s.shutdown()
	except:
		print("Server not running")

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
# file = QFileDialog.getExistingDirectory('Select Directory')

#check for no remote access
localOnly = QCheckBox('Local Only')

#Directory Path input
dirpath = QLineEdit()

#connect start button to server function
run_btn = QPushButton('Start Server')
run_btn.clicked.connect(server)

#kill server
kill_btn = QPushButton('Kill Server')
kill_btn.clicked.connect(kill_server)

#build layout
layout.addWidget(QLabel('Scotty - Simple HTTP File Server'))
layout.addWidget(localOnly)
# layout.addWidget(file)
layout.addWidget(QLabel('Enter base directory path:'))
layout.addWidget(dirpath)
layout.addWidget(run_btn)
layout.addWidget(kill_btn)
window.setLayout(layout)
window.show()

#run app
sys.exit(app.exec_())