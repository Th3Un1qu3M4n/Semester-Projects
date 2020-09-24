/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hotel_management_system;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.Date;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.text.SimpleDateFormat;
import javax.swing.JOptionPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author Th3Un1qu3M4n
 */
public class RESERVATIONS {
    
    DB_CONNECTION myConnection = new DB_CONNECTION();
    
    ROOMS rooms = new ROOMS();
    
    CLIENT clients = new CLIENT();
    
    public boolean addReservations(int clientId,int roomNumber, String dateIn, String dateOut){
        
        PreparedStatement st;
        
        String addQuery = "INSERT INTO `reservations`(`client_id`, `room_number`, `date_in`, `date_out`) VALUES (?,?,?,?)";
        
       
        try {
            if(clients.checkClientStatus(clientId)){
                if(rooms.checkRoomStatus(roomNumber).equals("No")){
                    st = myConnection.createConnection().prepareStatement(addQuery);

                    st.setInt(1, clientId);
                    st.setInt(2, roomNumber);
                    st.setString(3, dateIn);
                    st.setString(4, dateOut);


                    if (st.executeUpdate() > 0){
                        rooms.setRoomStatus(roomNumber, "Yes");
                        createLog(0,"ADDED");
                        return true;
                    }else
                        return false;
                    
                }else{                
                    JOptionPane.showMessageDialog(null, "Room is already reserved!", "ALready Reserved!", JOptionPane.ERROR_MESSAGE);
                    return false;
                }
                
            }else{
                
                JOptionPane.showMessageDialog(null, "Client Doesn't Exits", "Client Error!", JOptionPane.ERROR_MESSAGE);
                return false;
            
            }
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        
    }
    
    public boolean updateReservations(int reserveId, int clientId,int roomNumber, String dateIn, String dateOut){
        
        PreparedStatement st;
        
        String updateQuery = "UPDATE `reservations` SET `client_id`=?,`room_number`=?,`date_in`=?,`date_out`=? WHERE `reserve_id`=?";
        
        int roomIdreserved = getRoomNumber(reserveId);
        
        try {
            if(clients.checkClientStatus(clientId)){
                if(roomNumber == roomIdreserved || (rooms.checkRoomStatus(roomNumber).equals("No"))){
            
                    st = myConnection.createConnection().prepareStatement(updateQuery);


                    st.setInt(1, clientId);
                    st.setInt(2, roomNumber);
                    st.setString(3, dateIn);
                    st.setString(4, dateOut);
                    st.setInt(5, reserveId);

                    createLog(reserveId,"EDITED");   
                    return (st.executeUpdate() > 0);
             
               
                }else{                
                    JOptionPane.showMessageDialog(null, "Room is already reserved!", "ALready Reserved!", JOptionPane.ERROR_MESSAGE);
                    return false;
                }
                
            }else{
                
                JOptionPane.showMessageDialog(null, "Client Doesn't Exits", "Client Error!", JOptionPane.ERROR_MESSAGE);
                return false;
                
            }
                    
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        
    }
    public boolean removeReservation(int reserveId){
        
        PreparedStatement st;
        
        String removeQuery = "DELETE FROM `reservations` WHERE `reserve_id`=?";
        
       
        try {
            st = myConnection.createConnection().prepareStatement(removeQuery);
            
            st.setInt(1, reserveId);
            
            int roomId = getRoomNumber(reserveId);
            
            if (st.executeUpdate() > 0){
                if(rooms.setRoomStatus(roomId, "No")){
                    createLog(reserveId,"DELETED"); 
                    return true;
                }
                else
                    return false;
            }else
                return false;
            
                
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        
    }
    
    public void refreshReservationsTable(JTable roomTable){
         
        PreparedStatement ps;
        ResultSet rs;
        
        String selectionQuery = "SELECT * FROM `reservations`";
        
        try {
            ps = myConnection.createConnection().prepareStatement(selectionQuery);
            
            rs  = ps.executeQuery();
            
            DefaultTableModel tableModel = (DefaultTableModel) roomTable.getModel();
            
            Object[] row;
            
            while(rs.next()){
                row = new Object[5];
                
                row[0] = rs.getInt(1);
                row[1] = rs.getInt(2);
                row[2] = rs.getInt(3);
                row[3] = rs.getString(4);
                row[4] = rs.getString(5);
                
                tableModel.addRow(row);
                
            }
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
    
    public int getRoomNumber(int reserveId){
        
        
        PreparedStatement ps;
        ResultSet rs;
        //System.out.println(reserveId);
        
        String selectionQuery = "SELECT `room_number` FROM `reservations` WHERE `reserve_id`=?";
        
        
        try {
            ps = myConnection.createConnection().prepareStatement(selectionQuery);
            
            ps.setInt(1, reserveId);
            
            rs  = ps.executeQuery();
            
                           
            if(rs.next()){
                return rs.getInt(1);
            }else
                return 0;
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return 0;
        }
    }
    
    public void createLog(int reserveId, String action){
        
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd 'at' h:mm a");
        
        String currentTimeStamp = dateFormat.format(new Date());
        
        if(reserveId == 0){
            
        }
        
        try {
            BufferedWriter writeLog = new BufferedWriter(new FileWriter("log.txt",true));
            
            if(reserveId == 0){
                writeLog.write("NEW reservation" + " " + action + " at " + currentTimeStamp+"\n");
                
            }else{
                writeLog.write("Reservation Number: " + reserveId + " " + action + " on " + currentTimeStamp+"\n");
            }
            
            writeLog.flush();
            writeLog.close();
            
            
            
        } catch (IOException ex) {
            Logger.getLogger(RESERVATIONS.class.getName()).log(Level.SEVERE, null, ex);
        }
    
    }
       
}
