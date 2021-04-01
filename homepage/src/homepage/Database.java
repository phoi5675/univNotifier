package homepage;

import java.sql.*;

public class Database {
	public static boolean isInDatabase(Connection conn, Member member) {
		boolean isInDB = true;
		try {
			PreparedStatement pstmt = conn.prepareStatement("SELECT count(*) AS recordCount FROM " + member.getSchool() + " WHERE Email=?");
			
			pstmt.setString(1, member.getEmail());
			
			ResultSet rs = pstmt.executeQuery();
			
			while (rs.next()) {
				int recordCount = rs.getInt("recordCount");
				
				if (recordCount != 1) {
					isInDB = false;
				}
				else {
					isInDB = true;
				}
			}
			
			pstmt.close();
			rs.close();
		}
		catch (SQLException e) {
			e.printStackTrace();
		}
		
		if (isInDB) {
			return true;
		}
		else {
			return false;
		}
		
	}
	
	public static void insertEmail(Connection conn, Member member) {
		try {
			PreparedStatement pstmt = conn.prepareStatement("INSERT INTO " + member.getSchool() + " (Email, RegDate, Major) VALUES (?, ?, ?)");

			pstmt.setString(1, member.getEmail());
			pstmt.setString(2, member.getRegDate());
			pstmt.setString(3, member.getMajor());
			
			pstmt.executeUpdate();
			
			pstmt.close();
		}
		catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
	public static void deleteEmail(Connection conn, Member member) {
		try {
			PreparedStatement pstmt = conn.prepareStatement("DELETE FROM " + member.getSchool() + " WHERE Email=?");
			
			pstmt.setString(1, member.getEmail());
			
			pstmt.executeUpdate();
			
			pstmt.close();
		}
		catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
	public static void extendSubscribe(Connection conn, Member member) {
		try {
			PreparedStatement pstmt = conn.prepareStatement("UPDATE " + member.getSchool() + " SET RegDate=? WHERE Email=?");

			pstmt.setString(1, member.getRegDate());
			pstmt.setString(2, member.getEmail());
			
			pstmt.executeUpdate();
			
			pstmt.close();
		}
		catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
