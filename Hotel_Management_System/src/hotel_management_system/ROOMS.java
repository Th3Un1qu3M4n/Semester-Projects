/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hotel_management_system;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JComboBox;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author Th3Un1qu3M4n
 */
public class ROOMS {
    
    DB_CONNECTION myConnection = new DB_CONNECTION();
    
    public boolean removeRoomTypes(){
        
        PreparedStatement st;
        
        String removeQuery = "DELETE FROM `type`";
        
       
        try {
            st = myConnection.createConnection().prepareStatement(removeQuery);
            
            return (st.executeUpdate() > 0);
                
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        
    }
    
    
    public boolean saveRoomTypes(JTable roomsTypeTable){
        
        PreparedStatement ps;
        String addQuery = "INSERT INTO `type`(`id`, `label`, `price`) VALUES (?,?,?)";
        DefaultTableModel tableModel = (DefaultTableModel) roomsTypeTable.getModel();
        
        try {
            ps = myConnection.createConnection().prepareStatement(addQuery);
            
            

            for(int row=0; row <roomsTypeTable.getRowCount(); row++){

                String roomTypeIdString =  (String) tableModel.getValueAt(row,0);
                int roomTypeId = Integer.valueOf(roomTypeIdString);
                String title =  (String) tableModel.getValueAt(row,1);
                String price =  (String) tableModel.getValueAt(row,2);
                ps.setInt(1, roomTypeId);
                ps.setString(2, title);
                ps.setString(3, price);
                ps.addBatch();
            }
            
            ps.executeBatch();
            return true;
            
        } catch (SQLException ex) {
            Logger.getLogger(ROOMS.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        
            
        
    
    }
    
    public void readRoomTypes(JTable roomsTypeTable){
        
                
        try {
            
            BufferedReader br = new BufferedReader(new FileReader("roomsType.txt"));
            
            DefaultTableModel model = (DefaultTableModel)roomsTypeTable.getModel();
            Object[] lines = br.lines().toArray();
            
            for(int i = 0; i < lines.length; i++){
                String[] row = lines[i].toString().split(" ");
                model.addRow(row);
            }
            
        } catch (FileNotFoundException ex) {
            Logger.getLogger(ROOMS.class.getName()).log(Level.SEVERE, null, ex);
        }
    
    }

    
    public void insertRoomsTypeTable(JTable roomsTable){
         
        PreparedStatement ps;
        ResultSet rs;
        
        String selectionQuery = "SELECT * FROM `type`";
        
        try {
            ps = myConnection.createConnection().prepareStatement(selectionQuery);
            
            rs  = ps.executeQuery();
            
            DefaultTableModel tableModel = (DefaultTableModel) roomsTable.getModel();
            
            Object[] row;
            
            while(rs.next()){
                row = new Object[3];
                
                row[0] = rs.getInt(1);
                row[1] = rs.getString(2);
                row[2] = rs.getString(3);
                
                tableModel.addRow(row);
                
            }
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
    
    public void insertRoomsTypeComboBox(JComboBox comboBox){
         
        PreparedStatement ps;
        ResultSet rs;
        
        String selectionQuery = "SELECT `id` FROM `type`";
        
        try {
            ps = myConnection.createConnection().prepareStatement(selectionQuery);
            
            rs  = ps.executeQuery();
                                   
            while(rs.next()){
                                
                comboBox.addItem(rs.getInt(1));
                
            }
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
    
    
    public boolean addRooms(int roomId,int roomType, String pNumber){
        
        PreparedStatement st;
        
        String addQuery = "INSERT INTO `rooms`(`room_number`, `type`, `phone`, `reserved`) VALUES (?,?,?,?)";
        
       
        try {
            st = myConnection.createConnection().prepareStatement(addQuery);
            
            st.setInt(1, roomId);
            st.setInt(2, roomType);
            st.setString(3, pNumber);
            st.setString(4, "No");
        
            
            if (st.executeUpdate() > 0)
                return true;
            else
                return false;
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        
    }
    
    
    public boolean updateRoom(int roomId,int roomType, String pNumber, String reserved){
        
        PreparedStatement st;
        
        String updateQuery = "UPDATE `rooms` SET `type`=?,`phone`=?,`reserved`=? WHERE `room_number`=?";
        
       
        try {
            st = myConnection.createConnection().prepareStatement(updateQuery);
            
            
            st.setInt(1, roomType);
            st.setString(2, pNumber);
            st.setString(3, reserved);
            st.setInt(4, roomId);
        
            
            return (st.executeUpdate() > 0);
                
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        
    }
    
    public boolean removeRoom(int roomId){
        
        PreparedStatement st;
        
        String removeQuery = "DELETE FROM `rooms` WHERE `room_number`=?";
        
       
        try {
            st = myConnection.createConnection().prepareStatement(removeQuery);
            
            st.setInt(1, roomId);
            
            return (st.executeUpdate() > 0);
                
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        
    }
    
    public void refreshRoomTable(JTable roomTable){
         
        PreparedStatement ps;
        ResultSet rs;
        
        String selectionQuery = "SELECT * FROM `rooms`";
        
        try {
            ps = myConnection.createConnection().prepareStatement(selectionQuery);
            
            rs  = ps.executeQuery();
            
            DefaultTableModel tableModel = (DefaultTableModel) roomTable.getModel();
            
            Object[] row;
            
            while(rs.next()){
                row = new Object[4];
                
                row[0] = rs.getInt(1);
                row[1] = rs.getString(2);
                row[2] = rs.getString(3);
                row[3] = rs.getString(4);
                
                tableModel.addRow(row);
                
            }
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
    
    
    public boolean setRoomStatus(int roomId,String isReserved){
        
        PreparedStatement st;
        
        String updateQuery = "UPDATE `rooms` SET `reserved`=? WHERE `room_number`=?";
        
       
        try {
            st = myConnection.createConnection().prepareStatement(updateQuery);
            
            
            st.setString(1, isReserved);
            st.setInt(2, roomId);
        
            
            return (st.executeUpdate() > 0);
                
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        
    }
    public String checkRoomStatus(int roomId){
        
        PreparedStatement st;
        ResultSet rs;
        
        String updateQuery = "SELECT `reserved` FROM `rooms` WHERE `room_number`=?";
        
       
        try {
            st = myConnection.createConnection().prepareStatement(updateQuery);
            
            st.setInt(1, roomId);
            rs = st.executeQuery();
            
            if(rs.next())
                return rs.getString(1);
            else
                return "";
                
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return "";
        }
        
    }
    
    
    
}
