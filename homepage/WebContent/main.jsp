<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<script src="js_function.js?version=1.1"></script>
<link rel="stylesheet" type="text/css" href="main.css?version=1.1">
<!-- 모바일 보기 설정 태그 -->
<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0">
<title>KAU e-mail notifier</title>
</head>
<body>
<%--
자바스크립트로 폼 확인하는 방식은 클라이언트에서 JS파일 수정 가능하므로 보안은 취약하지만
추후 해당 IP 접근 횟수 제한 + JSP에서 하는 방법으로 해결하자
--%>
<%
String includeFolder = "include/";
String subscribe = "subscribe.jsp";
String unsubscribe = "unsubscribe.jsp";
String targetPage =  (request.getParameter("targetPage") == null) ? 
		includeFolder + subscribe : includeFolder + request.getParameter("targetPage");
%>
<div class="contentBox">
	<jsp:include page="<%= targetPage %>"/>
</div>
<div class="siteInfo">
<%@ include file="info.jsp" %>
</div>
</body>
</html>