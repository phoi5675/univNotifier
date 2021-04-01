<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.util.*, java.sql.*, homepage.*" %>
<!DOCTYPE html>
<jsp:useBean id="member" class="homepage.Member"/>
<jsp:setProperty name="member" property="id" param="id"/>
<jsp:setProperty name="member" property="cname" param="mail"/>
<jsp:setProperty name="member" property="school" param="school"/>

<html>
<head>
<link rel="stylesheet" type="text/css" href="main.css?version=1.0">
<title>이메일 구독 완료</title>
</head>
<body>
<%
boolean isNew = false;
//db에 제거하는 부분
Connection conn = ConnectionContext.getConnection();
if (Database.isInDatabase(conn, member)){
	isNew = false;
	Database.deleteEmail(conn, member);
}
else {
	isNew = true;
}

conn.close();
%>
<div class="contentBox">
	<div class="textBox">
		<% if (!isNew) { %>
		구독 해지가 완료되었습니다.<br/>
		해지하신 이메일은 <%= member.getEmail() %>입니다.<br/>
		이용해 주셔서 감사합니다 :)
		<% } else { %>
		존재하지 않는 회원입니다.<br/>
		<a href="main.jsp">이전으로</a>
		<% } %>
	</div>
</div>
<div class="siteInfo">
<%@ include file="info.jsp" %>
</div>
</body>
</html>