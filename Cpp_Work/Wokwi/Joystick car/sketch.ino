#include <Stepper.h>

#define VERT_PIN_D A0
#define HORZ_PIN_D A1
#define SEL_PIN_D 2

#define VERT_PIN_S A2
#define HORZ_PIN_S A3
#define SEL_PIN_S 3

#define ApD 12 // A+ line
#define AmD 13 // A- line
#define BpD 10 // B+ line
#define BmD 11 // B- line

#define ApS 8 // A+ line
#define AmS 9 // A- line
#define BpS 6 // B+ line
#define BmS 7 // B- line

String steerDir = "V"; // Steer motor init

const int stepsPerRevolution = 200;

Stepper steerMotor(stepsPerRevolution, ApS, AmS, BpS, BmS);
// int vertStickMap[3][2] = {
//   {1023, LOW}
// };

void setup()
{
    steerMotor.setSpeed(60);
    // put your setup code here, to run once:
    // set up joystick
    pinMode(VERT_PIN_D, INPUT);
    pinMode(HORZ_PIN_D, INPUT);
    pinMode(SEL_PIN_D, INPUT_PULLUP);
    pinMode(VERT_PIN_S, INPUT);
    pinMode(HORZ_PIN_S, INPUT);
    pinMode(SEL_PIN_S, INPUT_PULLUP);

    // set up motors
    pinMode(ApD, OUTPUT);
    pinMode(AmD, OUTPUT);
    pinMode(BpD, OUTPUT);
    pinMode(BmD, OUTPUT);

    // pinMode(ApS, OUTPUT);
    // pinMode(AmS, OUTPUT);
    // pinMode(BpS, OUTPUT);
    // pinMode(BmS, OUTPUT);
}

void runForward()
{
    delay(10);
    digitalWrite(BmD, LOW);
    digitalWrite(ApD, HIGH);
    delay(10);
    digitalWrite(ApD, LOW);
    digitalWrite(BpD, HIGH);
    delay(10);
    digitalWrite(BpD, LOW);
    digitalWrite(AmD, HIGH);
    delay(10);
    digitalWrite(AmD, LOW);
    digitalWrite(BmD, HIGH);
}

void runBackward()
{
    delay(10);
    digitalWrite(ApD, LOW);
    digitalWrite(BmD, HIGH);
    delay(10);
    digitalWrite(BmD, LOW);
    digitalWrite(AmD, HIGH);
    delay(10);
    digitalWrite(AmD, LOW);
    digitalWrite(BpD, HIGH);
    delay(10);
    digitalWrite(BpD, LOW);
    digitalWrite(ApD, HIGH);
}

void loop()
{
    // put your main code here, to run repeatedly:
    int vertD = analogRead(VERT_PIN_D);
    int horzD = analogRead(HORZ_PIN_D);
    bool selPressedD = digitalRead(SEL_PIN_D) == LOW;
    // int vertS = analogRead(VERT_PIN_S);
    // int horzS = analogRead(HORZ_PIN_S);
    // bool selPresseds = digitalRead(SEL_PIN_S) == LOW;

    if (vertD > 512)
    {
        if (steerDir != "V")
        {
            steerDir = "V";
            steerMotor.step(-stepsPerRevolution / 4);
        }
        runForward();
    }
    if (vertD < 512)
    {
        if (steerDir != "V")
        {
            steerDir = "V";
            steerMotor.step(-stepsPerRevolution / 4);
        }
        runBackward();
    }
    if (horzD > 512)
    {
        if (steerDir != "H")
        {
            steerDir = "H";
            steerMotor.step(stepsPerRevolution / 4);
        }
        runBackward();
    }

    if (horzD < 512)
    {
        if (steerDir != "H")
        {
            steerDir = "H";
            steerMotor.step(stepsPerRevolution / 4);
        }
        runForward();
    }
}
