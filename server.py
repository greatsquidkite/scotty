#!/usr/bin/env python3

import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QVBoxLayout, QLabel

SERVER_PID = 0

def server():
	if localOnly:
		s = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
	else:
		exit()
	s.serve_forever()

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()

#check for no remote access
localOnly = QCheckBox('Local Only')

#connect start button to server function
run_btn = QPushButton('Start Server')
run_btn.clicked.connect(server)

layout.addWidget(QLabel('Scotty - Simple HTTP File Server'))
layout.addWidget(localOnly)
layout.addWidget(run_btn)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())