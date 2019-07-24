#pragma config(Sensor, in1,    Gyroscope,      sensorGyro)
#pragma config(Sensor, dgtl7,  rightEncoder,   sensorQuadEncoder)
#pragma config(Sensor, dgtl10, leftEncoder,    sensorQuadEncoder)
#pragma config(Motor,  port1,           leftmotor,     tmotorVex393_HBridge, openLoop, encoderPort, dgtl10)
#pragma config(Motor,  port10,          rightmotor,    tmotorVex393_HBridge, openLoop, encoderPort, dgtl7)
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//

task main()
{
SensorValue[rightEncoder] = 0;

motor(leftmotor) = 110;
motor(rightmotor) = 127;

while(SensorValue[rightEncoder]<=1440){
	if(SensorValue[rightEncoder]<=1440){
		motor(leftmotor) = 110;
		motor(rightmotor) = 127;

}
	else {
	stopMotor(leftmotor);
	stopMotor(rightmotor);
}
}

}
