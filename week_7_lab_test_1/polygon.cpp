#include <iostream>
#include<bits/stdc++.h>
#include <vector>
#include <cmath>
using namespace std;

class Point
{
public:
    double x;
    double y;

public:
    Point()
    {
        x =0;
        y = 0;
    }
    ~Point() {}

    void setPoint(double x_value, double y_value){
        x=x_value;
        y=y_value;
    }
};

class Polygon
{
public:
    vector<Point> vertices;

public:
    Polygon(int number = 0)
    {
        vertices.resize(number);
    }

    ~Polygon()
    {
        vertices.clear();
    }

    void readPolygon(vector<double> xarr, vector<double> yarr)
    {
        int j = 0;
        for (int i = 0; i < vertices.size(); i++)
        {
            vertices[i].setPoint(xarr[j],yarr[j]);
            j++;
        }
    }

    void setNumberofVertices(int number)
    {
        vertices.clear();
        vertices.resize(number);
    }

    void print()
    {
        for (int i = 0; i < vertices.size(); i++)
        {
            cout << "vertex " << i << ":" << vertices[i].x << "," << vertices[i].y << endl;
        }
    }

    double CalculateAngle(Point first, Point second, Point third)
    {
        double slope1 = (second.y - first.y) / (second.x - first.x);
        double slope2 = (third.y - second.y) / (third.x - second.x);

        double angle = (slope2 - slope1) / (1 + (slope2 * slope1));
        angle = (angle > 0 ? angle : -angle);

        return angle;
    }

    bool CheckConvex()
    {
        bool check = true;
        double value = 0;
        for (int i = 0; i < vertices.size() - 2; i++)
        {
            int j = i + 1;
            int k = j + 1;

            value = CalculateAngle(vertices[i], vertices[j], vertices[k]);
            if (value > 180)
            {
                check = false;
                break;
            }
        }

        value = CalculateAngle(vertices[vertices.size() - 2], vertices[vertices.size() - 1], vertices[0]);
        if (value > 180)
        {
            check = false;
        }

        value = CalculateAngle(vertices[vertices.size() - 1], vertices[0], vertices[1]);
        if (value > 180)
        {
            check = false;
        }

        return check;
    }

    double LengthofSide(Point first, Point second)
    {
        return sqrt((first.x - second.x) * (first.x - second.x) + (first.y - second.y) * (first.y - second.y));
    }

    double areaofSingleTriangle(Point first, Point second, Point third)
    {
        double length_a = LengthofSide(first, second);
        double length_b = LengthofSide(third, second);
        double length_c = LengthofSide(first, third);
        // cout<<"jk"<<length_a<<"jk"<<length_b<<"jk"<<length_c<<endl;

        double length_s = (length_a + length_b + length_c) / 2;
        // return 0;
        // cout<<"dhfdbhfd"<<sqrt(length_s * (length_s - length_a) * (length_s - length_b) * (length_s - length_c));

        return sqrt(length_s * (length_s - length_a) * (length_s - length_b) * (length_s - length_c));
    }

    double CalculateArea()
    {
        Point fixed_point = vertices[0];

        double final_area = 0;

        for (int i = 1; i < vertices.size() - 1; i++)
        {
            int j = i + 1;

            final_area += areaofSingleTriangle(fixed_point, vertices[i], vertices[j]);
            // cout<<"fsdgahsvhkfs:"<<final_area;
        }

        return final_area;
    }
};

int main()
{  
    int n;
    cout << "Enter the number  of sides";
    cin >> n;

    Polygon poly;
    poly.setNumberofVertices(n);

    vector<double> xarr;
    vector<double> yarr;

    cout << "Enter the coordinates" << endl;

    for (int i = 0; i < n; i++)
    {
        double x, y;
        cin >> x;
        cin >> y;

        xarr.push_back(x);
        yarr.push_back(y);
    }
    poly.readPolygon(xarr, yarr);
    // poly.print();

    bool check_convex = poly.CheckConvex();
    if (check_convex)
    {
        cout << "The given polygon is Convex" << endl;

        cout << "The area of the polygon is:" << poly.CalculateArea();
    }
}