/**
 * Assignment 1: Modular C Programming
 * Name:Sumit Kumar
 * Roll No.-22CS30056
 * Course:Software Engineering Laboratory
 * @file social.h
 * @brief This is the header file for the social.c file
 * @details This file contains all the functions and the structures used in the social.c file
 * @date 25/01/2024
 * @version 1.0
 * @bug None
 * @warning None
**/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// The following are the global variables
#define BASIC_LENGTH 100
#define MIN_LENGTH 30
#define MAX_LENGTH 10000
#define NUMBER_OF_POSTS 3

// this variable defines the number of nodes of each type
#define NUMBER_OF_PEOPLE 10

// this variable defines the number of members of in each node which can be linked
#define NUMBER_OF_MEMBERS 10

// This is the id of the node variable from which d to each node is assigned
// All the functions used in this program require this variable as a parameter
int project_id = 1;

//these varaibles keep track of the number of nodes of each type in the database created
int count_individuals = 0;
int count_groups = 0;
int count_business = 0;
int count_organisations = 0;

// A point to store location in(x,y) format
typedef struct point
{
    double x;
    double y;
} point;

// This is the structure of the node of the individual
typedef struct each_node_individual
{
    char type[BASIC_LENGTH];
    int id;
    char name[MIN_LENGTH];
    int creation_date;
    int birthday;
    char posted_content[NUMBER_OF_POSTS][MAX_LENGTH];

} each_node_individual;

// This is the structure of the node of the group
typedef struct each_node_group
{
    char type[BASIC_LENGTH];
    int id;
    char name[MIN_LENGTH];
    int creation_date;
    char posted_content[NUMBER_OF_POSTS][MAX_LENGTH];

    struct each_node_individual *individual_member_list;
    int individual_member_count;

    struct each_node_business *business_member_list;
    int business_member_count;

} each_node_group;

// This is the structure of the node of the business
typedef struct each_node_business
{
    char type[BASIC_LENGTH];
    int id;
    char name[MIN_LENGTH];
    int creation_date;
    char posted_content[NUMBER_OF_POSTS][MAX_LENGTH];

    point location;
    struct each_node_individual *individual_member_list;
    int individual_member_count;

    struct each_node_individual *owners_list;
    int owners_count;

} each_node_business;

// This is the structure of the node of the organisation
typedef struct each_node_organisations
{
    char type[BASIC_LENGTH];
    int id;
    char name[MIN_LENGTH];
    int creation_date;
    char posted_content[NUMBER_OF_POSTS][MAX_LENGTH];

    point location;
    struct each_node_individual *individual_member_list;
    int individual_member_count;

} each_node_organisations;

// This is the function for adding the data to the individual node
void individual_data_addition(each_node_individual *individual_data);

// This is the function for adding the data to the group node
void group_data_addition(each_node_group *group_data);

// This is the function for adding the data to the business node
void business_data_addition(each_node_business *business_data);

// This is the function for adding the data to the organisation node
void organisation_data_addition(each_node_organisations *organisation_data);

// This is the function for printing the data of the individual node
void individual_data_printing(each_node_individual *individual_data);

// This is the function for printing the data of the group node
void group_data_printing(each_node_group *group_data);

// This is the function for printing the data of the business node
void business_data_printing(each_node_business *business_data);

// This is the function for printing the data of the organisation node
void organisation_data_printing(each_node_organisations *organisation_data);

// This is the function for printing the data of the individual node
void delete_individual(each_node_individual *individual_data, int id);

// This is the function for printing the data of the group node
void delete_group(each_node_group *group_data, int id);

// This is the function for printing the data of the business node
void delete_business(each_node_business *business_data, int id);

// This is the function for printing the data of the organisation node
void delete_organisation(each_node_organisations *organisations_data, int id);

// this is function for searching and printing the data if it matches the birthday
void search_by_birthday(each_node_individual *individual_data, int birthday);

// this is function for searching and printing the data if it matches the type of the node
void search_by_type(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data);

// this is function for searching and printing the data if it matches the name of the node
void search_by_name(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data);

// this is function for searching and printing the data if it matches the id of the node
void *search_by_id(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data, int search_id);

// this is the function for creating the posts of the nodes
void create_post(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data);

// this is the function for  searching and printing the posts of the nodes
void search_by_post(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data);

// this is the function for adding the the 1_hop links to the node
void add_1_hop_node(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data);

// this is the function for printing the 1_hop links to the node
void print_1_hop_node(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data);

// this is the function to display the content of the node by id
void display_content_by_id(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data, int search_id);

// this is the  function to display the content of a node linke by another node
void display_content_linked_to_node(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data);

// this is the function to add owners to the business
void add_owners_to_business(each_node_individual *individual_data, each_node_business *business_data);

// this is the function to printed the content of the linked individuals
void print_linked_individuals(each_node_individual *individual_data, each_node_group *group_data, each_node_organisations *organisations_data);
