package homepage;

public class Member {
	private String id;
	private String cname; // 이메일 뒷자리 부분
	private String regDate;
	private String school;
	private String major;
	
	// getter
	public String getId() { return this.id; }
	public String getCname() { return this.cname; }
	public String getEmail() { return this.id + "@" + this.cname; }
	public String getRegDate() { return this.regDate; }
	public String getSchool() { return this.school; }
	public String getMajor() { return this.major; }
	
	// setter
	public void setId(String id) { this.id = id; }
	public void setCname(String cname) { this.cname = cname; }
	public void setRegDate(String regDate) { this.regDate = regDate; }
	public void setSchool(String school) { this.school = school; }
	public void setMajor(String major) { this.major = major; }
}
