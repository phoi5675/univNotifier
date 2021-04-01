<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<div class="textBox">
공지알리미 신청 페이지 입니다.<br/>
구독 기간은 <b>4년</b> 입니다.<br/>
자세한 개인정보 이용 내역은 <a href="main.jsp?targetPage=terms.jsp">여기</a>에서 확인해 주세요<br/>
<form name="subscribeForm" action="processSubscribe.jsp" method="post">
	이메일 : <input type="text" name="id"> @ <input type="text" name="mail"> <br/>
	<%-- 학교 선택한 값은 DB 테이블 선택 부분이랑 연결 --%>
	학교 <jsp:include page="schoolList.html"/><br/>
	학과 <select id="major" name="major">
			<option>학과를 선택해주세요</option>
		</select>
	<input type="button" name="submitbtn" value="확인"
		onClick="submitForm(checkBlank(subscribeForm) & checkMailForm(subscribeForm.mail.value), subscribeForm)">
</form>
</div>
<div class="subscribeBox">
	기간 연장은 <a href="main.jsp?targetPage=extendSubscribe.jsp">여기</a>,<br/>
	구독 해지는 <a href="main.jsp?targetPage=unsubscribe.jsp">여기</a>에서 해주세요
</div>