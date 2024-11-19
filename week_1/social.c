/**
 * Assignment 1: Modular C Programming
 * Name:Sumit Kumar
 * Roll No.-22CS30056
 * Course:Software Engineering Laboratory
 *Date:15/01/2024
 * @mainpage Social Network
 * @file social.c
 * This file contains the functions for adding, printing, deleting, searching and creating posts and other utility functions for the different types of nodes.
**/

#include "social.h"

// This is the function for adding the data to the individual node
void individual_data_addition(each_node_individual *individual_data)
{
    strcpy(individual_data[count_individuals].type, "individual");
    individual_data[count_individuals].id = project_id;
    project_id++;

    printf("enter the name of the individual:");
    char enter_name[MIN_LENGTH];
    scanf(" %[^\n]%*c", enter_name);
    strcpy(individual_data[count_individuals].name, enter_name);

    printf("enter the creation date of the individual in format ddmmyyyy:");
    int creation_date_initialize;
    scanf("%d", &creation_date_initialize);
    individual_data[count_individuals].creation_date = creation_date_initialize;

    printf("enter the birthday of the individual in format ddmmyyyy:");
    int birthday_initialize;
    scanf("%d", &birthday_initialize);
    individual_data[count_individuals].birthday = birthday_initialize;

    count_individuals++;
    return;
}

// This is the function for printing the data of the individual node
void individual_data_printing(each_node_individual *individual_data)
{

    int n = count_individuals;
    if (n == 0)
    {
        printf("No data present");
        return;
    }

    for (int i = 0; i < n; i++)
    {
        printf("the id is: %d\n", individual_data[i].id);
        printf("the name is: %s\n", individual_data[i].name);
        printf("the creation date is: %d\n", individual_data[i].creation_date);
        printf("the birthday is: %d\n", individual_data[i].birthday);

        printf("Posts:\n");
        for (int j = 0; j < NUMBER_OF_POSTS; j++)
        {
            if (strlen(individual_data[i].posted_content[j]) > 0)
            {
                printf("Post %d: %s\n", j + 1, individual_data[i].posted_content[j]);
            }
        }
        printf("\n");
    }

    return;
}

// This is the function for adding the data to the group node
void group_data_addition(each_node_group *group_data)
{
    strcpy(group_data[count_groups].type, "group");
    group_data[count_groups].id = project_id;
    project_id++;

    printf("enter the name of the group:");
    char enter_name[MIN_LENGTH];
    scanf(" %[^\n]%*c", enter_name);
    strcpy(group_data[count_groups].name, enter_name);

    printf("enter the creation date of the group in format ddmmyyyy:");
    int creation_date_initialize;
    scanf("%d", &creation_date_initialize);
    group_data[count_groups].creation_date = creation_date_initialize;

    group_data[count_groups].individual_member_list = malloc(NUMBER_OF_PEOPLE * sizeof(each_node_individual));
    group_data[count_groups].individual_member_count = 0;

    group_data[count_groups].business_member_list = malloc(NUMBER_OF_PEOPLE * sizeof(each_node_business));
    group_data[count_groups].business_member_count = 0;

    count_groups++;
    return;
}

// This is the function for printing the data of the group node
void group_data_printing(each_node_group *group_data)
{

    int n = count_groups;
    if (n == 0)
    {
        printf("No data present");
        return;
    }

    for (int i = 0; i < n; i++)
    {
        printf("the id is %d:\n", group_data[i].id);
        printf("the name is %s:\n", group_data[i].name);
        printf("the creation date is %d:\n", group_data[i].creation_date);

        printf("Posts:\n");
        for (int j = 0; j < NUMBER_OF_POSTS; j++)
        {
            if (strlen(group_data[i].posted_content[j]) > 0)
            {
                printf("Post %d: %s\n", j + 1, group_data[i].posted_content[j]);
            }
        }
        printf("\n");
    }
    return;
}

// This is the function for adding the data to the business node
void business_data_addition(each_node_business *business_data)
{
    strcpy(business_data[count_business].type, "business");
    business_data[count_business].id = project_id;
    project_id++;

    printf("enter the name of the business:");
    char enter_name[MIN_LENGTH];
    scanf(" %[^\n]%*c", enter_name);
    strcpy(business_data[count_business].name, enter_name);

    printf("enter the creation date of the business in format ddmmyyyy:");
    int creation_date_initialize;
    scanf("%d", &creation_date_initialize);
    business_data[count_business].creation_date = creation_date_initialize;

    double x_position, y_position;
    printf("Enter x position: ");
    scanf("%lf", &x_position);
    printf("Enter y position: ");
    scanf("%lf", &y_position);
    business_data[count_business].location.x = x_position;
    business_data[count_business].location.y = y_position;

    business_data[count_business].individual_member_list = malloc(NUMBER_OF_PEOPLE * sizeof(each_node_individual));
    business_data[count_business].individual_member_count = 0;

    business_data[count_business].owners_list = malloc(NUMBER_OF_PEOPLE * sizeof(each_node_individual));
    business_data[count_business].owners_count = 0;

    count_business++;
    return;
}

// This is the function for printing the data of the business node
void business_data_printing(each_node_business *business_data)
{

    int n = count_business;
    if (n == 0)
    {
        printf("No data present");
        return;
    }

    for (int i = 0; i < n; i++)
    {
        printf("the id is %d:\n", business_data[i].id);
        printf("the name is %s:\n", business_data[i].name);
        printf("the creation date is %d:\n", business_data[i].creation_date);

        printf("Posts:\n");
        for (int j = 0; j < NUMBER_OF_POSTS; j++)
        {
            if (strlen(business_data[i].posted_content[j]) > 0)
            {
                printf("Post %d: %s\n", j + 1, business_data[i].posted_content[j]);
            }
        }
        printf("\n");
    }
    return;
}

// This is the function for adding the data to the organisations node
void organisations_data_addition(each_node_organisations *organisations_data)
{
    strcpy(organisations_data[count_organisations].type, "organisations");
    organisations_data[count_organisations].id = project_id;
    project_id++;

    printf("enter the name of the organisations:");
    char enter_name[MIN_LENGTH];
    scanf(" %[^\n]%*c", enter_name);
    strcpy(organisations_data[count_organisations].name, enter_name);

    printf("enter the creation date of the organisations in format ddmmyyyy:");
    int creation_date_initialize;
    scanf("%d", &creation_date_initialize);
    organisations_data[count_organisations].creation_date = creation_date_initialize;

    double x_position, y_position;
    printf("Enter x position: ");
    scanf("%lf", &x_position);
    printf("Enter y position: ");
    scanf("%lf", &y_position);

    organisations_data[count_organisations].location.x = x_position;
    organisations_data[count_organisations].location.y = y_position;

    organisations_data[count_organisations].individual_member_list = malloc(NUMBER_OF_PEOPLE * sizeof(each_node_individual));
    organisations_data[count_organisations].individual_member_count = 0;

    count_organisations++;
    return;
}

// This is the function for printing the data of the organisations node
void organisations_data_printing(each_node_organisations *organisations_data)
{

    int n = count_organisations;
    if (n == 0)
    {
        printf("No data present");
        return;
    }

    for (int i = 0; i < n; i++)
    {
        printf("the id is %d:\n", organisations_data[i].id);
        printf("the name is %s:\n", organisations_data[i].name);
        printf("the creation date is %d:\n", organisations_data[i].creation_date);

        printf("Posts:\n");
        for (int j = 0; j < NUMBER_OF_POSTS; j++)
        {
            if (strlen(organisations_data[i].posted_content[j]) > 0)
            {
                printf("Post %d: %s\n", j + 1, organisations_data[i].posted_content[j]);
            }
        }
        printf("\n");
    }
    return;
}

// This is the function for deleting the data of the individual node
void delete_individual(each_node_individual *individual_data, int id)
{
    for (int i = 0; i < count_individuals; i++)
    {
        if (individual_data[i].id == id)
        {
            for (int j = i; j < count_individuals - 1; j++)
            {
                individual_data[j] = individual_data[j + 1];
            }
            count_individuals--;
            printf("Individual with ID %d deleted.\n", id);
            return;
        }
    }
    printf("Individual with ID %d not found.\n", id);
    return;
}

// This is the function for deleting the data of the group node
void delete_group(each_node_group *group_data, int id)
{
    for (int i = 0; i < count_groups; i++)
    {
        if (group_data[i].id == id)
        {
            for (int j = i; j < count_groups - 1; j++)
            {
                group_data[j] = group_data[j + 1];
            }
            count_groups--;
            printf("Group with ID %d deleted.\n", id);
            return;
        }
    }
    printf("Group with ID %d not found.\n", id);
    return;
}

// This is the function for deleting the data of the business node
void delete_business(each_node_business *business_data, int id)
{
    for (int i = 0; i < count_business; i++)
    {
        if (business_data[i].id == id)
        {
            for (int j = i; j < count_business - 1; j++)
            {
                business_data[j] = business_data[j + 1];
            }
            count_business--;
            printf("Business with ID %d deleted.\n", id);
            return;
        }
    }
    printf("Business with ID %d not found.\n", id);
    return;
}

// This is the function for deleting the data of the organisations node
void delete_organisation(each_node_organisations *organisations_data, int id)
{
    for (int i = 0; i < count_organisations; i++)
    {
        if (organisations_data[i].id == id)
        {
            for (int j = i; j < count_organisations - 1; j++)
            {
                organisations_data[j] = organisations_data[j + 1];
            }
            count_organisations--;
            printf("Organisation with ID %d deleted.\n", id);
            return;
        }
    }
    printf("Organisation with ID %d not found.\n", id);
    return;
}

// this is function for searching and printing the data if it matches the birthday
void search_by_birthday(each_node_individual *individual_data, int search_birthday)
{
    int find = 0;
    for (int i = 0; i < count_individuals; i++)
    {
        if (individual_data[i].birthday == search_birthday)
        {
            printf("Individual found with birthday %d:\n", search_birthday);
            printf("ID: %d\n", individual_data[i].id);
            printf("Name: %s\n", individual_data[i].name);
            printf("Posts:\n");
            for (int j = 0; j < NUMBER_OF_POSTS; j++)
            {
                printf("Post %d: %s\n", j + 1, individual_data[i].posted_content[j]);
            }
            printf("\n");
            find++;
        }
    }
    if (find == 0)
        printf("No individual found with birthday '%d'.\n", search_birthday);
    return;
}

// this is function for searching and printing the data if it matches the type of the node
void search_by_type(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data)
{
    int search_type = 0;
    printf("Enter the type of the data you want to search for\n Enter 1 for individual\n Enter 2 for group\n Enter 3 for business\n Enter 4 for organisations\n");
    scanf("%d", &search_type);
    if (search_type == 1)
        individual_data_printing(individual_data);
    else if (search_type == 2)
        group_data_printing(group_data);
    else if (search_type == 3)
        business_data_printing(business_data);
    else if (search_type == 4)
        organisations_data_printing(organisations_data);
    else
        printf("Enter the correct choice.");
    return;
}

// this is function for searching and printing the data if it matches the name of the node
void search_by_name(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data)
{
    char search_name[MIN_LENGTH];
    printf("Enter the name of the data you want to search for\n");
    scanf(" %[^\n]%*c", search_name);

    for (int i = 0; i < count_individuals; i++)
    {
        if (strcmp(individual_data[i].name, search_name) == 0)
        {
            printf("Individual found with name '%s':\n", search_name);
            printf("ID: %d\n", individual_data[i].id);
            printf("Name: %s\n", individual_data[i].name);
            printf("Creation Date: %d\n", individual_data[i].creation_date);
            printf("Birthday: %d\n", individual_data[i].birthday);
            printf("Posts:\n");
            for (int j = 0; j < NUMBER_OF_POSTS; j++)
            {
                if (strlen(individual_data[i].posted_content[j]) > 0)
                {
                    printf("Post %d: %s\n", j + 1, individual_data[i].posted_content[j]);
                }
            }
            return;
        }
    }
    for (int i = 0; i < count_groups; i++)
    {
        if (strcmp(group_data[i].name, search_name) == 0)
        {
            printf("Group found with name '%s':\n", search_name);
            printf("ID: %d\n", group_data[i].id);
            printf("Name: %s\n", group_data[i].name);
            printf("Creation Date: %d\n", group_data[i].creation_date);
            printf("Posts:\n");
            for (int j = 0; j < NUMBER_OF_POSTS; j++)
            {
                if (strlen(group_data[i].posted_content[j]) > 0)
                {
                    printf("Post %d: %s\n", j + 1, group_data[i].posted_content[j]);
                }
                return;
            }
        }
    }
    for (int i = 0; i < count_business; i++)
    {
        if (strcmp(business_data[i].name, search_name) == 0)
        {
            printf("Business found with name '%s':\n", search_name);
            printf("ID: %d\n", business_data[i].id);
            printf("Name: %s\n", business_data[i].name);
            printf("Creation Date: %d\n", business_data[i].creation_date);
            printf("Posts:\n");
            for (int j = 0; j < NUMBER_OF_POSTS; j++)
            {
                if (strlen(business_data[i].posted_content[j]) > 0)
                {
                    printf("Post %d: %s\n", j + 1, business_data[i].posted_content[j]);
                }
            }
            return;
        }
    }
    for (int i = 0; i < count_organisations; i++)
    {
        if (strcmp(organisations_data[i].name, search_name) == 0)
        {
            printf("Organisation found with name '%s':\n", search_name);
            printf("ID: %d\n", organisations_data[i].id);
            printf("Name: %s\n", organisations_data[i].name);
            printf("Creation Date: %d\n", organisations_data[i].creation_date);
            printf("Posts:\n");
            for (int j = 0; j < NUMBER_OF_POSTS; j++)
            {
                if (strlen(organisations_data[i].posted_content[j]) > 0)
                {
                    printf("Post %d: %s\n", j + 1, organisations_data[i].posted_content[j]);
                }
            }
            return;
        }
    }
    printf("No data found with name '%s'.\n", search_name);
    return;
}

// this is function for searching and printing the data if it matches the id of the node
void *search_by_id(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data, int search_id)
{

    for (int i = 0; i < count_individuals; i++)
    {
        if (individual_data[i].id == search_id)
        {
            return &individual_data[i];
        }
    }
    for (int i = 0; i < count_groups; i++)
    {
        if (group_data[i].id == search_id)
        {
            return &group_data[i];
        }
    }
    for (int i = 0; i < count_business; i++)
    {
        if (business_data[i].id == search_id)
        {
            return &business_data[i];
        }
    }
    for (int i = 0; i < count_organisations; i++)
    {
        if (organisations_data[i].id == search_id)
        {
            return &organisations_data[i];
        }
    }
}

// this is the function for creating the posts of the nodes
void create_post(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data)
{
    int id;
    printf("Enter the id of the data you want to create post for\n");
    scanf("%d", &id);
    getchar();

    for (int i = 0; i < count_individuals; i++)
    {
        if (individual_data[i].id == id)
        {
            for (int j = 0; j < NUMBER_OF_POSTS; j++)
            {
                printf("Enter post %d for %s: ", j + 1, individual_data[i].name);
                fgets(individual_data[i].posted_content[j], MAX_LENGTH, stdin);
                individual_data[i].posted_content[j][strcspn(individual_data[i].posted_content[j], "\n")] = '\0';
            }
            printf("Post created for individual with ID %d.\n", id);
            return;
        }
    }
    for (int i = 0; i < count_groups; i++)
    {
        if (group_data[i].id == id)
        {
            for (int j = 0; j < NUMBER_OF_POSTS; j++)
            {
                printf("Enter post %d for %s: ", j + 1, group_data[i].name);
                fgets(group_data[i].posted_content[j], MAX_LENGTH, stdin);
                group_data[i].posted_content[j][strcspn(group_data[i].posted_content[j], "\n")] = '\0';
            }
            printf("Post created for group with ID %d.\n", id);
            return;
        }
    }
    for (int i = 0; i < count_business; i++)
    {
        if (business_data[i].id == id)
        {
            for (int j = 0; j < NUMBER_OF_POSTS; j++)
            {
                printf("Enter post %d for %s: ", j + 1, business_data[i].name);
                fgets(business_data[i].posted_content[j], MAX_LENGTH, stdin);
                business_data[i].posted_content[j][strcspn(business_data[i].posted_content[j], "\n")] = '\0';
            }
            printf("Post created for business with ID %d.\n", id);
            return;
        }
    }
    for (int i = 0; i < count_organisations; i++)
    {
        if (organisations_data[i].id == id)
        {
            for (int j = 0; j < NUMBER_OF_POSTS; j++)
            {
                printf("Enter post %d for %s: ", j + 1, organisations_data[i].name);
                fgets(organisations_data[i].posted_content[j], MAX_LENGTH, stdin);
                organisations_data[i].posted_content[j][strcspn(organisations_data[i].posted_content[j], "\n")] = '\0';
            }
            printf("Post created for organisation with ID %d.\n", id);
            return;
        }
    }
}

// this is the function to display the content of the node by id
void display_content_by_id(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data, int search_id)
{
    for (int i = 0; i < count_individuals; i++)
    {
        if (individual_data[i].id == search_id)
        {
            for (int j = 0; j < NUMBER_OF_POSTS; j++)
            {
                if (strlen(individual_data[i].posted_content[j]) > 0)
                {
                    printf("Post %d for %s: %s\n", j + 1, individual_data[i].name, individual_data[i].posted_content[j]);
                }
            }
            return;
        }
    }
    for (int i = 0; i < count_groups; i++)
    {
        if (group_data[i].id == search_id)
        {
            for (int j = 0; j < NUMBER_OF_POSTS; j++)
            {
                if (strlen(group_data[i].posted_content[j]) > 0)
                {
                    printf("Post %d for %s: %s\n", j + 1, group_data[i].name, group_data[i].posted_content[j]);
                }
            }
            return;
        }
    }
    for (int i = 0; i < count_business; i++)
    {
        if (business_data[i].id == search_id)
        {
            for (int j = 0; j < NUMBER_OF_POSTS; j++)
            {
                if (strlen(business_data[i].posted_content[j]) > 0)
                {
                    printf("Post %d for %s: %s\n", j + 1, business_data[i].name, business_data[i].posted_content[j]);
                }
            }
            return;
        }
    }
    for (int i = 0; i < count_organisations; i++)
    {
        if (organisations_data[i].id == search_id)
        {
            for (int j = 0; j < NUMBER_OF_POSTS; j++)
            {
                if (strlen(organisations_data[i].posted_content[j]) > 0)
                {
                    printf("Post %d for %s: %s\n", j + 1, organisations_data[i].name, organisations_data[i].posted_content[j]);
                }
            }
            return;
        }
    }
    printf("No data found with ID '%d'.\n", search_id);
    return;
}

// this is the function to display the content of the node by name
void add_1_hop_node(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data)
{
    bool check_if_added = false;
    int target_project_id;
    printf("Enter the project id of the node  where you want to add 1-hop: ");
    scanf("%d", &target_project_id);
    getchar();

    for (int i = 0; i < count_groups; i++)
    {
        if (group_data[i].id == target_project_id)
        {
            printf("Enter the id of the 1-hop node which you will make a connection to the %d: ", target_project_id);
            int hop_id;
            scanf("%d", &hop_id);

            // check if the node is already a 1-hop member
            for (int k = 0; k < group_data[i].individual_member_count; k++)
            {
                if (group_data[i].individual_member_list[k].id == hop_id)
                {
                    printf("Node with ID %d is already a 1-hop member.\n", hop_id);
                    return;
                }
            }

            // add the link
            for (int j = 0; j < count_individuals; j++)
            {
                if (individual_data[j].id == hop_id)
                {
                    group_data[i].individual_member_list[group_data[i].individual_member_count] = individual_data[j];
                    group_data[i].individual_member_count++;
                    check_if_added = true;
                }
            }

            // Check if hop_id is already in the business_member_list
            for (int k = 0; k < group_data[i].business_member_count; k++)
            {
                if (group_data[i].business_member_list[k].id == hop_id)
                {
                    printf("Node with ID %d is already a 1-hop member.\n", hop_id);
                    return;
                }
            }

            // Add the 1-hop node
            for (int j = 0; j < count_business; j++)
            {
                if (business_data[j].id == hop_id)
                {
                    group_data[i].business_member_list[group_data[i].business_member_count] = business_data[j];
                    group_data[i].business_member_count++;
                    check_if_added = true;
                }
            }
        }
    }

    for (int i = 0; i < count_business; i++)
    {
        if (business_data[i].id == target_project_id)
        {
            printf("Enter the id of the 1-hop node which you will make a connection to the %d: ", target_project_id);
            int hop_id;
            scanf("%d", &hop_id);

            // Check if hop_id is already in the individual_member_list
            for (int k = 0; k < business_data[i].individual_member_count; k++)
            {
                if (business_data[i].individual_member_list[k].id == hop_id)
                {
                    printf("Node with ID %d is already a 1-hop member.\n", hop_id);
                    return;
                }
            }

            for (int j = 0; j < count_individuals; j++)
            {
                if (individual_data[j].id == hop_id)
                {
                    business_data[i].individual_member_list[business_data[i].individual_member_count] = individual_data[j];
                    business_data[i].individual_member_count++;
                    check_if_added = true;
                }
            }
        }
    }

    for (int i = 0; i < count_organisations; i++)
    {
        if (organisations_data[i].id == target_project_id)
        {
            printf("Enter the id of the 1-hop node which you will make a connection to the %d: ", target_project_id);
            int hop_id;
            scanf("%d", &hop_id);

            // Check if hop_id is already in the individual_member_list
            for (int k = 0; k < organisations_data[i].individual_member_count; k++)
            {
                if (organisations_data[i].individual_member_list[k].id == hop_id)
                {
                    printf("Node with ID %d is already a 1-hop member.\n", hop_id);
                    return;
                }
            }
            // Add the 1-hop node
            for (int j = 0; j < count_individuals; j++)
            {
                if (individual_data[j].id == hop_id)
                {
                    organisations_data[i].individual_member_list[organisations_data[i].individual_member_count] = individual_data[j];
                    organisations_data[i].individual_member_count++;
                    check_if_added = true;
                }
            }
        }
    }

    if (!check_if_added)
    {
        printf("The Ids entered are wrong . Enter the correct IDs");
        return;
    }
}

// this is the function to display the content of the node by name
void print_1_hop_node(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data)
{
    printf("enter th given id of the node whose 1-hop node you want to print:");
    int search_id;
    scanf("%d", &search_id);

    for (int i = 0; i < count_groups; i++)
    {
        if (group_data[i].id = search_id)
        {
            printf("The 1-hop nodes of the group with ID %d are:\n", search_id);
            for (int j = 0; j < group_data[i].individual_member_count; j++)
            {
                printf("The type of the node is %s\n", group_data[i].individual_member_list[j].type);
                printf("Name: %s\n", group_data[i].individual_member_list[j].name);
                printf("ID: %d\n", group_data[i].individual_member_list[j].id);
                printf("\n");
            }
            for (int j = 0; j < group_data[i].business_member_count; j++)
            {
                printf("The type of the node is %s\n", group_data[i].business_member_list[j].type);
                printf("Name: %s\n", group_data[i].business_member_list[j].name);
                printf("ID: %d\n", group_data[i].business_member_list[j].id);
                printf("\n");
            }
            return;
        }
    }

    for (int i = 0; i < count_business; i++)
    {
        if (business_data[i].id == search_id)
        {
            printf("The 1-hop nodes of the business with ID %d are:\n", search_id);
            for (int j = 0; j < business_data[i].individual_member_count; j++)
            {
                printf("The type of the node is %s\n", business_data[i].individual_member_list[j].type);
                printf("Name: %s\n", business_data[i].individual_member_list[j].name);
                printf("ID: %d\n", business_data[i].individual_member_list[j].id);
                printf("\n");
            }
            return;
        }
    }

    for (int i = 0; i < count_organisations; i++)
    {
        if (organisations_data[i].id == search_id)
        {
            printf("The 1-hop nodes of the organisations with ID %d are:\n", search_id);
            for (int j = 0; j < organisations_data[i].individual_member_count; j++)
            {
                printf("The type of the node is %s\n", organisations_data[i].individual_member_list[j].type);
                printf("Name: %s\n", organisations_data[i].individual_member_list[j].name);
                printf("ID: %d\n", organisations_data[i].individual_member_list[j].id);
                printf("\n");
            }
        }
    }
    return;
}

// this is the function for  searching and printing the posts of the nodes
void search_by_post(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data)
{
    printf("enter the content of the post by whom you want to search:");
    char search_post[MAX_LENGTH];
    scanf(" %[^\n]%*c", search_post);

    for (int i = 0; i < count_individuals; i++)
    {
        for (int j = 0; j < NUMBER_OF_POSTS; j++)
        {
            if (strcmp(individual_data[i].posted_content[j], search_post) == 0)
            {
                printf("The post %s is posted by %s", search_post, individual_data[i].name);
            }
        }
    }

    for (int i = 0; i < count_groups; i++)
    {
        for (int j = 0; j < NUMBER_OF_POSTS; j++)
        {
            if (strcmp(group_data[i].posted_content[j], search_post) == 0)
            {
                printf("The post %s is posted by %s", search_post, group_data[i].name);
            }
        }
    }

    for (int i = 0; i < count_business; i++)
    {
        for (int j = 0; j < NUMBER_OF_POSTS; j++)
        {
            if (strcmp(business_data[i].posted_content[j], search_post) == 0)
            {
                printf("The post %s is posted by %s", search_post, business_data[i].name);
            }
        }
    }

    for (int i = 0; i < count_organisations; i++)
    {
        for (int j = 0; j < NUMBER_OF_POSTS; j++)
        {
            if (strcmp(organisations_data[i].posted_content[j], search_post) == 0)
            {
                printf("The post %s is posted by %s", search_post, organisations_data[i].name);
            }
        }
    }
    return;
}

// this is the  function to display the content of a node linke by another node
void display_content_linked_to_node(each_node_individual *individual_data, each_node_group *group_data, each_node_business *business_data, each_node_organisations *organisations_data)
{
    printf("enter the id of the node whose linked nodes content you want to print: ");
    int search_id;
    scanf("%d", &search_id);

    for (int i = 0; i < count_groups; i++)
    {
        if (group_data[i].id == search_id)
        {
            for (int j = 0; j < group_data[i].individual_member_count; j++)
            {
                display_content_by_id(individual_data, group_data, business_data, organisations_data, group_data[i].individual_member_list[j].id);
            }

            for (int j = 0; j < group_data[i].business_member_count; j++)
            {
                display_content_by_id(individual_data, group_data, business_data, organisations_data, group_data[i].business_member_list[j].id);
            }
        }
    }

    for (int i = 0; i < count_business; i++)
    {
        if (business_data[i].id == search_id)
        {
            for (int j = 0; j < business_data[i].individual_member_count; j++)
            {
                display_content_by_id(individual_data, group_data, business_data, organisations_data, business_data[i].individual_member_list[j].id);
            }
        }
    }

    for (int i = 0; i < count_organisations; i++)
    {
        if (organisations_data[i].id == search_id)
        {
            for (int j = 0; j < organisations_data[i].individual_member_count; j++)
            {
                display_content_by_id(individual_data, group_data, business_data, organisations_data, organisations_data[i].individual_member_list[j].id);
            }
        }
    }
    return;
}

// this is the function to add owners to the business
void add_owners_to_business(each_node_individual *individual_data, each_node_business *business_data)
{
    bool check_if_added = false;
    int target_project_id;
    printf("Enter the project id of the node  where you want to add 1-hop: ");
    scanf("%d", &target_project_id);

    for (int i = 0; i < count_business; i++)
    {
        if (business_data[i].id == target_project_id)
        {
            printf("Enter the id of the owner whom you want to add as an owner to the %d: ", target_project_id);
            int hop_id;
            scanf("%d", &hop_id);

            for (int j = 0; j < count_individuals; j++)
            {
                if (individual_data[j].id == hop_id)
                {
                    business_data[i].owners_list[business_data[i].owners_count] = individual_data[j];
                    business_data[i].owners_count++;
                    check_if_added = true;
                }
            }
        }
    }

    if (!check_if_added)
    {
        printf("The Ids entered are wrong . Enter the correct IDs");
        return;
    }
}

// this is the function to printed the content of the linked individuals
void print_linked_individuals(each_node_individual *individual_data, each_node_group *group_data, each_node_organisations *organisations_data)
{
    printf("enter the given id of the individual linked with the individual you will be needing to print :");
    int search_id;
    scanf("%d", &search_id);

    //  need to print individual whhich are present int he same group or oraganisations
    for (int i = 0; i < count_groups; i++)
    {
        for (int j = 0; j < group_data[i].individual_member_count; j++)
        {
            if (group_data[i].individual_member_list[j].id == search_id)
            {
                printf("The individuals linked to the individual with ID %d are:\n", search_id);
                for (int k = 0; k < group_data[i].individual_member_count; k++)
                {
                    printf("Name: %s\n", group_data[i].individual_member_list[k].name);
                    printf("ID: %d\n", group_data[i].individual_member_list[k].id);
                    printf("\n");
                }
                return;
            }
        }
    }

    for (int i = 0; i < count_organisations; i++)
    {
        for (int j = 0; j < organisations_data[i].individual_member_count; j++)
        {
            if (organisations_data[i].individual_member_list[j].id == search_id)
            {
                printf("The individuals linked to the individual with ID %d are:\n", search_id);
                for (int k = 0; k < organisations_data[i].individual_member_count; k++)
                {
                    printf("Name: %s\n", organisations_data[i].individual_member_list[k].name);
                    printf("ID: %d\n", organisations_data[i].individual_member_list[k].id);
                    printf("\n");
                }
                return;
            }
        }
    }
}

// this is the function to display the master-text-interface
void displayMenu()
{
    printf("\n-------- Welcome to the Text-Based Interface --------\n");
    printf("1. Add Individual Data\n");
    printf("2. Add Group Data\n");
    printf("3. Add Business Data\n");
    printf("4. Add Organizations Data\n");
    printf("5. Print All Nodes\n");
    printf("6. Delete Individual\n");
    printf("7. Delete Group\n");
    printf("8. Delete Business\n");
    printf("9. Delete Organisation\n");
    printf("10. Search by Birthday\n");
    printf("11. Search by Type\n");
    printf("12. Search by Name\n");
    printf("13. Create Post\n");
    printf("14. Search by Content\n");
    printf("15. Add 1-Hop Node\n");
    printf("16. Print 1-Hop Nodes\n");
    printf("17. Display Content Linked to  any Particular Node\n");
    printf("18. Display Content By a particular ID\n");
    printf("19. Add Owners to Business\n");
    printf("20. Print Linked Individuals Content \n");
    printf("0. Exit\n");
}

// this is the main function
int main()
{
    // initializing the different data types
    each_node_individual *individual_data = malloc(NUMBER_OF_PEOPLE * sizeof(each_node_individual));
    each_node_group *group_data = malloc(NUMBER_OF_PEOPLE * sizeof(each_node_group));
    each_node_business *business_data = malloc(NUMBER_OF_PEOPLE * sizeof(each_node_business));
    each_node_organisations *organisations_data = malloc(NUMBER_OF_PEOPLE * sizeof(each_node_organisations));

    if (individual_data == NULL)
    {
        printf("Memory allocation failed.\n");
        return 1;
    }
    if (group_data == NULL)
    {
        printf("Memory allocation failed.\n");
        return 1;
    }
    if (business_data == NULL)
    {
        printf("Memory allocation failed.\n");
        return 1;
    }
    if (organisations_data == NULL)
    {
        printf("Memory allocation failed.\n");
        return 1;
    }

    int choice;
    int delete_id;
    int search_birthday;
    int search_id_display_content;

    do
    {
        displayMenu(); // This is display master-text-interface
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            individual_data_addition(individual_data);
            break;
        case 2:
            group_data_addition(group_data);
            break;
        case 3:
            business_data_addition(business_data);
            break;
        case 4:
            organisations_data_addition(organisations_data);
            break;
        case 5:
            individual_data_printing(individual_data);
            group_data_printing(group_data);
            business_data_printing(business_data);
            organisations_data_printing(organisations_data);
            break;
        case 6:
            printf("Enter the id of the node you want to delete");
            scanf("%d", &delete_id);
            delete_individual(individual_data, delete_id);
            break;
        case 7:
            printf("Enter the id of the node you want to delete");
            scanf("%d", &delete_id);
            delete_group(group_data, delete_id);
            break;
        case 8:
            printf("Enter the id of the node you want to delete");
            scanf("%d", &delete_id);
            delete_business(business_data, delete_id);
            break;
        case 9:
            printf("Enter the id of the node you want to delete");
            scanf("%d", &delete_id);
            delete_organisation(organisations_data, delete_id);
            break;
        case 10:
            printf("Enter the birthday of the individual you want to search for in ddmmyyyy format");
            scanf("%d", &search_birthday);
            search_by_birthday(individual_data, search_birthday);
            break;
        case 11:
            search_by_type(individual_data, group_data, business_data, organisations_data);
            break;
        case 12:
            search_by_name(individual_data, group_data, business_data, organisations_data);
            break;
        case 13:
            create_post(individual_data, group_data, business_data, organisations_data);
            break;
        case 14:
            search_by_post(individual_data, group_data, business_data, organisations_data);
            break;
        case 15:
            add_1_hop_node(individual_data, group_data, business_data, organisations_data);
            break;
        case 16:
            print_1_hop_node(individual_data, group_data, business_data, organisations_data);
            break;
        case 17:
            display_content_linked_to_node(individual_data, group_data, business_data, organisations_data);
            break;
        case 18:
            printf("Enter the id of the node whose content you want to print");
            scanf("%d", &search_id_display_content);
            display_content_by_id(individual_data, group_data, business_data, organisations_data, search_id_display_content);
        case 19:
            add_owners_to_business(individual_data, business_data);
            break;
        case 20:
            print_linked_individuals(individual_data, group_data, organisations_data);
            break;
        case 0:
            break;
        default:
            printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 0);

    // free the memory
    free(individual_data);
    free(group_data);
    free(business_data);
    free(organisations_data);
    return 0;
}