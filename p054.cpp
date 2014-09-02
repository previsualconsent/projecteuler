#include "hand.h"
#include <iostream>
#include <fstream>
#include <string>
int main()
{
   std::ifstream ifile;
   ifile.open("p054_poker.txt");
   std::string in;
   int count = 0;
   while( std::getline(ifile,in))
   {
      PokerHand h1(in.substr(0,14));
      PokerHand h2(in.substr(15,14));
      std::cout << h1;
      std::cout << h2;
      std::cout << (h1 > h2) << std::endl;
      count += (h1 > h2);
   }
   std::cout << "Total: " << count << std::endl;
}
