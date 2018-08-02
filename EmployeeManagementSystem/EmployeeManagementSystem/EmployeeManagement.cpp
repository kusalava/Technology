#include"EmployeeManagement.h"

VEMPLOYEE::VEMPLOYEE()
{

}
VEMPLOYEE::~VEMPLOYEE()
{

}

VEMPLOYEE Actualemployee;
employee_rec emp;
VEMPLOYEE MyTestvector;
vector<employee_rec> xyz, xyy;
void VEMPLOYEE::InitEmployee(employee_rec& emp)
{
	strcpy_s(emp.department, " ");
	strcpy_s(emp.name, " ");
	emp.salary = 0.0;
}
ifstream& VEMPLOYEE::ReadFile(ifstream& infile, employee_rec& emp)
{
	infile >> emp.name >> emp.department >> emp.salary;
	return infile;
}

ifstream& VEMPLOYEE::ReadExpectedFile(ifstream& infile, employee_rec& emp)
{
	infile >> emp.name >> emp.department >> emp.salary;
	return infile;
}
void VEMPLOYEE::LoadAndProcessDetails(employee_rec& emp, char* Inputfile, double value)
{
	int i = 0;
	int ops = 0;
	ifstream infile;
	InitEmployee(emp);
	infile.open(Inputfile, ios::in);
	while (ReadFile(infile, emp))
	{  
		++ops;
		IncrementSalary(emp, value);
		Actualemployee.push_back(emp);
	}
	std::sort(Actualemployee.begin(), Actualemployee.end(), Cmpemp);
	infile.close();
	//std::sort(MyTestvector.begin(), MyTestvector.end(), Cmpemp);
}
void VEMPLOYEE::LoadProcessExpectedDetails(employee_rec& emp1, char* Inputfile)
{
	ifstream infile;
	infile.open(Inputfile, ios::in);
	if (!infile)
		exit(1);
	while (ReadExpectedFile(infile, emp1))
	{
		MyTestvector.push_back(emp1);
	}
	infile.close();
}
bool VEMPLOYEE::Cmpemp(const employee_rec& x, const employee_rec& y)
{
	int n;
	n = strcmp(x.department, y.department);
	if (n<0) return 1;
	if (n == 0)
	{
		n = strcmp(x.name, y.name);
		if (n<0) return 1;
		if (n == 0 && x.salary < y.salary) return 1;
	}
	return 0;
}

void VEMPLOYEE::IncrementSalary(employee_rec& emp, double value)
{
	emp.salary += ((emp.salary / 100) * value);
}

void VEMPLOYEE::WriteDetails(employee_rec& emp, char* Outputfile)
{
	vector<employee_rec>::iterator iter1;
	ofstream outfile;
	outfile.open(Outputfile, ios::out);
	for (iter1 = Actualemployee.begin(); iter1 != Actualemployee.end(); ++iter1)
	{

		PrintToOutFile(outfile, &*iter1);
	}
	    outfile.close();
}

void VEMPLOYEE::PrintToOutFile(ofstream& outfile, const employee_rec* w)
{
	outfile << setw(15) << left << w->name << setw(7) << w->department << setw(7) << w->salary << "\n";
}

///////// applying the compare function ////////
bool VEMPLOYEE::compareClass(const VEMPLOYEE& left, const VEMPLOYEE& right)
{
	vector<employee_rec>::const_iterator leftIt, rightIt;
	leftIt = left.begin();
	rightIt = right.begin();
	bool diff = 1;
	bool nodiff = 1;
	int Record = 1;
	ofstream outfile;
	outfile.open("MissMatchedValues.txt");
	// Account for different length vector instances
	if (left.size() != right.size())
	{
		outfile.open("MissMatchedValues.txt");
		outfile << "Both containeres  are different \n Check Once again \n";
		diff = 0;
		outfile.close();
		return diff;
	}
		while (leftIt != left.end() && rightIt != right.end())
		{
			

			if (&*leftIt != &*rightIt)
			{
				while(left.size()!=right.size())
				
				if (strcmp(rightIt->department, leftIt->department) != 0)
				{
					outfile << "Deparments are not same for employee" << Record << "\n";
					outfile << " Actual Record :--\t" << rightIt->department << "\t" << "Expected Record :--\t" << leftIt->department << "\n\n";
					diff = 0;
				}


				if (strcmp(rightIt->name, leftIt->name) != 0)
				{
					outfile << "Names are different for employee " << Record << "\n";
					outfile << " Actual Record  :--\t" << rightIt->name << "\t" << "Expected Record :--\t" << leftIt->name << "\n\n";
					diff = 0;
				}

				if (rightIt->salary != leftIt->salary)
				{
					outfile << "Salaries are  different for employee " << Record << "\n";
					outfile << "Actual Record  :--\t" << rightIt->salary << "\t" << " Expected Record  :--\t" << leftIt->salary << "\n\n";
					diff = 0;
				}

				leftIt++;
				rightIt++;
				Record++;
			}
			
	}
		outfile.close();
	    return diff;
	
}


int main()
{
	VEMPLOYEE inc;
	double value;
	employee_rec emp1;
	cout << "Enter which percent to increment \n";
	cin >> value;
	inc.LoadAndProcessDetails(emp, "Input.txt", value);
	inc.WriteDetails(emp, "Output.txt");
	inc.LoadProcessExpectedDetails(emp1, "Output_Expected.txt");
	inc.compareClass(Actualemployee, MyTestvector);
	return 0;
}

