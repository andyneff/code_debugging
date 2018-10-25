#include <iostream>
#include <unistd.h>
#include <signal.h>
using namespace std;

int main(int argc, char *argv[])
{
  int y=1;
  for(int x=0; x<10000; x++)
  {
    cout << "8: " << ++y+y++ << endl;
    if(x == 10)
    {
      raise(SIGSTOP);
    }
  }
  return 0;
}