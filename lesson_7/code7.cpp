#include <iostream>
#include <unistd.h>
using namespace std;

int main(int argc, char *argv[])
{
  int y=1;
  for(int x=0; x<10000; x++)
  {
    cout << ++y+y++ << endl;
    sleep(1);
  }
  return 0;
}