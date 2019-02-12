#include "Source.h"

int main()
{
	int a = 5, b = 4;
	cout << Add(a, b) << "\n";
	cout << Subtract(a, b) << "\n";
	cout << Multiply(a, b) << "\n";
	cin >> a >> b;
	cout << divison(a, b) << "\n";
	Example();
	Example2();
	cout << "Program Executed Successfully\n";

	std::getchar();
	return 0;
}