# **DATA SRUCTURE AND ALGORITHM:**

# PROJECT OVERVIEW

## (Sir Dr. Inayat ur Rehman)

![](RackMultipart20211128-4-17dd17n_html_d29faab2afb2051e.jpg)

Submitted by:

# _ **Faiq Shahzad** _

## _**(FA19-BCS-021)**_

# _ **Muhammad Ahmed** _

## _**(FA19-BCS-041)**_

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

**FILE HANDLING:**

- Back Up Data

1. **User:**

- View All Trains
- Book a Train
- View **Minimum Distance** from one Station to another along with the **Trains on that Route**
- View **Minimum Cost** from one Station to another along with the **Trains on that Route**

**Working:**

(NOTE: Can not enter strings with spaces due to the limitations of file handling)

![](RackMultipart20211128-4-17dd17n_html_9259d3892e18c5f6.png)

**ADMIN:**

This management system allows the admin to perform various operations on the Trains and Tickets.

**LOGIN:**

The admin is required to provide password in order to access the Admin Menu.

Admin Password is **&quot;admin123&quot;.**

![](RackMultipart20211128-4-17dd17n_html_717eab9b85729263.png)

**ADMIN MENU:**

![](RackMultipart20211128-4-17dd17n_html_7a34b4525105101d.png)

**TRAIN INSERTION:**

The admin can insert a train and all its details along with its routes and this process is performed using linked list and the data inserted is saved in the file **&quot;trains.txt&quot;**.

![](RackMultipart20211128-4-17dd17n_html_6db4c2373081c09c.png)

**VIEW TRAINS:**

The admin has the access to view all the available trains along with details.

![](RackMultipart20211128-4-17dd17n_html_1c5a2e6f7b9f1c66.png)

**SEARCH SPECIFIC TRAIN:**

The admin can search a specific train along a specific route by entering the source and destination.

![](RackMultipart20211128-4-17dd17n_html_a3e67cdf031ffe89.png)

**UPDATE TRAIN DATA:**

The admin has the authority to search and update a trains details, the train node is searched by its train id.

![](RackMultipart20211128-4-17dd17n_html_3a2f6ffaf7bcd90f.png)

**TRAIN DELETION:**

The admin has the authority to delete a train with all its details and the tickets details booked for it would be lost.

![](RackMultipart20211128-4-17dd17n_html_b0fff10b3b37e334.png)

**VIEW TICKETS:**

The admin can view all the tickets details for all the trains available.

![](RackMultipart20211128-4-17dd17n_html_556eb855222c2198.png)

**SEARCH SPECIFIC TICKET:**

The admin can search or verify a specific ticket. This ticket can be accessed by entering its ticket number.

![](RackMultipart20211128-4-17dd17n_html_446cb1c939945fe4.png)

**VIEW RECENT TRAINS AND TICKETS:**

Whenever a train is inserted or a ticket is booked, then two stacks are maintained, the one stack contains the train ids and the other stack contains the ticket number. The admin can view the most recently inserted train and booked ticket.

![](RackMultipart20211128-4-17dd17n_html_a2c020d7af14edc6.png)

**USER:**

This management system allows the user to view the details of all the trains and give user access to book a ticket from one station to another.

**USER MENU:**

![](RackMultipart20211128-4-17dd17n_html_34e4255f102f03cb.png)

**VIEW TRAIN DETAILS:**

It displays the details of all the trains available.

![](RackMultipart20211128-4-17dd17n_html_936d0eaaf100f0ae.png)

**BOOK A TICKET:**

First the user has to input the source station, then provide the destination.

Now, if there are no trains on that particular route then, the program will display an option to search again or go back to User Menu.

Otherwise, if the trains are available on the particular route, then the program will display all the trains on that specific route and ask user to input train id to book.

If the id is not correct the program will again display option to continue….

If the Train id is correct, then the program will ask for the booking details and will then provide an option to confirm.

Once a ticket is booked, the data is then written to file **&quot;tickets.txt&quot;**.

![](RackMultipart20211128-4-17dd17n_html_a2b008d37cdc735a.png)

**VIEW ROUTES:**

It also allows the user to view the specific routes. This process is performed by using **Graph** and our **own algorithm** by modifying the **Dijkstra** and **Prims algorithms** using **adjacency matrix**.

- _Minimum Distance:_

User can view the minimum distance from one station to another, also the user can view the route take and the available trains on that route.

![](RackMultipart20211128-4-17dd17n_html_b380b0552a00d7b5.png)

- _Minimum Cost:_

User can view the minimum cost from one station to another, also the user can view the route take and the available trains on that route.

![](RackMultipart20211128-4-17dd17n_html_e03c31723030e30.png)

**GRAPH:**

So far, the following is the graph that is being constructed according to current stations and trains.

**COST (RS):**

![Picture 14](RackMultipart20211128-4-17dd17n_html_71844a9369dbccc.gif)

![](RackMultipart20211128-4-17dd17n_html_ee7caab3ff1a68ca.png) ![](RackMultipart20211128-4-17dd17n_html_a5edcced8786845c.png) ![](RackMultipart20211128-4-17dd17n_html_46d6c8a3bbe1424b.png)

![](RackMultipart20211128-4-17dd17n_html_a09a7e97ac19c576.png)

![](RackMultipart20211128-4-17dd17n_html_4354e2ed6625f3bb.png) ![](RackMultipart20211128-4-17dd17n_html_2b804ceb2ba17dfa.png)

![Picture 14](RackMultipart20211128-4-17dd17n_html_71844a9369dbccc.gif)

**DISTANCE (KM):**

![](RackMultipart20211128-4-17dd17n_html_2b804ceb2ba17dfa.png)

![](RackMultipart20211128-4-17dd17n_html_371793f6c23d8d51.png) ![](RackMultipart20211128-4-17dd17n_html_d72140fafda0e6c5.png)

![](RackMultipart20211128-4-17dd17n_html_6bb961acc5375563.png)

![](RackMultipart20211128-4-17dd17n_html_7b475926ba4ab376.png) ![](RackMultipart20211128-4-17dd17n_html_46aaba37106de1d7.png)