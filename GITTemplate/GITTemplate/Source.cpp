#include "Source.h"

int Add(int a, int b)
{
	return a+b;
}

int Subtract(int a, int b)
{
	if (a > b)
		return a - b;
	if (a < b)
		return b - a;
	return 0;
}

int Multiply(int a, int b)
{
	return a*b;
}

int divison(int a, int b)
{
	if(b>0)
	{
		return a / b;
	}
	else
	{
		cout << "Error\t" << "Cannot Divide by\t" << a << "\n";
	}
	return 0;
}

void Example()
{
	auto foo = SimplePair<int, double>{ 4,4.536896 };
	cout << foo.first << "\t" << foo.second << "\n";
}
