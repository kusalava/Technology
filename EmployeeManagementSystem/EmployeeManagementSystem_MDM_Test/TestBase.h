#pragma once
#include <ostream>
#include <iostream>
#include <fstream>

using namespace System;
using namespace System::Text;
using namespace System::Collections::Generic;
using namespace System::Runtime::InteropServices;
using namespace	Microsoft::VisualStudio::TestTools::UnitTesting;

extern std::ofstream LogFile;

namespace EmployeeSalaryManagementSystem_MDM_Test 
{
	[TestClass]
	public ref class TestBase
	{
	public:

		property TestContext ^ TestContext;

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

	};
}

