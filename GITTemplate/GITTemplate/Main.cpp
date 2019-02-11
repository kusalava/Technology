#include "Source.h"

int main()
{
	int a = 5, b = 4;
	vector<int> vac;
	cout << Add(a, b) << "\n";
	cout << Subtract(a, b) << "\n";
	cout << Multiply(a, b) << "\n";
	cin >> a >> b;
	cout << divison(a, b) << "\n";
	Example();
	UseNewFeature();
	cout<<"Major branch"<<"\n";
	cout << "Program Executed Successfully\n";
	for(int i=0;i<100;i++)
		vac.push_back(i);
	cout<<"Size of vac is\t"<<vac.size()<<"\n";
	system("pause");
	return 0;
}
