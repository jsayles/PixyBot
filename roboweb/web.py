from flask import Flask,request, redirect,render_template
import time
import robot

speed = 0

def moveFoward(speedBackMotor):
	robot.lf(150)
	robot.rf(150)

def moveBackward(speedBackMotor):
	robot.lb(150)
	robot.rb(150)

def stopMoving():
	robot.stop()

def turnFowardRight(speedBackMotor,speedFrontMotor):
	robot.rf(150)

def turnFowardLeft(speedBackMotor,speedFrontMotor):
	robot.lf(150)

def increaseSpeed():
	print("increase speed")
	global speed
	global maxSpeed
	global minSpeed
	if speed <= maxSpeed:
		speed = speed + 0.1 #increaseing speed by 10
		print 'speed +0.1'
	else:
		speed = maxSpeed

def decreaseSpeed():
	print("decrease speed")
	global speed
	global maxSpeed
	global minSpeed
	if speed <= minSpeed:
		speed = minSpeed
		print 'speed = minSpeed'
	else:
		speed = speed - 0.1
		print 'speed -0.1'

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/controlit', methods = ['POST'])
def control():
    buttonHit = request.form['buttonPress']
    print("The button hit is '" + buttonHit + "'")
    if buttonHit == 'Fast':
        increaseSpeed()
    elif buttonHit == 'Slow':
        decreaseSpeed()
    elif buttonHit == 'Foward':
        moveFoward(speed)
        time.sleep(1);
        stopMoving()
	print ("Move Foward")
    elif buttonHit == 'Back':
        moveBackward(speed)
        time.sleep(1);
        stopMoving()
	print ("Move Back")
    elif buttonHit == 'Left':
        turnFowardLeft(speed,0.6)
        time.sleep(1);
        stopMoving()
	print ("Move Left")
    elif buttonHit == 'Right':
        turnFowardRight(speed,0.7)
        time.sleep(1);
        stopMoving()
	print ("Move Right")
    else :
        print("Do Nothing")
		
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
