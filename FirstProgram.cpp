#include<iostream>
using namespace std;

int add(int a,int b)
{
	return a+b;
}

int sub(int a,int b)
{
	return a - b;
}

int mul(int a,int b)
{
	return a*b;
}

float div(int a,int b)
{
	return a/b;
}

int main()
{
	int a=10,b = 5;
	
	cout<<"Addition of \t"<<a<<"\t"<<b<<" is"<<add(a,b)<<"\n";
 	cout<<"Subtraction  of \t"<<a<<"\t"<<b<<" is"<<sub(a,b)<<"\n";
	cout<<"Multiplication of \t"<<a<<"\t"<<b<<" is"<<mul(a,b)<<"\n";
	cout<<"Division of \t"<<a<<"\t"<<b<<" is"<<div(a,b)<<"\n";

	cout<<"Program Execution is completed \n";
	return 0;


}
