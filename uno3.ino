#include <LedControl.h>

int DIN = 13;
int CS =  12;
int CLK = 11;
byte buf[8];
LedControl lc = LedControl(DIN, CLK, CS, 4);

void setup() {
  Serial.begin(115200);
  lc.shutdown(0, false);      //启动时，MAX72XX处于省电模式
  lc.setIntensity(0, 1);      //将亮度设置为最大值
  lc.clearDisplay(0);         //清除显示
}

void loop() {
  if (Serial.available()) {
    Serial.readBytes(buf, 8);
    printByte(buf);
    delay(50);
  }
}
//点阵显示函数
void printByte(byte character [])
{
  int i = 0;
  for (i = 0; i < 8; i++)
  {
    lc.setRow(0, i, character[i]);
  }
}
