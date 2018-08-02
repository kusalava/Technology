#pragma once
#pragma once
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<fstream>
#include <cstdio>
#include<algorithm>
#include<iterator>
#include<iomanip>
#define SIZEOF(array)	(int)sizeof(array)
#define sort  stable_sort
using namespace std;

struct employee_rec
{
	char name[30];
	char department[15];
	double salary;
};

class VEMPLOYEE : public vector<employee_rec>
{
public:
	VEMPLOYEE();
	~VEMPLOYEE();


	void InitEmployee(employee_rec& emp);
	//This method loads the person details from input.txt file
	void LoadAndProcessDetails(employee_rec& emp, char* Inputfile, double value);
	//This method increments the particular percentage of a salary
	void IncrementSalary(employee_rec& emp, double value);
	//This method writes the Results to output file
	void WriteDetails(employee_rec& emp, char* Outputfile);
	void PrintToOutFile(ofstream& outfile, const employee_rec* w);
	ifstream& ReadFile(ifstream& infile, employee_rec& emp);
	ifstream& VEMPLOYEE::ReadExpectedFile(ifstream& infile, employee_rec& emp);
	void VEMPLOYEE::LoadProcessExpectedDetails(employee_rec& emp, char* Inputfile);
	static inline bool Cmpemp(const employee_rec& x, const employee_rec& y);
	bool compareClass(const VEMPLOYEE& left, const VEMPLOYEE& right);
};