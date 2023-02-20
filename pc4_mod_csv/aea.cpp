#include <bits/stdc++.h>
using namespace std;

int main() {
    // open a file in read mode
    ifstream infile;
    infile.open("datos.csv");
    // check if the file is open
    if (!infile.is_open()) {
        cout << "Error opening file" << endl;
        exit(1);
    }

    // create a new file to write the modified data
    ofstream outfile;
    outfile.open("datos_mod.csv");

    string line;
    while (getline(infile, line)) {
        // modify a comma to a semicolon line per line
        replace(line.begin(), line.end(), ',', ';');
        // print the modified line
        // write the new line to a new file
        outfile << line << endl;
    }
}