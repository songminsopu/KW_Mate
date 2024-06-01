# 두근 두근 팡메이트
 팡메이트 Flask API

## simple match

- url(GET방식) : http://127.0.0.1:5000/match/simple/[std_id]/[menu]
- 요청할 때 보내는 JSON 없음
- 응답 값 :   
{  
    &emsp;"code": 1,  
    &emsp;"matching_list": [  
        &emsp;&emsp;&emsp;{  
            &emsp;&emsp;&emsp;&emsp;"age": 20,  
            &emsp;&emsp;&emsp;&emsp;"blocked_cnt": 0,  
            &emsp;&emsp;&emsp;&emsp;"description": "WXSR",  
            &emsp;&emsp;&emsp;&emsp;"insta": "58R2K7K",  
            &emsp;&emsp;&emsp;&emsp;"kakao": "0WLIOAF",  
            &emsp;&emsp;&emsp;&emsp;"name": "user 43UZ",  
            &emsp;&emsp;&emsp;&emsp;"std_id": "7"  
        &emsp;&emsp;&emsp;},  
        
    &emsp;]  
}  

## block user
- url(POST방식): http://127.0.0.1:5000/match/simple/block/  
- 요청 값 :  
{  
    &emsp;"std_id": "사용자 학번",  
    &emsp;"bu_std_id": "차단할 사람 학번"  
}  
- 응답 값 :
{  
&emsp;"code": 1,  
&emsp;"msg": "차단 완료"  
}  

## 매칭 종료
- url(GET방식): http://127.0.0.1:5000/match/cancel/[std_id]
- 요청할 때 보내는 JSON 없음
- 응답 값:
{  
    &emsp;"code": 1,  
    &emsp;"msg": "매칭 종료"  
}  