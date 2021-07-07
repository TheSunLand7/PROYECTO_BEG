#include <iostream>

/*TUPLES
#include <tuple>

int main()
{
	//Declare a tuple
	std::tuple<int, std::string> person(20, "Joe");
	//Access the elements:
	std::cout << std::get<1>(person) << std::endl;  //Inside <> index.
	//Modify an element:
	std::get<1>(person) = "Benja";

	//An empty tuple
	std::tuple<int,char, bool> patient;
	//Add elements
	patient = std::make_tuple(24, 'M', true);

	//Another way to declare a tuple
	// std::tuple<int, std::string> person1 = std::make_tuple(21, "Tim")

	//Swap tuples. Tuples have to be of the same type.
	std::tuple<int, char> tuple1 = std::make_tuple(21, 'M');
	std::tuple<int, char> tuple2 = std::make_tuple(18, 'F');

	tuple1.swap(tuple2);
	std::cout << std::get<1>(tuple1);

	//Decompose a tuple into single variables with 'tie'
	std::tuple<int, char> tuple1 = std::make_tuple(21, 'M');
	int age;
	char gender;

	std::tie(age, gender) = tuple1;

	std::cout << age << std::endl;
	std::cout << gender << std::endl;

	//Cocatenating tuples
	std::tuple<int, char> tuple1 = std::make_tuple(21, 'M');
	std::tuple<float, std::string> tuple2 = std::make_tuple(15.8f, "Hi dad!");

	std::tuple<int, char, float, std::string> tuple3 = std::tuple_cat(tuple1, tuple2); //Return to another tuple.

	std::cout << std::get<1>(tuple3) << std::endl;

	std::cin.get();
	return 0;
}
*/

/*MAPS --> It is almost similar to dictionaries in Python
#include <map>

int main() {

	//Declare a map
	std::map<char, int> mymap {
		{'V', 2},
		{'L', 4},
		{'A', 9}
	};

	/Access the elements. If we trid to access to a value that does not exist in the map,
	//  this returns 0.
	std::cout << mymap['A'] << std::endl;
	//Add elements
	mymap['u'] = 5;
	mymap.insert(std::pair<char, int>('p', 1));
	//Erase elements
	mymap.erase('V');
	std::cout << mymap['V'] << std::endl;
	//Remove all in the map
	mymap.clear();
	//Check if the map is empty. 1 -->empty, 0 --> not empty.
	std::cout << mymap.empty() << std::endl;

	//Iterate through maps
	std::map<char, int>::iterator itr;
	for (itr = mymap.begin(); itr != mymap.end(); ++itr) {
		std::cout << itr->first << ": " << itr->second << std::endl;
	}

	std::string test = "Hola amigo, how have you been?, ttml. chronos, mangos.";
	std::map<char, int> mymap;
	std::map<char, int>::iterator itr;

	for (int i = 0; i < test.size(); ++i) {
		char letter = test[i];
		if (mymap.find(letter) == mymap.end()) {
			mymap[letter] = 0;
		}
		++mymap[letter];
	}

	for (itr = mymap.begin(); itr != mymap.end(); ++itr) {
		std::cout << itr->first << ": " << itr->second << std::endl;
	}

	std::cin.get();
	return 0;
}
*/

/*VECTORS
#include <vector>

int main() {

	//Declare a vector
	std::vector<int> vec1 {2, 3, 5};
	//Access elements
	std::cout << vec1[2] << std::endl;
	//First element
	std::cout << vec1.front() << std::endl;
	//Last element
	std::cout << vec1.back() << std::endl;

	//How many elemnts can hold
	std::cout << vec1.capacity() << std::endl;
	//Add elements at the end
	vec1.push_back(9);
	//Delete the last element
	vec1.pop_back();

	//If we add an element the capacity increase, but if we delete the capacity
	// does not decrease, so the vector is taking the capacity increased yet.
	//To free memory we have to use 'vec1.shrink_to_fit();'

	//Insert element at the beginning but we can insert in whatever position by addind it
	//the number of position from the beginning.
	vec1.insert(vec1.begin(), 0);  //vec1.insert(vec1.begin()+1, 7);

	//Erase an element
	vec1.erase(vec1.begin()); //vec1.erase(vec1.begin()+2);


	std::cin.get();
	return 0;
}*/

//SET
#include <string>
#include <set>

int main() {
	std::string test = "I am not from around here, I am afraid I cannot help you!";
	std::string find = "No problem!";
	std::set<char> findLetters;

	for (int i = 0; i < find.size(); ++i) {
		char letter = find[i];
		findLetters.insert(letter); //No problem
	}

	for (int i = 0; i < test.size(); ++i) {
		char letter = test[i];
		findLetters.erase(letter);
	}

	if (findLetters.size() > 0) {
		std::cout << "NO! it does not have all letters!" << std::endl;
	} else {
		std::cout << "YES! it does!" << std::endl;
	}

	std::cin.get();
	return 0;
}
