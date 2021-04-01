<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<div class="textBox">
공지알리미 구독 해지 페이지 입니다.<br/>
만약 구독 해지를 했는데도 메일이 계속 수신되는 경우,<br/>
phoiNotifier@gmail.com 으로 직접 메일을 보내주세요<br/>
구독 취소 사유가 있는 경우 적어주시면 감사하겠습니다 :)<br/>
이용해 주셔서 감사합니다.<br/>
<form name="subscribeForm" action="processUnsubscribe.jsp" method="post">
	이메일 : <input type="text" name="id"> @ <input type="text" name="mail"> <br/>
	학교 <jsp:include page="schoolList.html"/><br/>
	취소 이유<br/>
	<textarea name="unsubscribeReason" rows="3" cols="30">.</textarea><br/>
	<input type="button" name="submitbtn" value="확인"
		onClick="submitForm(checkBlank(subscribeForm) & checkMailForm(subscribeForm.mail.value), subscribeForm)">
</form>
</div>
<div class="subscribeBox">
	구독은 <a href="main.jsp?targetPage=subscribe.jsp">여기</a>에서 해주세요
</div>