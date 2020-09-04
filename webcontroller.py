import os
from flask import Flask, render_template
from threading import Thread
from time import sleep
import eiscp

app = Flask(__name__)

# https://github.com/miracle2k/onkyo-eiscp
# Create a receiver object, connecting to the host
receiver = eiscp.eISCP('10.210.10.133')
current = receiver.command('volume=query')
output = (current)[1]

@app.route("/")
def home():
	return render_template('index.html', output = output)
	   
@app.route('/full')
def full():
	global output
	global current
	output = int(125)
	cmd = f"volume={output}"
	receiver.command(cmd)
	current = receiver.command('volume=query')
	receiver.command('display-mode=03')
	output = (current)[1]
	return ("nothing")
    
@app.route('/button75')
def button75():
	global output
	global current
	output = int(94)
	cmd = f"volume={output}"
	receiver.command(cmd)
	current = receiver.command('volume=query')
	receiver.command('display-mode=03')
	output = (current)[1]
	return ("nothing")

@app.route('/button50')
def button50():
	global output
	global current
	output = int(63)
	cmd = f"volume={output}"
	receiver.command(cmd)
	current = receiver.command('volume=query')
	receiver.command('display-mode=03')
	output = (current)[1]
	return ("nothing")

@app.route('/button25')
def button25():
	global output
	global current
	output = int(32)
	cmd = f"volume={output}"
	receiver.command(cmd)
	current = receiver.command('volume=query')
	receiver.command('display-mode=03')
	output = (current)[1]
	return ("nothing")

@app.route('/buttonmute')
def buttonmute():
	global output
	global current
	output = int(0)
	cmd = f"volume={output}"
	receiver.command(cmd)
	current = receiver.command('volume=query')
	receiver.command('display-mode=03')
	output = (current)[1]
	return ("nothing")

@app.route('/button10')
def button10():
	global output
	global current
	output = int(output) + 10
	cmd = f"volume={output}"
	receiver.command(cmd)
	current = receiver.command('volume=query')
	receiver.command('display-mode=03')
	output = (current)[1]
	return ("nothing")
    
@app.route('/button5')
def button5():
	global output
	global current
	output = int(output) + 5
	cmd = f"volume={output}"
	receiver.command(cmd)
	current = receiver.command('volume=query')
	receiver.command('display-mode=03')
	output = (current)[1]
	return ("nothing")

@app.route('/button1')
def button1():
	global output
	global current
	output = int(output) + 1
	cmd = f"volume={output}"
	receiver.command(cmd)
	current = receiver.command('volume=query')
	receiver.command('display-mode=03')
	output = (current)[1]
	return ("nothing")
    
@app.route('/button01')
def button01():
	global output
	global current
	output = int(output) - 1
	cmd = f"volume={output}"
	receiver.command(cmd)
	current = receiver.command('volume=query')
	receiver.command('display-mode=03')
	output = (current)[1]
	return ("nothing")
    
@app.route('/button05')
def button05():
	global output
	global current
	output = int(output) - 5
	cmd = f"volume={output}"
	receiver.command(cmd)
	current = receiver.command('volume=query')
	receiver.command('display-mode=03')
	output = (current)[1]
	return ("nothing")
    
@app.route('/button010')
def button010():
	global output
	global current
	output = int(output) - 10
	cmd = f"volume={output}"
	receiver.command(cmd)
	current = receiver.command('volume=query')
	receiver.command('display-mode=03')
	output = (current)[1]
	return ("nothing")
	
n = 1
def timer():
	while n > 0:
		receiver.command('display-mode=03')
		sleep(60)

if __name__ == "__main__":
	t1 = Thread(target=timer)
	t1.start()
	app.run(host='10.210.10.166', port=6969)