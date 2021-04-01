<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.util.Date, java.util.Calendar, java.sql.*, java.text.SimpleDateFormat, homepage.*" %>
<!DOCTYPE html>
<jsp:useBean id="member" class="homepage.Member" scope="session"/>
<jsp:setProperty name="member" property="id" param="id"/>
<jsp:setProperty name="member" property="cname" param="mail"/>
<jsp:setProperty name="member" property="major" param="major"/>
<jsp:setProperty name="member" property="school" param="school"/>

<html>
<head>
<link rel="stylesheet" type="text/css" href="main.css?version=1.0">
<title>이메일 구독 완료</title>
<%
boolean isNew = true;
String targetPage = "";

Date today = new Date();
SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMdd");
String todayString = sdf.format(today);

member.setRegDate(todayString);

//db에 추가하는 부분
Connection conn = ConnectionContext.getConnection();
if (!Database.isInDatabase(conn, member)){
	Database.insertEmail(conn, member);
	isNew = true;
}
else {
	isNew = false;
}

conn.close();
/*
String includeFolder = "include/";
String exist = "subscribeError.jsp";
String newMember = "subscribeComplete.jsp";
if (isNew) {
	targetPage = includeFolder + newMember; 
}
else {
	targetPage = includeFolder + exist;
}
*/
%>
</head>
<body>
<%
int subscribeLimitYear = 4;
Calendar cal = Calendar.getInstance();
int year = cal.get(Calendar.YEAR) + subscribeLimitYear;
int month = cal.get(Calendar.MONTH) + 1;
int date = cal.get(Calendar.DATE);

String subscribeDue = year + "년 " + month + "월 " + date + "일";
%>
<div class="contentBox">
	<div class="textBox">
		<%-- 효율적인 방법이 있을라나... --%>
		<% if (isNew){ %>
		가입이 완료되었습니다.<br/>
		가입하신 이메일은 <%= member.getEmail() %>입니다.<br/>
		공지 구독 기간은 ~ <%= subscribeDue %> 이고, 연장은 추후 가능합니다.<br/>
		<% } else { %>
		이미 존재하는 사용자입니다.
		<% } %>
	</div>
</div>
<div class="siteInfo">
<%@ include file="info.jsp" %>
</div>
</body>
</html>