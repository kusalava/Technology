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
	try
	{
		return a / b;
	}
	catch (int a)
	{
		cout << "Error\t" << "Cannot Divide by\t" << a << "\n";
	}
	return 0;
}
