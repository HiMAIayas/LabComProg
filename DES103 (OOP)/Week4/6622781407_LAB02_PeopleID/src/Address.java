
public class Address {
	String houseNo="-";
	String soi="-";
	String road="-";
	String subDistrict="-";
	String district="-";
	String province="-";
	String postcode="-";
	
	Address(String houseNo, String Soi, String Road, String subDistrict, 
			String district, String province,String postcode){
		this.houseNo = houseNo;
		this.soi = Soi;
		this.road = Road;
		this.subDistrict = subDistrict;
		this.district = district;
		this.province = province;
		this.postcode = postcode;
	}
	
	Address(String province, String postcode){
		this.province = province;
		this.postcode = postcode;
	}
	
	void printFullAddress() {
		System.out.println(
				houseNo+", "+
				soi+", "+
				road+", "+
				subDistrict+", "+
				district+", "+
				province+", "+
				postcode
		);
	}
	
	void printShortAddress() {
		System.out.println(province+", "+postcode);
	}
	
	
}
