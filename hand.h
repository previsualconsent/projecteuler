#include "card.h"
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <iostream>
class Hand
{
   public:
      //input string hand format "AA BB CC DD EE FF GG"
      Hand(std::string hand_string)
      {
         float hs = (hand_string.size()+1)/3.0;
         int handsize = int(hs);
         if(handsize != hs)
            return;
         for(int i=0; i<handsize; i++)
         {
            m_cards.push_back(Card(hand_string.substr(i*3,2)));
         }
         std::sort(m_cards.begin(),m_cards.end());
      }

   protected:
      std::vector<Card> m_cards;
};

std::string PokerHandTypes[10] = {
         "HIGH_CARD",      // 0
         "PAIR",           // 1
         "TWO_PAIRS",      // 2
         "THREE_KIND",     // 3
         "STRAIT",         // 4
         "FLUSH",          // 5
         "FULL_HOUSE",     // 6
         "FOUR_KIND",      // 7
         "STRAIT_FLUSH",   // 8
         "ROYAL_FLUSH"     // 9
};
enum PokerHandType
{
   HIGH_CARD,      // 0
   PAIR,           // 1
   TWO_PAIRS,      // 2
   THREE_KIND,     // 3
   STRAIT,         // 4
   FLUSH,          // 5
   FULL_HOUSE,     // 6
   FOUR_KIND,      // 7
   STRAIT_FLUSH,   // 8
   ROYAL_FLUSH     // 9
};
class PokerHand : Hand
{
   // High Card: Highest value card.
   // One Pair: Two cards of the same value.
   // Two Pairs: Two different pairs.
   // Three of a Kind: Three cards of the same value.
   // Straight: All cards are consecutive values.
   // Flush: All cards of the same suit.
   // Full House: Three of a kind and a pair.
   // Four of a Kind: Four cards of the same value.
   // Straight Flush: All cards are consecutive values of same suit.
   // Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
   public:

      PokerHand(std::string hand_string) 
         : Hand(hand_string)
      {
         assign_type();
      }
      void assign_type()
      {
         m_hand_type = HIGH_CARD;
         m_rank = m_cards[4].rank();

         bool strait = false;
         bool flush = false;
         if (m_cards[0].rank() + 1 == m_cards[1].rank() &&
               m_cards[0].rank() + 2 == m_cards[2].rank() &&
               m_cards[0].rank() + 3 == m_cards[3].rank() &&
               m_cards[0].rank() + 4 == m_cards[4].rank())
         {
            strait = true;
            m_hand_type = STRAIT;
         }
         if (m_cards[0].suit() == m_cards[1].suit() &&
               m_cards[0].suit() == m_cards[2].suit() &&
               m_cards[0].suit() == m_cards[3].suit() &&
               m_cards[0].suit() == m_cards[4].suit())
         {
            flush = true;
            m_hand_type = FLUSH;
         }

         if (flush && strait)
         {
            if(m_cards[4].rank() == ACE)
               m_hand_type = ROYAL_FLUSH;
            else
               m_hand_type = STRAIT_FLUSH;
            return;
         }
         else if (flush || strait)
            return;

         std::map<Rank,int> hand_count;
         for( std::vector<Card>::iterator ic = m_cards.begin();
               ic != m_cards.end();
               ic++)
         {
            hand_count[ic->rank()] += 1;
            switch(hand_count[ic->rank()])
            {
               case 2:
                  switch(m_hand_type)
                  {
                     case HIGH_CARD:
                        m_hand_type = PAIR;
                        m_rank = ic->rank();
                        break;
                     case PAIR:
                        m_hand_type = TWO_PAIRS;
                        m_rank = std::max(m_rank,ic->rank());
                        break;
                     case THREE_KIND:
                        m_hand_type = FULL_HOUSE;
                        break;
                     default:
                        break;
                  }
                  break;
               case 3:
                  switch(m_hand_type)
                  {
                     case PAIR:
                        m_hand_type = THREE_KIND;
                        break;
                     case TWO_PAIRS:
                        m_hand_type = FULL_HOUSE;
                        m_rank = ic->rank();
                        return;
                        break;
                     default:
                        break;
                  }
                  break;
               case 4:
                  m_hand_type = FOUR_KIND;
                  return;
                  break;
               default:
                  break;
            }
         }
      }

      PokerHandType getHandType() const {return m_hand_type;}
      std::vector<Card> getCards() const {return m_cards;}
      Rank getRank() const {return m_rank;}
   private:
      PokerHandType m_hand_type;
      Rank m_rank;

};

inline bool operator< (const PokerHand& lhs, const PokerHand& rhs)
{
   if( lhs.getHandType() != rhs.getHandType() )
      return  lhs.getHandType() < rhs.getHandType();
   else if (lhs.getRank() != rhs.getRank())
      return  lhs.getRank() < rhs.getRank();
   else
      for(int i = 4; i >=0; --i)
         if( lhs.getCards()[i].value() != rhs.getCards()[i].value() )
            return  lhs.getCards()[i].value() < rhs.getCards()[i].value();

   return false;
}
inline bool operator> (const PokerHand& lhs, const PokerHand& rhs){return rhs < lhs;}
inline bool operator<=(const PokerHand& lhs, const PokerHand& rhs){return !(lhs > rhs);}
inline bool operator>=(const PokerHand& lhs, const PokerHand& rhs){return !(lhs < rhs);}

std::ostream& operator<<(std::ostream& out, const PokerHand& h){
   std::cout << "Hand of " << h.getCards().size() << " cards: ";
      for(std::vector<Card>::iterator it =  h.getCards().begin();
            it != h.getCards().end();
            ++it)
         out << (*it) << ' ';

      out << ": " << PokerHandTypes[h.getHandType()] << "\n";
      return out;

}
