<%@ page contentType="text/html;charset=utf-8" %>
<%@ page import="homepage.ConnectionContext" %>
<%@ page import="java.sql.*" %>
<html>
<body>
<%
   String msg = null;
   String sql = "SELECT 'hello jspbookdb!' AS msg";
   Connection conn = ConnectionContext.getConnection();
   PreparedStatement pstmt = conn.prepareStatement(sql);
   ResultSet rs = pstmt.executeQuery();
   if (rs.next())
      msg = rs.getString("msg");
   rs.close();
   pstmt.close();
%>
쿼리문: <%=sql%><br/>
쿼리결과: <%=msg%><br/>
</body>
</html>
