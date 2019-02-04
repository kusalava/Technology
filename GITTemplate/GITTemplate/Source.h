#pragma once
// This is the headr file for Git example project
#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;

int Add(int a,int b);

int Subtract(int a, int b);

int Multiply(int a,int b);

int divison(int a, int b);
template<typename Tfirst , typename Tsecond>
struct SimplePair
{
	Tfirst first;
	Tsecond second;
	SimplePair(Tfirst f, Tsecond s) :first{ f }, second{ s }
	{
	};
};
void Example();
