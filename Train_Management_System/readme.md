# **DATA SRUCTURE AND ALGORITHM:**

# PROJECT OVERVIEW

## (Sir Dr. Inayat ur Rehman)



Submitted by:

# **Faiq Shahzad**

### _**(FA19-BCS-021)**_

# **Muhammad Ahmed**

### _**(FA19-BCS-041)**_

**TRAIN MANAGEMENT SYSTEM:**

**FEATURES:**

The following project is a train management system that controls maximum aspects of a train management. This management system comprises of:

- Linked List
- Graphs
- Stack
- Array List
- Loops/Switch
- Console-based GUI
- Vectors
- File Handling

**Credentials:**

1. **Admin:**

- Password

**TRAIN:**

- Insert a Train
- View All Trains
- Search Specific Train
- Update Train Data
- Delete a Train

**TICKETS:**

- View All Tickets
- Search Specific Ticket
- View Recent Tickets
- Back Up Data


**FILE HANDLING:**


1. **User:**

- View All Trains
- Book a Train
- View **Minimum Distance** from one Station to another along with the **Trains on that Route**
- View **Minimum Cost** from one Station to another along with the **Trains on that Route**

**Working:**

    (NOTE: Can not enter strings with spaces due to the limitations of file handling)



**ADMIN:**

  This management system allows the admin to perform various operations on the Trains and Tickets.

**LOGIN:**

  The admin is required to provide password in order to access the Admin Menu.

    Admin Password is admin123



**ADMIN MENU:**



**TRAIN INSERTION:**

  The admin can insert a train and all its details along with its routes and this process is performed using linked list and the data inserted is saved in the file **&quot;trains.txt&quot;**.



**VIEW TRAINS:**

  The admin has the access to view all the available trains along with details.



**SEARCH SPECIFIC TRAIN:**

  The admin can search a specific train along a specific route by entering the source and destination.



**UPDATE TRAIN DATA:**

  The admin has the authority to search and update a trains details, the train node is searched by its train id.



**TRAIN DELETION:**

  The admin has the authority to delete a train with all its details and the tickets details booked for it would be lost.



**VIEW TICKETS:**

  The admin can view all the tickets details for all the trains available.



**SEARCH SPECIFIC TICKET:**

  The admin can search or verify a specific ticket. This ticket can be accessed by entering its ticket number.

**VIEW RECENT TRAINS AND TICKETS:**

  Whenever a train is inserted or a ticket is booked, then two stacks are maintained, the one stack contains the train ids and the other stack contains the ticket number. The admin can view the most recently inserted train and booked ticket.

**USER:**

   This management system allows the user to view the details of all the trains and give user access to book a ticket from one station to another.

**USER MENU:**

**VIEW TRAIN DETAILS:**

   It displays the details of all the trains available.

**BOOK A TICKET:**

   First the user has to input the source station, then provide the destination.

   Now, if there are no trains on that particular route then, the program will display an option to search again or go back to User Menu.

   Otherwise, if the trains are available on the particular route, then the program will display all the trains on that specific route and ask user to input train id to book.

   If the id is not correct the program will again display option to continue….

   If the Train id is correct, then the program will ask for the booking details and will then provide an option to confirm.

   Once a ticket is booked, the data is then written to file **&quot;tickets.txt&quot;**.

**VIEW ROUTES:**

   It also allows the user to view the specific routes. This process is performed by using **Graph** and our **own algorithm** by modifying the **Dijkstra** and   **Prims algorithms** using **adjacency matrix**.

- _Minimum Distance:_

    User can view the minimum distance from one station to another, also the user can view the route take and the available trains on that route.

- _Minimum Cost:_
    User can view the minimum cost from one station to another, also the user can view the route take and the available trains on that route.

## © MUHAMMAD AHMED
