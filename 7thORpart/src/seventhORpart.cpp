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
	void one();
	void two(second &obj1);
	void add(second &obj1);


};

void second::one(){
	Node* ptr;
	ptr = head;
	while(ptr != NULL){
		if (ptr->data == '0'){
			ptr->data = '1';
		}
		else{
			ptr->data = '0';
		}
		cout<< ptr->data <<"";
		ptr = ptr->next;

	}
}
void second :: two(second &obj1){

}

void second :: add(second &obj1){
	Node* ptr;
	Node* ptr1;
	Node* ptr2;
	char carry = '0';
	second obj2;
	ptr = head;
	ptr1 = obj1.head;
	ptr2 = obj2.head;
	while(ptr != NULL || ptr1 != NULL){
		if(ptr->data == '1' && ptr1->data == '1'){
			if(carry == '0'){
				ptr2->data = '0';
			}
			else{
				ptr2->data = '1';
			}
			carry = '1';
		}
		else if((ptr->data == '0' && ptr1->data == '1') || (ptr->data == '1' && ptr1->data == '0')){
			if(carry == '0'){
				ptr2->data = '1';
			}
			else{
				ptr2->data = '0';

			}
			carry = '0';
		}
		else{
			if(carry == '0'){
				ptr2->data = '0';
			}
			else{
				ptr2->data = '1';
			}
			carry = '0';
		}

	}
	while(ptr2 != NULL){
		cout<< ptr2->data <<"";
		ptr2 = ptr2->next;
	}
	obj2.display();

}


void second::insert(char newdata) {
	   Node* newnode = new Node;
	   newnode->data = newdata;
	   newnode->prev = NULL;
	   newnode->next = head;
	   if(head != NULL)
	   head->prev = newnode ;
	   head = newnode;
}

void second:: display() {
   Node* ptr;
   ptr = head;
   while(ptr != NULL) {
      cout<< ptr->data <<"";
      ptr = ptr->next;
   }
}

int main() {
	second obj;

	int n;
	cout<<"enter digits in binary string"<<endl;
	cin>>n;

	for(int i = 0;i<n;i++){
		char a;
		cout<<"enter digit"<<endl;
		cin>>a;
		obj.insert(a);
	}
	cout<<"string is"<<endl;
	obj.display();
	cout<<endl;

	int l;
	cout<<"Enter 1 to get ones complement\n"
			" Enter 2 to get twos complement\n"
			" Enter 3 to add two binary no. \n"<<endl;

	cin>>l;
	if(l == 1){
		obj.one();
	}
// 	if(l == 2){
// 		second obj1;
//

// 		obj.two(obj1);
// 	}
	if(l == 3){
		second obj1;
		int m;
			cout<<"enter digits in binary string of second "<<endl;
			cin>>m;

			for(int i = 0;i<m;i++){
				char a;
				cout<<"enter digit"<<endl;
				cin>>a;
				obj1.insert(a);
			}
			cout<<"string is"<<endl;
			obj1.display();
			cout<<endl;
		obj.add(obj1);
	}


	return 0;
}
