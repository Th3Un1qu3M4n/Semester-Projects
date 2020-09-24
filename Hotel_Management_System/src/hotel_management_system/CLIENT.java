/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hotel_management_system;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author Th3Un1qu3M4n
 */
public class CLIENT {
    
    DB_CONNECTION myConnection = new DB_CONNECTION();
    
    public boolean validatePhoneNumber(String pNumber){
        
        
        
        int digitCount = 0;
        
        if(pNumber.length() == 11 || pNumber.length() == 10){
            
            for(int i=0; i<pNumber.length();i++){
                                   
                    if(Character.isDigit(pNumber.charAt(i)))
                        digitCount++;
                    else{
                        break;
                    }
            }
            if(digitCount == pNumber.length())
                return true;
            
            else{
                JOptionPane.showMessageDialog(null, "Phone Number can only have numbers!", "ERROR", 3);
                return false;
            }     
           
        }
        
        JOptionPane.showMessageDialog(null, "Invalid Phone Number", "ERROR", 3);
        return false;
                

    }
    
    public boolean addClient(String fName, String lName, String pNumber, String email){
        
        PreparedStatement st;
        
        String addQuery = "INSERT INTO `clients`(`first_name`, `last_name`, `phone_number`, `email`) VALUES (?,?,?,?)";
        
       
        try {
            st = myConnection.createConnection().prepareStatement(addQuery);
            
            st.setString(1, fName);
            st.setString(2, lName);
            st.setString(3, pNumber);
            st.setString(4, email);
        
            
            if (st.executeUpdate() > 0)
                return true;
            else
                return false;
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        
    }
    
    public void refreshClientTable(JTable clientTable){
         
        PreparedStatement ps;
        ResultSet rs;
        
        String selectionQuery = "SELECT * FROM `clients`";
        
        try {
            ps = myConnection.createConnection().prepareStatement(selectionQuery);
            
            rs  = ps.executeQuery();
            
            DefaultTableModel tableModel = (DefaultTableModel) clientTable.getModel();
            
            Object[] row;
            
            while(rs.next()){
                row = new Object[5];
                
                row[0] = rs.getInt(1);
                row[1] = rs.getString(2);
                row[2] = rs.getString(3);
                row[3] = rs.getString(4);
                row[4] = rs.getString(5);
                
                tableModel.addRow(row);
                
            }
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
    
    public boolean updateClient(int clientId,String fName, String lName, String pNumber, String email){
        
        PreparedStatement st;
        
        String updateQuery = "UPDATE `clients` SET `first_name`=?,`last_name`=?,`phone_number`=?,`email`=? WHERE `id`=?";
        
       
        try {
            st = myConnection.createConnection().prepareStatement(updateQuery);
            
            
            st.setString(1, fName);
            st.setString(2, lName);
            st.setString(3, pNumber);
            st.setString(4, email);
            st.setInt(5, clientId);
        
            
            return (st.executeUpdate() > 0);
                
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        
    }
    
    
    public boolean removeClient(int clientId){
        
        PreparedStatement st;
        
        String removeQuery = "DELETE FROM `clients` WHERE `id`=?";
        
       
        try {
            st = myConnection.createConnection().prepareStatement(removeQuery);
            
            st.setInt(1, clientId);
            
            return (st.executeUpdate() > 0);
                
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        
        
        
    }
    
    public boolean checkClientStatus(int clientId){
        
        PreparedStatement st;
        ResultSet rs;
        
        String updateQuery = "SELECT * FROM `clients` WHERE `id`=?";
        
       
        try {
            st = myConnection.createConnection().prepareStatement(updateQuery);
            
            st.setInt(1, clientId);
            rs = st.executeQuery();
            
            if(rs.next())
                return true;
            else
                return false;
                
            
        } catch (SQLException ex) {
            Logger.getLogger(CLIENT.class.getName()).log(Level.SEVERE, null, ex);
            return false;
        }
        
    }
    
}
