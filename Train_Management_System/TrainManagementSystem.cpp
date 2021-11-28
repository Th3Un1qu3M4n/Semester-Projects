#include <iostream>
#include <fstream>
#include <iomanip>
#include <stack>
#include <vector>

using namespace std;

struct train{

	string trainId, trainName, source, destination;
	int arrivalTime, departureTime, seats, cost, distance;
	train *next = NULL ;
};
 
struct ticket{

	int ticketNo;
	string bookedTrainId, bookerName;
	int noOfSeats, bookedCost;
	train *bookedTrain = NULL ;
	ticket *next = NULL;
};
 

//------------------------------------------------ DIJKSTRA GRAPH ALGORITHM ------------------------------------
 
 
int *route; 
int *parent;


class Graph{
	
	int **edges;
	
public:
		
	int n;
	int e;
	
	Graph(){
		
        this->n = 4;
        this->e = 6;
        edges = new int*[n];
    
		for(int i=0; i<n;i++){
			edges[i]= new int[n];
			for(int j=0;j<n;j++){
				edges[i][j];
			}
		}
	}
	
		
	Graph(int n,int e){
		
		this->n = n;
		this->e = e;
		edges = new int*[n];
		
		for(int i=0; i<n;i++){
			edges[i]= new int[n];
			for(int j=0;j<n;j++){
				edges[i][j];
			}
		}
	}
	
	
	void addEdge(int f,int s,int weight){
		
		edges[f][s]=weight;
	}
	
	void dijkstra(int srcIndex){
		
		route = new int[n];
		parent = new int[n];
		bool *visited = new bool[n];
		
		for(int i=0; i<n; i++){
			route[i] = INT_MAX;
			visited[i] = false;
			parent[i] = -1;
		}
		
		route[srcIndex] = 0;
		parent[srcIndex] = -1;
		
		for(int i=0; i<n-1; i++){
			
			int minVertex = findMinVertex(route, visited);
			visited[minVertex] = true;
			
			for(int j=0; j<n; j++){
				if(edges[minVertex][j] != 0 && !visited[j]){
					int dist = route[minVertex] + edges[minVertex][j];
					
					if(dist < route[j]){
						route[j] = dist;
						parent[j] = minVertex;
					}
				}
			}
		}	
	}
	
	
	int findMinVertex(int *route, bool *visited){
		
		int minVertex = -1;
		
		for(int i=0; i<n; i++){
			
			if(!visited[i] && (minVertex == -1 || route[i] < route[minVertex])){
				minVertex = i;
			}
		}
		return minVertex;
	}
};



//-------------------------------------------------------------------------------------------------


//VECTOR:
vector<string> cities;

//STACK:
stack<string> checkLastTrain;
stack<int> checkLastBooking;

//TRAIN:
train *first= NULL;
train *last = NULL;

string trainId, trainName, source, destination;
int arrivalTime, departureTime, seats, cost, distanc;
bool isFound;

//TICKET:
ticket *ticketFirst= NULL;
ticket *ticketLast = NULL; 
	
int ticketNo;
string bookedTrainId, bookerName;
int noOfSeats, bookedCost;


//-------------------------------------------------------------------------------------------------
//MENUS


void mainMenu();
void AdminLogin();
void AdminMenu();
void UserMenu();


//-------------------------------------------------------------------------------------------------
//TRAIN FUNCTIONS:


void insertTrain(string, string, string, string, int, int, int, int, int);
void insertTrainMenu();
void display();
void searchTrainMenu();
train* searchTrainById(string);
void searchTrain(string, string);
void showRouteTrain(string , string);
void updateTrain();
void deleteTrain(string);
void readFromFile();
void writeToFile();


//-------------------------------------------------------------------------------------------------
//TICKET FUNCTIONS:


void insertTicket(int , string, string ,int);
void bookTicketMenu();
void displayTickets();
void searchTicket();
void readTicketsFromFile();
void writeTicketsToFile();

void viewLatestBookingAndTrain();

void createGraph();
void minimumDistanceRoute(Graph, int, int);
void printPath(int* , int );
void searchTrainRoute(int*, int);


//------------------------------------------------ MAIN -------------------------------------------



int main(){

readFromFile();
readTicketsFromFile();
//system("PAUSE");

mainMenu();

}



//----------------------------------------------- MENU FUNCTIONS ------------------------------------



void mainMenu(){
	
	int opt;
	system ("CLS");
	system ("Color 4F");
	
		cout<<"\n";	
		cout<<setw(65)<<" "<<"WELCOME TO TRAIN MANAGEMENT SYSTEM\n\n\n";
		cout<<setw(70)<<" "<<"1---ADMIN\n";
		cout<<setw(70)<<" "<<"2---USER\n";
		cout<<setw(70)<<" "<<"0---EXIT\n\n";
		cout<<setw(70)<<" "<<"Enter your choice: ";
		cin>>opt;
		cout<<"\n";
		
		switch(opt)
		{
			case 1: 
				AdminLogin();
				break;
			case 2:	
				UserMenu();
				break;
			case 0:	
				cout<<"Exiting Program!";
				exit(0);
				
				break;
			default:
				cout<<"\n Plz enter correct choice ";
				mainMenu();
				break;
		}
		mainMenu();
}


void AdminLogin(){
	string password;
	char x;
	
	cout<<"Enter Password: ";
	cin>>password;
	
	if (password != "admin123"){
		cout<<"\nWrong Password\n";
		cout<<"Do you want to try again (y/n)";
		cin>>x;
		cout<<"\n";
		
		if (x == 'y' || x == 'Y'){
			AdminLogin();
		}
		else{
			mainMenu();
		}
	}
	AdminMenu(); 
}


void AdminMenu(){
	int opt;
	system ("CLS");
	system ("Color 0A");
		
		cout<<"\n";
		cout<<setw(65)<<" "<<"WELCOME TO TRAIN MANAGEMENT SYSTEM\n\n\n";
		
		cout<<setw(70)<<" "<<"-----TRAIN--------\n";
		cout<<setw(70)<<" "<<"Enter 1 to Insert\n";
		cout<<setw(70)<<" "<<"Enter 2 to View All Trains\n";
		cout<<setw(70)<<" "<<"Enter 3 to Search Specific Train\n";
		cout<<setw(70)<<" "<<"Enter 4 to Update Train DATA\n";
		cout<<setw(70)<<" "<<"Enter 5 to Delete Specific Train\n\n";
		
		cout<<setw(70)<<" "<<"-----TICKET--------\n";
		cout<<setw(70)<<" "<<"Enter 6 to View All Tickets\n";
		cout<<setw(70)<<" "<<"Enter 7 to Search Specific Ticket\n";
		cout<<setw(70)<<" "<<"Enter 8 to View Recent Tickets And Trains\n";
		cout<<setw(70)<<" "<<"Enter 9 to BackUp data to File\n";
		cout<<setw(70)<<" "<<"Enter 0 to LOGOUT\n\n";
		cout<<setw(70)<<" "<<"Enter your choice: ";
		
		cin>>opt;
		cout<<"\n";
	
		switch(opt)
		{
			case 1: 
				insertTrainMenu();
				break;
			case 2:	
				display();
				break;
			case 3:	
				searchTrainMenu();
				system("PAUSE");
				break;
			case 4:	
				updateTrain();
				break;
			case 5:	{
				cout<<"\n Enter Train no to delete: ";
				string del_val;
				cin>>del_val;
				deleteTrain(del_val);
				break;
				}
			case 6:	{
				displayTickets();
				break;
				}
			case 7:	{
				searchTicket();
				break;
				}
			case 8:
				viewLatestBookingAndTrain();
				break;
			case 9:	{
				writeToFile();
				writeTicketsToFile();
				break;
				}
			case 0:	
				cout<<"Logging Out!";
				mainMenu();
				break;
			default:
				cout<<"\n Plz enter correct choice ";
				AdminMenu();
				break;
		}
		AdminMenu();
}


void UserMenu(){
	int opt;
	system ("CLS");
	system ("Color F2");
		
		cout<<"\n";
		cout<<setw(65)<<" "<<"WELCOME TO TRAIN MANAGEMENT SYSTEM\n\n\n";
		
		cout<<setw(70)<<" "<<"Enter 1 to View Trains\n";
		cout<<setw(70)<<" "<<"Enter 2 to Book Ticket\n";
		cout<<setw(70)<<" "<<"Enter 3 to View Minimum Distance and Cost\n";
		cout<<setw(70)<<" "<<"Enter 0 to MAINMENU\n\n";
		cout<<setw(70)<<" "<<"Enter your choice: ";
		
		cin>>opt;
		cout<<"\n";
		
		switch(opt)
		{
			case 1:	
				display();
				break;
			case 2:
				bookTicketMenu();
				break;
			case 3:
				createGraph();
				break;
			case 0:	
				cout<<"Exiting Program!";
				mainMenu();
				break;
			default:
				cout<<"\n Plz enter correct choice ";
				UserMenu();
				break;
		}
		UserMenu();
}



//---------------------------------------------- TRAIN FUNCTIONS ------------------------------------



void insertTrain(string id, string name, string source, string destination, int arr, int dep, int seats, int cost, int distanc){
	
	train *curr = new train;
	
	curr->trainId = id;
	curr->trainName = name;
	curr->source = source;
	curr->destination = destination;
	curr->arrivalTime = arr;
	curr->departureTime = dep;
	curr->seats = seats;
	curr->cost = cost;
	curr->distance = distanc;
	
	if(first==NULL){
	    first = last = curr;
	}
	else{
		last->next = curr;
		last = curr;
	}
}


void insertTrainMenu(){
	system ("CLS");
	
	cout<<"\nEnter Train Id:";
	cin >> trainId;
	
	cout<<"\nEnter Train Name:";
	cin >> trainName;
	
	cout<<"\nEnter Train source:";
	cin >> source;
	
	cout<<"\nEnter Train destination:";
	cin >> destination;
	
	cout<<"\nEnter Train arrivalTime:";
	cin >> arrivalTime;
	
	cout<<"\nEnter Train departureTime:";
	cin >> departureTime;
	
	cout<<"\nEnter Train Available Seats:";
	cin >> seats;
	
	cout<<"\nEnter Cost of a seat:";
	cin >> cost;
	
	cout<<"\nEnter Distance between Cities(KM):";
	cin >> distanc;
	
	insertTrain(trainId, trainName, source, destination, arrivalTime, departureTime, seats, cost, distanc);
	cout<<"\nInserted Train no:"<<trainId<<"\n\n";
	
	checkLastTrain.push(trainId);
	writeToFile();
	
	system ("PAUSE");
}


void display(){

	train *p;
	
	p = first;
	
	cout<<setw(10)<<"Train Id"<<setw(20)<<" Train Name"<<setw(20)<<"Train Source"<<setw(20)<<"Train Destination"<<setw(20)<<"Arrival Time"<<setw(20)<<"Departure Time"<<setw(20)<<"Available Seats"<<setw(10)<<"Cost"<<setw(20)<<"Distance";
	cout<<"\n"<<setw(10)<<"---------"<<setw(20)<<"-----------"<<setw(20)<<"-------------"<<setw(20)<<"------------------"<<setw(20)<<"-------------"<<setw(20)<<"---------------"<<setw(20)<<"----------------"<<setw(10)<<"------"<<setw(20)<<"------";
	
	if(first != NULL){	
	
		while(p != NULL){
			
			cout<<"\n\n";
			cout<<setw(10)<<p->trainId;
			cout<<setw(20)<<p->trainName;
			cout<<setw(20)<<p->source;
			cout<<setw(20)<<p->destination;
			cout<<setw(20)<<p->arrivalTime;
			cout<<setw(20)<<p->departureTime;
			cout<<setw(15)<<p->seats;
			cout<<setw(15)<<p->cost;
			cout<<setw(15)<<p->distance;
			
			p = p->next;
		
		}
		cout<<"\n\n\n\n";
		system ("PAUSE");
	}
	else{
		cout<<"\n The list is EMPTY!\n\n";
		system ("PAUSE");
	}

}


void searchTrainMenu(){
	system ("CLS");
	
	cout<<"\nEnter Train source:";
	cin >> source;
	
	cout<<"\nEnter Train destination:";
	cin >> destination;
	
	searchTrain(source, destination);
}


train* searchTrainById(string srchId){

	train *p;
	
	p = first;	
	
	while(p != NULL){
		
		if(p->trainId == srchId){
			return p;		
		}
		
		p = p->next;
	
	}
	return NULL;
}


void searchTrain(string trSource, string trDestination){

	train *p;
	p = first;
	
	isFound = false;
	
	cout<<"\n";
	cout<<setw(10)<<"Train Id"<<setw(20)<<" Train Name"<<setw(20)<<"Train Source"<<setw(20)<<"Train Destination"<<setw(20)<<"Arrival Time"<<setw(20)<<"Departure Time"<<setw(20)<<"Available Seats"<<setw(10)<<"Cost"<<setw(20)<<"Distance";
	cout<<"\n"<<setw(10)<<"---------"<<setw(20)<<"-----------"<<setw(20)<<"-------------"<<setw(20)<<"------------------"<<setw(20)<<"-------------"<<setw(20)<<"---------------"<<setw(20)<<"----------------"<<setw(10)<<"------"<<setw(20)<<"------";
	
	if(first != NULL){	
	
		while(p != NULL){
			
			if(p->source == trSource && p->destination == trDestination){
				
				isFound = true;
				
				cout<<"\n";
				cout<<setw(10)<<p->trainId;
				cout<<setw(20)<<p->trainName;
				cout<<setw(20)<<p->source;
				cout<<setw(20)<<p->destination;
				cout<<setw(20)<<p->arrivalTime;
				cout<<setw(20)<<p->departureTime;
				cout<<setw(15)<<p->seats;
				cout<<setw(15)<<p->cost;
				cout<<setw(15)<<p->distance;
			}
			
			p = p->next;
		
		}
		if (!isFound){
			cout<<"\n\nNO TRAIN AVAILABLE ON THIS SPECIFIC ROUTE!!";
		}
		cout<<"\n\n";
	}
	else{
		cout<<"\n The list is EMPTY!\n\n";
	}

}


void showRouteTrain(string trSource, string trDestination){

	train *p;
	
	p = first;
	
	if(first != NULL){		
		while(p != NULL){
			
			if(p->source == trSource && p->destination == trDestination){
				
				cout<<"\n";
				cout<<setw(10)<<p->trainId;
				cout<<setw(20)<<p->trainName;
				cout<<setw(20)<<p->source;
				cout<<setw(20)<<p->destination;
				cout<<setw(20)<<p->arrivalTime;
				cout<<setw(20)<<p->departureTime;
				cout<<setw(15)<<p->seats;
				cout<<setw(15)<<p->cost;
				cout<<setw(15)<<p->distance;
			}
			
			p = p->next;
		
		}
		cout<<"\n";
	}
	else{
		cout<<"\n The list is EMPTY!\n\n";
	}
}


void updateTrain(){
	string searchTrainId;
	cout<<"\n Enter Train Id:";cin>>searchTrainId;
	
	train* currTrain = searchTrainById(searchTrainId);
	
	if(currTrain == NULL){
		cout<<"\n Train Doesnt Exists! \n\n";
		system("PAUSE");
		return;
	}
	
	cout<<"\nEnter Train Name:";
	cin >> trainName;
	
	cout<<"\nEnter Train source:";
	cin >> source;
	
	cout<<"\nEnter Train destination:";
	cin >> destination;
	
	cout<<"\nEnter Train arrivalTime:";
	cin >> arrivalTime;
	
	cout<<"\nEnter Train departureTime:";
	cin >> departureTime;
	
	cout<<"\nEnter Train Available Seats:";
	cin >> seats;
	
	cout<<"\nEnter Cost of a seat:";
	cin >> cost;
	
	cout<<"\nEnter Distance between Cities(KM):";
	cin >> distanc;
	
	currTrain->trainName = trainName;
	currTrain->source = source;
	currTrain->destination = destination;
	currTrain->arrivalTime = arrivalTime;
	currTrain->departureTime = departureTime;
	currTrain->seats = seats;
	currTrain->cost = cost;
	currTrain->distance = distanc;
	
	checkLastTrain.push(currTrain->trainId);
	
	writeToFile();
	system ("PAUSE");
	
}


void deleteTrain(string val){
	
	train *p = first;
	train *p1;
	
	while(p!=NULL && p->trainId != val){
		p1 = p;
		p = p->next;
	}
	
	if(p == NULL){
		cout<<"\n Train No. "<<val<<" Doestnot Exists!\n\n";
		system("PAUSE");
		return;
	}
	
	p1->next = p->next;
	
	cout<<"\n"<<p->trainId<<" Deleted\n";
	
	delete p;
	
	system ("PAUSE");
}


// TRAIN FILE READING:
void readFromFile(){
	
	ifstream inFile;
	inFile.open("trains.txt");
	
	if(inFile.fail()){
		cerr << "Error Opeing File!\n";
		exit(1);
	}
	
	while(!inFile.eof()){
		inFile >> trainId;
		inFile >> trainName;
		inFile >> source;
		inFile >> destination;
		inFile >> arrivalTime;
		inFile >> departureTime;
		inFile >> seats;
		inFile >> cost;
		inFile >> distanc;
		if(inFile.eof()){
			break;
		}
		
		insertTrain(trainId, trainName, source, destination, arrivalTime, departureTime, seats, cost, distanc);
		cout<<"\nInserted Train no:"<<trainId<<"\n";
	}
	inFile.close();
	
}


// TRAIN FILE WRITING:
void writeToFile(){
	
	train *p;
	
	p = first;
	
	ofstream outFile;
	outFile.open("trains.txt");
	
	if(first != NULL){		
		while(p != NULL)		
		{
		
			outFile<<p->trainId<<"\n";
			outFile<<p->trainName<<"\n";
			outFile<<p->source<<"\n";
			outFile<<p->destination<<"\n";
			outFile<<p->arrivalTime<<"\n";
			outFile<<p->departureTime<<"\n";
			outFile<<p->seats<<"\n";
			outFile<<p->cost<<"\n";
			outFile<<p->distance<<"\n\n";
						
			p = p->next;
		
		}
		cout<<"\n DATA SAVED!\n\n";
	}
	else{
		cout<<"\n The list is EMPTY!\n\n";
	}	
		
	outFile.close();

}



//---------------------------------------------- TICKET FUNCTIONS ------------------------------------



void insertTicket(int srcTicketNo, string srcBookedTrainId, string srcBookerName,int srcNoOfSeats){
	
	ticket *curr = new ticket;
	
	curr->ticketNo = srcTicketNo;
	curr->bookedTrainId = srcBookedTrainId;
	curr->bookerName = srcBookerName;
	curr->noOfSeats = srcNoOfSeats;
	curr->bookedTrain = searchTrainById(srcBookedTrainId);
	curr->bookedCost = curr->bookedTrain->cost * curr->noOfSeats;
	
	if(ticketFirst == NULL){
	    ticketFirst = ticketLast=curr;
	}
	else{
		ticketLast->next = curr;
		ticketLast = curr;
	}
}


void bookTicketMenu(){
	
	searchTrainMenu();
	
	train *tempTrain = NULL;
	char idChoice;
	if (!isFound){
		cout<<"\n\nDo you want to search again (y/n): ";
		cin>>idChoice;
		
		if (idChoice != 'y' && idChoice != 'Y'){
			UserMenu();
		}
		else{
			bookTicketMenu();
		}
	}
	do{
		cout<<"\nEnter Train Id to Book:";
		cin >> bookedTrainId;
		
		tempTrain = searchTrainById(bookedTrainId);
		
		if(tempTrain == NULL){
			cout<<"\n Train Id doesnot exists.... \n";
			
			cout<<"\n\nDo you want to enter id again (y/n): ";
			cin>>idChoice;
			
			if (idChoice != 'y' && idChoice != 'Y'){
				UserMenu();
			}
			
		}
	}while(tempTrain == NULL);
	
	cout<<"\n\n Booking "<<tempTrain->trainName<<" From "<<tempTrain->source<<" To "<<tempTrain->destination<<"\n";
	cout<<"\n\nEnter Booker Name:";cin >> bookerName;
	cout<<"\nEnter Number of Seats:";cin >> noOfSeats;
	cout<<"\n\nCONFIRM TICKET!";
	
	bookedCost = tempTrain->cost*noOfSeats;	
	
	cout<<"\n";
	
	cout<<setw(30)<<"Train No.: "<<bookedTrainId;
	cout<<setw(30)<<"Train Name: "<<tempTrain->trainName;
	cout<<setw(30)<<"\n-------------------------------------------------------------------------------------------------------------------------";
	cout<<setw(30)<<"\n\nBookerName: "<<bookerName;
	cout<<setw(30)<<"No. Of Seats: "<<noOfSeats;
	cout<<setw(30)<<"Booked Cost: "<<bookedCost;
	cout<<setw(30)<<"\nSource: "<<tempTrain->source;
	cout<<setw(30)<<"Destination: "<<tempTrain->destination;
	cout<<setw(30)<<"Arrival Time: "<<tempTrain->arrivalTime;
	cout<<setw(30)<<"Departure Time: "<<tempTrain->departureTime;
	
	cout<<"\n\n\nFor main menu enter any other key:";

	char confirm;	
	cout<<"\nDo you confirm ticket! (y/n):"; cin >> confirm;
	
	switch(confirm){
		case 'y':{
			break;
		}
		case 'n':{
			UserMenu();
			break;
		}
		default:{
			mainMenu();
			break;
		}
	}

	if(ticketLast == NULL){
		ticketNo = 1;
	}
	else{
		ticketNo = (ticketLast->ticketNo) + 1;
	}
	
	insertTicket(ticketNo, bookedTrainId, bookerName, noOfSeats);
	tempTrain->seats = (tempTrain->seats) - noOfSeats;
	
	cout<<"\n\nSucessfully Booked Ticket No."<<ticketNo<<"\n\n";
	
	checkLastBooking.push(ticketNo);
	
	writeToFile();
	writeTicketsToFile();
	
	system ("PAUSE");
}


void displayTickets(){

	ticket *p;
	
	p = ticketFirst;
	
	if(first != NULL){	
	
		while(p != NULL){
			
			cout<<"\n";
			cout<<setw(10)<<"Ticket No.: "<<p->ticketNo;
			cout<<setw(30)<<"Train No.: "<<p->bookedTrainId;
			cout<<setw(30)<<"Train Name: "<<p->bookedTrain->trainName;
			cout<<setw(30)<<"\n-------------------------------------------------------------------------------------------------------------------------";
			cout<<setw(30)<<"\nBookerName: "<<p->bookerName;
			cout<<setw(30)<<"No. Of Seats: "<<p->noOfSeats;
			cout<<setw(30)<<"Booked Cost: "<<p->bookedCost;
			cout<<setw(30)<<"\nSource: "<<p->bookedTrain->source;
			cout<<setw(30)<<"Destination: "<<p->bookedTrain->destination;
			cout<<setw(30)<<"Arrival Time: "<<p->bookedTrain->arrivalTime;
			cout<<setw(30)<<"Departure Time: "<<p->bookedTrain->departureTime;
			
			p = p->next;
			cout<<"\n\n";
		
		}
		cout<<"\n\n\n\n";
		system ("PAUSE");
	}
	else{
		cout<<"\n No Tickets Booked Yet! \n\n";
		system ("PAUSE");
	}
}


void searchTicket(){
	
	int searchNo;
	
	cout<<setw(10)<<"Enter Ticket No.: ";
	cin>>searchNo;
	
	ticket *p;
	p = ticketFirst;
	
	bool found = false;
	
	if(first != NULL){	
	
		while(p != NULL){
			if(p->ticketNo == searchNo){
				
				cout<<"\n";
				cout<<setw(10)<<"Ticket No.: "<<p->ticketNo;
				cout<<setw(30)<<"Train No.: "<<p->bookedTrainId;
				cout<<setw(30)<<"Train Name: "<<p->bookedTrain->trainName;
				cout<<setw(30)<<"\n-------------------------------------------------------------------------------------------------------------------------";
				cout<<setw(30)<<"\nBookerName: "<<p->bookerName;
				cout<<setw(30)<<"No. Of Seats: "<<p->noOfSeats;
				cout<<setw(30)<<"Booked Cost: "<<p->bookedCost;
				cout<<setw(30)<<"\nSource: "<<p->bookedTrain->source;
				cout<<setw(30)<<"Destination: "<<p->bookedTrain->destination;
				cout<<setw(30)<<"Arrival Time: "<<p->bookedTrain->arrivalTime;
				cout<<setw(30)<<"Departure Time: "<<p->bookedTrain->departureTime;
				cout<<"\n\n";
				
				found = true;
				break;
				
			}
			
			p = p->next;
				
		}
		if(found == false){
			cout<<"\n No TICKET FOUND WITH THIS NUMBER!\n\n";
		}
		cout<<"\n\n\n\n";
		system ("PAUSE");
	}
	else{
		cout<<"\n No Tickets Booked Yet! \n\n";
		system ("PAUSE");
	}

}


// TICKET FILE READING:
void readTicketsFromFile(){
	
	ifstream inFile;
	inFile.open("tickets.txt");
	
	if(inFile.fail()){
		cerr << "Error Opeing File!\n";
		exit(1);
	}
	
	while(!inFile.eof()){
		inFile >> ticketNo;
		inFile >> bookedTrainId;
		inFile >> bookerName;
		inFile >> noOfSeats;
		
		if(inFile.eof()){
			break;
		}
		
		insertTicket(ticketNo, bookedTrainId, bookerName, noOfSeats);
		cout<<"\nInserted ticketNo no:"<<ticketNo<<"\n";
	}
	
	inFile.close();
	
}


// TICKET FILE WRITING:
void writeTicketsToFile(){
	
	ticket *p;
	
	p = ticketFirst;
	
	ofstream outFile;
	outFile.open("tickets.txt");
	
	if(first != NULL){	
	
		while(p != NULL)	
		{
			outFile<<p->ticketNo<<"\n";
			outFile<<p->bookedTrainId<<"\n";
			outFile<<p->bookerName<<"\n";
			outFile<<p->noOfSeats<<"\n\n";
			
			p = p->next;
		
		}
		cout<<"\n DATA SAVED!\n\n";
	}
	else{
		cout<<"\n The list is EMPTY!\n\n";
	}
			
	outFile.close();
}




//------------------------------------------------GRAPH FUNCTIONS------------------------------------



void viewLatestBookingAndTrain(){
	
	if (checkLastBooking.empty()){
		cout<<"\nNo Recent Booking";
	}
	else{
		cout<<"\nRecent Booking ID is: "<<checkLastBooking.top();
	}
	
	cout<<"\n";
	
	if (checkLastTrain.empty()){
		cout<<"\nNo recent train inserted";
	}
	else{
		cout<<"\nRecent Inserted Train: "<<checkLastTrain.top();
	}
	
	cout<<"\n\n";
	system ("PAUSE");
}


bool isCityExists(string srcCity){
	
	for(int i=0; i<cities.size(); i++){
		if(cities[i] == srcCity){
			return true;
		}
	}
	return false;
}


int returnCityIndex(string srcCity){
	
	for(int i=0; i<cities.size(); i++){
		if(cities[i] == srcCity){
			return i;
		}
	}
	return -1;
}


void createGraph(){
	
	int noOfEdges=0;
	int noOfCities=0;
	
	train *curr = first;
	
	while(curr != NULL){
		
		if(curr == first){
			cities.push_back(curr->source);
			cities.push_back(curr->destination);
		}
		else{
			if(!isCityExists(curr->source)){
				cities.push_back(curr->source);
			}
			if(!isCityExists(curr->destination)){
				cities.push_back(curr->destination);
			}
		}
		
		noOfEdges+=1;
		curr = curr->next;
	}
	
	noOfCities = cities.size();
	
	cout<<"\n Current Cities are: ";
	for(int i=0; i<noOfCities; i++){
		cout<<"("<<i<<") "<<cities[i]<<", ";
	}
	
	curr = first;
	
	Graph distGraph(noOfCities, noOfEdges);
	Graph costGraph(noOfCities, noOfEdges);
	
	while(curr != NULL){
		
		int src = returnCityIndex(curr->source);
		int dest = returnCityIndex(curr->destination);
		int routeDist = curr->distance;
		int routeCost = curr->cost;
		
		distGraph.addEdge(src,dest,routeDist);
		costGraph.addEdge(src,dest,routeCost);
		
		curr = curr->next;
	}
	
	int srcIndex;
	char choice;
	
	cout<<"\n Enter Soruce station(Number): "; cin>>srcIndex;
	
	cout<<"\n View Minimum Distance(d) / Cost(c): ";
	cin>>choice;
	
	if(choice=='d' || choice=='D'){
		cout<<"\n\n";
		minimumDistanceRoute(distGraph, srcIndex, 1);
	}
	else if(choice=='c'|| choice=='C'){
		cout<<"\n\n";
		minimumDistanceRoute(costGraph, srcIndex, 2);
	}
	else{
		cout<<"\nInvalid View Choice....\n";
	}
	
	
	cities.clear();
	system("PAUSE");
	
}


void printPath(int parentArray[], int j){
	
	if(parent[j] == -1){
		return;
	}
	
	printPath(parentArray, parent[j]);
	cout<<" -> "<<cities[j];
		
}


void searchTrainRoute(int parentArray[], int j){
	
	string currCity = cities[j];
	if(parent[j] == -1){
		return;
	}
	
	string pCity = cities[parent[j]];
	
	searchTrainRoute(parentArray, parent[j]);
	
	showRouteTrain(pCity, currCity);	
		
}


void minimumDistanceRoute(Graph cityGraph, int srcIndex, int graphtype){
		
	cityGraph.dijkstra(srcIndex);
	
	cout<<setw(60)<<" "<<"**************************************************************\n";
	
	if(graphtype == 1 ){
		cout<<setw(60)<<" "<<"The Minimum distance from "<<cities[srcIndex]<<" to different cities is:\n";
	}
	else{
		cout<<setw(60)<<" "<<"The Minimum Cost from "<<cities[srcIndex]<<" to different cities is:\n";
	}
	
	cout<<setw(60)<<" "<<"**************************************************************\n\n";
	
	for(int i=0; i<cityGraph.n; i++){
		
		if(srcIndex == i){
			continue;
		}
		
		if(graphtype == 1){
			
			cout<<setw(70)<<" "<<cities[srcIndex]<<" -> "<<cities[i]<<" ====> "<<route[i]<<" KM"<<endl;
			
			cout<<setw(70)<<" "<<"Minimum Route is: "<<cities[srcIndex];
			printPath(parent, i);
			
			cout<<"\n\n";
			
			cout<<setw(70)<<" "<<"AVAILABLE TRAINS ON ROUTE: \n\n";
			
			cout<<setw(10)<<"Train Id"<<setw(20)<<" Train Name"<<setw(20)<<"Train Source"<<setw(20)<<"Train Destination"<<setw(20)<<"Arrival Time"<<setw(20)<<"Departure Time"<<setw(20)<<"Available Seats"<<setw(10)<<"Cost"<<setw(15)<<"Distance";
			cout<<"\n"<<setw(10)<<"---------"<<setw(20)<<"-----------"<<setw(20)<<"-------------"<<setw(20)<<"------------------"<<setw(20)<<"-------------"<<setw(20)<<"---------------"<<setw(20)<<"----------------"<<setw(10)<<"------"<<setw(15)<<"---------";
			
			searchTrainRoute(parent, i);
			
			cout<<"\n\n\n";
		}
		else{
			
			cout<<setw(70)<<" "<<cities[srcIndex]<<" -> "<<cities[i]<<" ====> "<<route[i]<<" RS"<<endl;
			
			cout<<setw(70)<<" "<<"Cheapest Route is: "<<cities[srcIndex];
			printPath(parent, i);
			
			cout<<"\n\n";
			
			cout<<setw(70)<<" "<<"AVAILABLE TRAINS ON ROUTE: \n\n";
			cout<<setw(10)<<"Train Id"<<setw(20)<<" Train Name"<<setw(20)<<"Train Source"<<setw(20)<<"Train Destination"<<setw(20)<<"Arrival Time"<<setw(20)<<"Departure Time"<<setw(20)<<"Available Seats"<<setw(10)<<"Cost"<<setw(15)<<"Distance";
			cout<<"\n"<<setw(10)<<"---------"<<setw(20)<<"-----------"<<setw(20)<<"-------------"<<setw(20)<<"------------------"<<setw(20)<<"-------------"<<setw(20)<<"---------------"<<setw(20)<<"----------------"<<setw(10)<<"------"<<setw(15)<<"---------";
			
			searchTrainRoute(parent, i);
			
			cout<<"\n\n\n";
		}	
	}	
}

//---------------------------------------------------------------------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------  END  ------------------------------------------------------------------------------
//---------------------------------------------------------------------------------------------------------------------------------------------------------------
