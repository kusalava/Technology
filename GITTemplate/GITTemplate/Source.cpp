#include "Source.h"

int Add(int a, int b)
{
	return a+b;
}

int Subtract(int a, int b)
{
	//It subtracts the higher value from lower value
	if (a > b)
		return a - b;
	if (a < b)
		return b - a;
	return 0;
}

int Multiply(int a, int b)
{
	//Multiplication of two variables
	return a*b;
}

int divison(int a, int b)
{
	// It checks divided by zero error
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

void NewFeature(int&& a)
{
	cout << "This is only R-value" << "\n";
	cout << "It doesn't allow L-values\n";
	cout << "The given value R-value is " << a << "\n";

}

void UseNewFeature()
{
	int b = 10;
	//NewFeature(b);  //It gives an error because it takes only r-values
	NewFeature(10);  //It will executes
	NewFeature(b + 20); //This also execute

}
