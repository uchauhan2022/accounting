#include <bits/stdc++.h>

using namespace std;
int main()
{

int t, j;
int n;
cin>>t;
for(j=0; j<t; j++)
{

  cin>>n; 
  int i;
  int count =0, num;

unordered_map< string, int > frequencyT, frequencyF;

vector<string> X;
vector<int> Y;

for (i = 0; i < n; ++i)
{	
	string temp_x;
	int  temp_y;
	cin>>temp_x;
	cin>>temp_y;
	
	X.push_back(temp_x);
	Y.push_back(temp_y);

}

for (int i = 0; i < n; ++i)
{

	frequencyT[X[i]]=0;

	frequencyF[X[i]]=0; 	

}


for (int i = 0; i < n; ++i)
{

	if(Y[i]) frequencyT[X[i]]++;

	else frequencyF[X[i]]++; 	

}

num= frequencyT.size();

string array[num];
i=0;
for (const auto x: frequencyT )
{
	array[i]=x.first;
	++i;
}


for (int i = 0; i < num; ++i)
{
	if (frequencyT[array[i]]>frequencyF[array[i]]) 
		count+=frequencyT[array[i]];
	else count+=frequencyF[array[i]];
}


cout<<count<<"\n";
}
return 0;
}
