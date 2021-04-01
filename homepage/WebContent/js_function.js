/*
 * main.jsp
 */
function checkBlank(formBox) {
	var isBlank = false;
	for (var i = 0; i < formBox.length; i++) {
		if (!formBox[i].value) {
			alert("빈칸을 채워주세요");
			formBox[i].focus();
			isBlank = true;
			break;
		}
	}

	if (isBlank) {
		return false;
	}
	else {
		return true;
	}
}
function checkMailForm(mailAddr) {
	/*
	 * regex from
	 * https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/%EC%A0%95%EA%B7%9C%EC%8B%9D
	 * http://blog.naver.com/psj9102/221203659771
	 */
	var re = /([a-z0-9\w]+\.)[a-z0-9]{2,4}/gi;

	if (re.test(mailAddr)) {
		return true;
	}
	else {
		alert("올바른 메일 형식을 입력해 주세요");
		return false;
	}

}
function submitForm(isCompleteForm, formBox) {

	if (isCompleteForm) {
		formBox.submit();
	}
}

function subSelect(select) {
	// 통일성을 위해 딕셔너리 및 배열에 사용되는 이름은 각각 폴더의 const 파일에서 가져와야 함
	var kau = {
		"mach": "항공우주기계공학부", "elec": "항공전자정보공학부", "soft": "소프트웨어학과", "stuf": "재료공학부",
		"laws": "항공교통물류학부", "avia": "항공운항학과", "busi": "경영학부", "free": "자유전공학부"
	};
	var smu = {
		"kjc": "한일문화컨텐츠전공", "biz": "경영학부", "eco": "경제금융학부", "new": "글로벌경영학과", "com": "융합경영학과",
		"hi": "휴먼지능정보공학전공", "game": "게임전공", "cs": "컴퓨터과학전공", "ani": "애니메이션전공", "elec": "전기공학전공",
		"eloc": "융합전자공학전공", "bio": "생명공학전공", "cee": "화학에너지공학전공", "ich": "화공신소재전공", "food": "식품영양학전공",
		"clot": "의류학전공", "smpe": "스포츠건강관리전공", "dan": "무용예술전공", "fine": "조형예술전공", "lad": "생활예술전공",
		"mus": "음악학부", "his": "역사콘텐츠전공", "cc": "지적재산권전공", "lib": "문헌정보학전공", "spa": "공간환경학부",
		"pub": "공공인재학부", "fam": "가족복지학과", "sdms": "국가안보학과", "koed": "국어교육과", "ened": "영어교육과",
		"peda": "교육학과", "maed": "수학교육"
	};

	var target = document.getElementById("major");
	var selected = null;

	// code from https://imivory.tistory.com/9
	switch (select.value) {
		case "KAU":
			selected = kau;
			break;
		case "SMU":
			selected = smu;
			break;
		default:
			break;
	}
	
	target.options.length = 0;
	
	for (major in selected) {
		var option = document.createElement("option");
		option.value = major;
		option.innerHTML = selected[major];

		target.appendChild(option);
	}
}