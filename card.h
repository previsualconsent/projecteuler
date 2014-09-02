#include <iostream>
#include <string>
//23456789TJQKA
//CSDH
enum Suit
{
   NO_SUIT,
   CLUB,
   SPADE,
   DIAMOND,
   HEART
};

enum Rank
{
   NO_RANK,
   TWO,
   THREE,
   FOUR,
   FIVE,
   SIX,
   SEVEN,
   EIGHT,
   NINE,
   TEN,
   JACK,
   QUEEN,
   KING,
   ACE
};

class Card
{
   public:
      Card(std::string in_str)
      {
         if(in_str.size() != 2)
         {
            std::cout << "Card length not 2 setting to \n";
            m_suit = NO_SUIT;
            m_rank = NO_RANK;
            m_value = 0;
            return;
         }

         m_card_string = in_str;
         set_rank(in_str[0]);
         set_suit(in_str[1]);
         calc_value();
      }

      void set_rank(char r)
      {
         m_rank_c = r;
         switch(r)
         {
            default:
               m_rank = NO_RANK;
               break;
            case '2':
               m_rank = TWO;
               break;
            case '3':
               m_rank = THREE;
               break;
            case '4':
               m_rank = FOUR;
               break;
            case '5':
               m_rank = FIVE;
               break;
            case '6':
               m_rank = SIX;
               break;
            case '7':
               m_rank = SEVEN;
               break;
            case '8':
               m_rank = EIGHT;
               break;
            case '9':
               m_rank = NINE;
               break;
            case 'T':
               m_rank = TEN;
               break;
            case 'J':
               m_rank = JACK;
               break;
            case 'Q':
               m_rank = QUEEN;
               break;
            case 'K':
               m_rank = KING;
               break;
            case 'A':
               m_rank = ACE;
               break;
         } 
      }
      void set_suit(char s)
      {
         m_suit_c = s;
         switch(s)
         {
            default:
               m_suit = NO_SUIT;
               break;
            case 'C':
               m_suit = CLUB;
               break;
            case 'S':
               m_suit = SPADE;
               break;
            case 'D':
               m_suit = DIAMOND;
               break;
            case 'H':
               m_suit = HEART;
               break;
         }
      }

      void calc_value()
      {
         m_value = int(m_rank);
      }

      float value() const
      {
         return m_value;
      }
      Suit suit() const
      {
         return m_suit;
      }
      Rank rank() const
      {
         return m_rank;
      }
      std::string string() const
      {
         return m_card_string;
      }

   private:
      Suit m_suit;
      Rank m_rank;
      char m_suit_c;
      char m_rank_c;
      float m_value;
      std::string m_card_string;
};

inline bool operator< (const Card& lhs, const Card& rhs)
{
   return lhs.value() < rhs.value();
}
inline bool operator> (const Card& lhs, const Card& rhs){return rhs < lhs;}
inline bool operator<=(const Card& lhs, const Card& rhs){return !(lhs > rhs);}
inline bool operator>=(const Card& lhs, const Card& rhs){return !(lhs < rhs);}

std::ostream& operator<<(std::ostream& out, const Card& c){
      return out << c.string();
}
