#include <iostream>
using namespace std;

class Node{
    public:
        int val;
        Node* next;
        Node(int x) : val(x), next(nullptr) {}
};

int makeListToInt(Node* head){
    int num = 0;
    int multiplier = 1;
    while(head){
        num += head->val * multiplier;
        multiplier *= 10;
        head = head->next;
    }
    return num;
}

Node* makeIntToList(int num){
    Node* head = nullptr;
    Node* curr = nullptr;
    while(num){
        int digit = num % 10;
        Node* newNode = new Node(digit);
        if(!head){
            head = newNode;
            curr = head;
        } 
        else {
            curr->next = newNode;
            curr = curr->next;
        }
        num /= 10;
    }
    return head;
}

void printList(Node* head){
    while(head){
        std::cout << head->val << " ";
        head = head->next;
    }
    std::cout << "[]"<< std::endl;
}

int main(){
    // Node* head1 = makeIntToList(1238);
    // Node* head2 = makeIntToList(45610);
    // int num = makeListToInt(head1)+makeListToInt(head2);
    // Node* head = makeIntToList(num);
    // printList(head);
    return 0;
}