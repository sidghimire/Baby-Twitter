// include the library code:
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(20,4);
  lcd.clear();

  Serial.begin(9600);
}
int a=0;
void loop() {
  
  if(Serial.available()){
    String ch;
    ch=Serial.readString();
    ch.trim();
    
    if(ch=="##"){
      a=0;
    }else if(ch=="###"){
      a=1;
    }else if(ch=="####"){
      a=2;
    }else if(ch=="#####"){
      a=3;
    }else{}
    lcd.setCursor(0,a);
    if(ch!="###" || ch!="##"){
      lcd.print(ch);
    }
  }
  
}

