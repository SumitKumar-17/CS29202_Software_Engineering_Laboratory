#include "VectorDataset.h"
#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <queue>
#include <chrono> // include the chrono library to measure the time taken to find the nearest neighbors
using namespace std;
// The kNearestNeighbors function takes a VectorDataset, a DataVector, and an integer k as arguments and returns a VectorDataset.
// It finds the k nearest neighbors of the given DataVector in the given VectorDataset using the Euclidean distance metric.
// It uses the getVector method of the VectorDataset class to access the DataVector objects in the dataset.
// It uses the dist method of the DataVector class to calculate the distance between two vectors.
// It uses the sort function from the algorithm library to sort the distances in ascending order.
// It uses the push_back method of the VectorDataset class to add the k nearest neighbors to the result dataset.
// It returns the result dataset.

// The kNearestNeighbors function is defined here. It takes a VectorDataset, a DataVector, and an integer k as arguments and returns a VectorDataset.
VectorDataset kNearestNeighbors(VectorDataset &dataset, DataVector &testVector, int k)
{
    // check if the dataset is empty. If it is, print an error message and return an empty dataset.
    if (dataset.size() == 0)
    {
        cout << "Error: empty dataset" << endl;
        return VectorDataset();
    }

    else{
        // Create a priority queue to store the distances and indices of the vectors in the dataset.
        // The priority queue is a max-heap, so we use the greater comparator to make it a min-heap.
        priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>> pq;

        // Iterate through the vectors in the dataset.
        for (int i = 0; i < dataset.size(); i++)
        {
            // Calculate the distance between the test vector and the current vector in the dataset.
            double distance = testVector.dist(dataset.getVector(i));

            // If the priority queue has fewer than k elements, add the current distance and index to the queue.
            if (pq.size() < k)
            {
                pq.push(make_pair(distance, i));
            }
            else
            {
                // If the priority queue has k elements, compare the current distance with the largest distance in the queue.
                // If the current distance is smaller, remove the largest distance from the queue and add the current distance.
                if (distance < pq.top().first)
                {
                    pq.pop();
                    pq.push(make_pair(distance, i));
                }
            }
        }

        // Create a VectorDataset to store the k nearest neighbors.
        VectorDataset result;

        // Add the k nearest neighbors to the result dataset.
        while (!pq.empty())
        {
            result.push_back(dataset.getVector(pq.top().second));
            pq.pop();
        }

        // Return the result dataset.
        return result;
    }
}

// The main function is the entry point of the program. It takes no arguments and returns an integer.
// It reads a dataset from a file and a test vector from the user.
// It finds the k nearest neighbors of the test vector in the dataset using the kNearestNeighbors function.
// It prints the nearest neighbors to the console.
// It measures the time taken to find the nearest neighbors and prints it to the console.
// It returns 0 to the operating system to indicate successful execution of the program.
// The main function is defined here.

// The main function is the entry point of the program. It takes no arguments and returns an integer.
int main()
{
    VectorDataset dataset;                           // create a VectorDataset object to store the dataset
    cout << "Your Dataset is being read..." << endl; // print a message to indicate that the dataset is being read
    // dataset.readDataset("2.csv");                    // read the dataset from a file
    dataset.readDataset("fmnist-train.csv");
    cout << "Dataset read successfully!" << endl; // print a message to indicate that the dataset has been read successfully

    // Ask for the dimension of the test vector from the user.
    // The dimension should be equal to the number of columns in the dataset.
    int dimension=784;
    // cout << "Enter the dimension of the test vector.";
    // cout << "The dimension should be equal to the number of columns in the dataset:" << endl;
    // cin >> dimension;

    // Create a DataVector object to store the test vector.
    // The dimension of the test vector is set to the value entered by the user.
    // The components of the test vector are set by the user.
    // The components of the test vector are set to 5.8 for testing purposes.
    // DataVector testVector(dimension);
    // cout << "Enter the values of the test vector:" << endl;

    // reading Test Vector from file
    VectorDataset testvectorDataset;
    testvectorDataset.readDataset("fmnist-test.csv");

    // Ask for the components of the test vector from the user.
    // The components are set using the setComponent method of the DataVector class.
    // for (int i = 0; i < dimension; i++)
    // {
    //     // cout << "Enter the value of the " << i + 1 << "th dimension: ";
    //     // double x;
    //     // cin >> x;
    //     // testVector.setComponent(i, x);
    //     testVector.setComponent(i, 5.8);
    // }

    // Ask for the number of nearest neighbours from the user.
    // The number of nearest neighbours is set to the value entered by the user.
    int k;
    cout << "Enter the value of k i.e. the number of nearest neighbours you want to find: ";
    cin >> k;

    // Find the k nearest neighbors of the test vector in the dataset using the kNearestNeighbors function.
    // The time taken to find the nearest neighbors is measured using the chrono library.
    // The nearest neighbors are printed to the console.
    // The time taken to find the nearest neighbors is printed to the console.
    int number;
    cout<<"Enter the number of test vectors you want to test:";
    cin>>number;
    cout << "Finding the nearest neighbours..." << endl;

    auto start = chrono::high_resolution_clock::now();
    VectorDataset nearestNeighbors;


    if(number>testvectorDataset.size()){
        cout << "Error: Number of test vectors is greater than the size of the dataset" << endl;
        return 0;
    }
   

    for (int i = 0; i < number; i++)
    {   
        // cout<<"i:fjf";
        DataVector testVector = testvectorDataset.getVector(i);
        nearestNeighbors = kNearestNeighbors(dataset, testVector, k);
    }
    // DataVector testVector(dimension);

    auto end = chrono::high_resolution_clock::now();
    cout << "Nearest neighbours found successfully!" << endl;

    cout << "Nearest neighbour search took: " << chrono::duration_cast<chrono::milliseconds>(end - start).count() << " ms" << endl;

    // This statement can be uncommented to check the test vector for the dataset
    //  cout << "Test Vector: ";
    //  testVector.print();

    // Print the nearest neighbors to the console.
    // cout << "Nearest Neighbors are:" << endl;
    // for (int i = 0; i < nearestNeighbors.size(); ++i)
    // {
    //     cout << "Nearest Neighbour " << i + 1 << ": ";
    //     nearestNeighbors.getVector(i).print(); // print the nearest neighbors
    //     cout << endl;
    // }

    return 0;
}
