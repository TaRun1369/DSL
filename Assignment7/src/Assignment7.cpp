//============================================================================
// Name        : linkedlist.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include<stdlib.h>
using namespace std;

class Node{
public:
	   char data;
	   struct Node *prev;
	   struct Node *next;
};

class second{
public:
	Node* head,* tail;
	second(){
		head = NULL;
	}
	void insert(char newdata);
	void display();


};




void second::insert(char newdata) {
	   struct Node* newnode = new Node;
	   newnode->data = newdata;
	   newnode->prev = NULL;
	   newnode->next = head;
	   if(head != NULL)
	   head->prev = newnode ;
	   head = newnode;
}

void second:: display() {
   struct Node* ptr;
   ptr = head;
   while(ptr != NULL) {
      cout<< ptr->data <<" ";
      ptr = ptr->next;
   }
}

int main() {
	second obj;
	obj.insert('0');
	obj.insert('1');
	obj.display();
	return 0;
}
