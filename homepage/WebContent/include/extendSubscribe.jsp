<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<div class="textBox">
<form name="subscribeForm" action="processExtend.jsp" method="post">
	이메일 : <input type="text" name="id"> @ <input type="text" name="mail"> <br/>
	<%-- 학교 선택한 값은 DB 테이블 선택 부분이랑 연결 --%>
	학교 <jsp:include page="schoolList.html"/><br/>
	<input type="button" name="submitbtn" value="확인"
		onClick="submitForm(checkBlank(subscribeForm) & checkMailForm(subscribeForm.mail.value), subscribeForm)">
</form>
</div>
<div class="subscribeBox">
	<a href="main.jsp?targetPage=subscribe.jsp">이전으로</a><br/>
	구독 해지는 <a href="main.jsp?targetPage=unsubscribe.jsp">여기</a>에서 해주세요
</div>