#include "stdafx.h"
#include "EmployeeManagement.cpp"

#define TEST_CASE_DIRECTORY GetDirectoryName(__FILE__)
using namespace System;
using namespace System::Text;
using namespace System::Collections::Generic;
using namespace Microsoft::VisualStudio::TestTools::UnitTesting;
std::ofstream LogFile;

namespace EmployeeManagementSystem_MDM_Test
{
	[TestClass]
	public ref class EmployeeManagement_Testing 
	{
	private:
		TestContext^ testContextInstance;

	public: 
		/// <summary>
		///Gets or sets the test context which provides
		///information about and functionality for the current test run.
		///</summary>
		property Microsoft::VisualStudio::TestTools::UnitTesting::TestContext^ TestContext
		{
			Microsoft::VisualStudio::TestTools::UnitTesting::TestContext^ get()
			{
				return testContextInstance;
			}
			System::Void set(Microsoft::VisualStudio::TestTools::UnitTesting::TestContext^ value)
			{
				testContextInstance = value;
			}
		};

			[TestInitialize]
			void TestInitialize()
			{
				char* testName = (char*)Marshal::StringToHGlobalAnsi(TestContext->TestName).ToPointer();
				LogFile << "Test Case " << testName << " Started Executing" << std::endl;
				Marshal::FreeHGlobal((IntPtr)testName);
			}

			[TestCleanup]
			void TestCleanup()
			{
				char* testName = (char*)Marshal::StringToHGlobalAnsi(TestContext->TestName).ToPointer();
				LogFile << "Test Case " << testName << " Completed Executing" << std::endl;
				Marshal::FreeHGlobal((IntPtr)testName);
			}
			
			[TestMethod]
			void LoadAndProcessDetails_Test()
			{
				ifstream infile;
				int i = 0;
				size_t n = 9;
				VEMPLOYEE Expectedemployee;
				employee_rec    emp_Test;
				infile.open("Output_Expected.txt",ios::in);
			    if (!infile)
			    exit(1);

				while (!infile.eof())
				{
					infile >> emp_Test.name >>  emp_Test.department >> emp_Test.salary;

					Expectedemployee.push_back(emp_Test);
				}

				infile.close();				
				
				VEMPLOYEE inc1;
				employee_rec emp1;
				inc1.LoadAndProcessDetails(emp1, "Input.txt", 10);
				ofstream outfile;
				outfile.open("Class_size.txt", ios::out);
				if (!outfile)
				exit(1);
				outfile << "Expected is\t" << Expectedemployee.size() << endl;
				outfile << "From program\t" << Actualemployee.size() << endl;
				outfile.close(); 
				/*
				Recursive test starts
				It compares atual values and negitive values
				*/ 
				VEMPLOYEE NegitiveTest;
				employee_rec dummy_emp = { "name","value",1.6 };
				NegitiveTest.push_back(dummy_emp);

				if( (inc1.compareClass(Expectedemployee, Actualemployee))==true)
				{
				Assert::AreEqual(Expectedemployee.size(), Actualemployee.size());
				Actualemployee.clear();
				Assert::AreNotEqual(NegitiveTest.size(), Actualemployee.size());
				}
				else
				{
					Actualemployee.clear();
					Assert::Fail();
				}
		};
	};
}
