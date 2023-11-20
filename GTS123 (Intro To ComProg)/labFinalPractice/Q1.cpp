#include <iostream>
#include <string>

bool isNumber(std::string s) //check for positive integer since '-' return false in function isdigit()
{
    for (char ch:s){
        if (!isdigit(ch)) return false;
    }
    return true;
}


int main(){
    int money, num;
    std::string act,numStr;
    std::cout<<"Enter the initial balance: ";
    std::cin>>money;

    while (true){
        std::cout<<"Transaction type and amount (\"done 0\" to exit):";
        std::cin>>act>>numStr;
        if (act=="done") break;
        else if (act!="W" && act!="D"){
            std::cout<<"> Invalid transaction type\n";
            continue;
        }

        num = std::stoi(numStr);
        if (act=="D"){
            money+=num;
            std::cout<<"> Deposit = "<<num<<" THB, current balance = "<<money<<" THB.\n";
        }
        else if (money<num){
            std::cout<<"> Invalid transaction, low money lol\n";
        }
        else {
            money-=num;
            std::cout<<"> Withdrawal = "<<num<<" THB, current balance = "<<money<<" THB.\n";
        }
    }

    std::cout<<"> Current balance = "<<money<<" THB.";
}