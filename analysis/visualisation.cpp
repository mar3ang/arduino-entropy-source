#include <iostream>
#include <fstream>
#include <vector>


using namespace std;

int main() {
    ifstream file("data/0Rsamples.txt");

    if (!file.is_open()) {
        cout << "Could not open file.\n";
        return 1;
    }

    vector<int> frequency(1024, 0); // since the Arduino ADC values go from 0 to 2^10, we need a vector of size 1024 to count the frequency of each possible value.

    int sample;

    while (file >> sample) {
        if (sample >= 0 && sample <= 1023) {
            frequency[sample]++;
        }
    }

    // Print histogram
    for (int i = 0; i < 1024; i++) {
        if (frequency[i] > 0) {
            cout << i << " : ";

            // Draw stars
            for (int j = 0; j < frequency[i]; j++) {
                cout << "*";
            }

            cout << " (" << frequency[i] << ")" << endl;
        }
    }

    return 0;
}