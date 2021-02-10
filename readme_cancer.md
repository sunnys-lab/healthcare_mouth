# 102021 구강계질환 의료영상 AI 경진대회

`poster`

## 1. 개요

* 구강 내시경 사진 내 악성 병변 존재 여부 탐지

![](https://raw.githubusercontent.com/mnc-challenge/healthcare_mouth/main/img/%EA%B5%AC%EA%B0%95_01.png)

## 2. 데이터 상세

### 데이터 셋 별 이미지 수량

| 데이터 셋    | 건수  | 비율(%) |
| ------------ | ----- | ------- |
| Train        | 4,457 | 80.0    |
| Test_public  | 558   | 10.0    |
| Test_private | 559   | 10.0    |
| 합계         | 5,574 | 100     |

* public / private 구분 기준 비공개
* 

### class 

* 라벨링 규칙
  * 라벨은 악성(Cancer, C) 양성(Benign, B), 정상(Normal, N)으로 파일명에 표기
  * 참가자가 직접 악성과 비악성으로 이진화하여 모델 개발에 사용 (암=1, 양성&정상=0)
* 이미지 파일명 규칙
* 환자ID: 기관코드(A-F) + 기관별 환자번호
* 해부학적 부위: 촬영 부위의 해부학적 위치 
  * T: Tongue, P: Palate, B: Buccal mucosa, O: Others
* **진단라벨**: N: Normal / B: Benign / C: Cancer 
  * A5_28_P_N.jpg, F2_5437_T_C.jpg.
  * 단, 테스트셋은 F2_5438_X_X.jpg

### Label

* 제출 파일 양식(csv)

```
filename,pred
A1_1_X_X.jpg,0.065604867
A1_8_X_X.jpg,0.937117042
```




## 3 디렉토리 구조

```bash
\_DATA								: 데이터 폴더
	\_CANCER						: 구강암 데이터 폴더
		\_TRAIN						: 구강암 학습 데이터 폴더
		\_TEST						: 구강암 테스트 데이터 폴더
	\_TEETH							: 치아 데이터 폴더
		* train_label.json			: 치아 학습 라벨 폴더
		\_TRAIN						: 치아 학습 데이터 폴더
		\_TEST						: 치아 테스트 데이터 폴더 
\_USER								: 참가자 사용 폴더
	\_USER_WORKSPACE				: 참가자 작업 폴더
	\_INFERENCE						: 최종 결과물 폴더
		\_TEETH						: 치아 최종 결과물 폴더(구강암 디렉토리와 구조 동일)
		\_CANCER					: 구강암 최종 결과물 폴더
			* train.sh				: train.py 실행 스크립트(arguments 포함)
			* inference.sh			: inference.py 실행 스크립트(arguments 포함)
			* train.py				: 학습 스크립트
			* infernce.py			: 추론 스크립트
			* readme.txt			: 스크립트 설명 파일
			\_results				: 결과 폴더
				* result.json(csv)	: 결과 파일
			\_src					: train.py, infernece.py 참조 스크립트
			\_weights				: 모델(가중치) 폴더
```

**주의사항(필독)**

* 대회 시작 전 아래 주의 사항을 숙지하시기 바랍니다

1. 디렉토리 구조 유지

   * 위 디렉토리 구조를 유지하면서 작업 진행해주시기 바랍니다.
   * <span style="color:red">**/USER_WORKSPACE, /src, /weights 에서만 하위 디렉토리 생성하셔서 작업하시기 바랍니다.**</span>
   * 디렉토리 이슈로 재현성 검증 실패 시 탈락 사유가 될 수 있으니 유의하시기 바랍니다.

2. 최종 결과물 저장 형식

   * 최종 결과물은 INFERENCE/{대회명}/ 아래 디렉토리 구조를 유지하면서 저장해 주시기 바랍니다.

   * train.sh , inference.sh

     * train.py, inference.py 에 arguments 를 넣어 수행할 수 있도록 작성하시기 바랍니다.

       ```shell
       # 예시 train.sh
       python3 train.py --data /DATA/TEETH/TRAIN/ --label /DATA/TEETH/train_label.json --model weights/
       
       # 예시 inference.sh
       python3 inference.py --data /DATA/TEETH/TEST/ --result /results/result.json
       ```

     * <span style="color:red">**재현성 검증 시 train.sh, inference.sh 두 파일만 실행합니다**</span>

       * 스크립트 오류, 재현성 검증 실패 시 탈락 사유가 될 수 있으니 작성에 유의하시기 바랍니다.

   * train.py, inference.py
     * 학습/추론 코드는 **한개 스크립트**에서 수행할 수 있도록 구성하시기 바랍니다.
     * 학습/추론 코드에서 참조(import)하는 모든 스크립트는 /src 내에 저장하시기 바랍니다.
     * 학습/추론 코드에서 불러오는 모든 가중치 파일은 /weights내에 저장하시기 바랍니다.
     * 최종 제출 파일(csv, json)은 results/ 내에 저장하시기 바랍니다

3. 최종 제출 파일(result.json)
   * 리더보드 상 점수에 해당하는 파일을 저장하시기 바랍니다.
   * 재현성 검증 시 해당 파일과 재학습 후 생성한 제출 파일이 리더보드 점수를 재현할 수 있는지 확인 합니다.