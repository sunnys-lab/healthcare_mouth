# 2021 구강계질환 의료영상 AI 경진대회

`poster`

## 1. 개요

* 치아 파노라마 사진 내 치아 위치 검출 및 번호 식별

![](G:\공유 드라이브\MNC Shared\Project\202009-AI 데이터 - 구강\경진대회\git_repository\img\치아_01.png)

## 2. 데이터 상세

### 데이터 셋 별 이미지 수량

| 데이터 셋    | 건수  | 비율(%) |
| ------------ | ----- | ------- |
| Train        | 3,966 | 79.6    |
| Test_public  | 507   | 10.2    |
| Test_private | 507   | 10.2    |
| 합계         | 4,980 | 100     |

* public / private 구분 기준 비공개

### class 분포

* class 별 bounding box 건수
* public/private class 분포 비공개

| Class | Train   | Test_public | Test_private |
| ----- | ------- | ----------- | ------------ |
| 11    | 3,798   |             |              |
| 12    | 3,844   |             |              |
| 13    | 3,900   |             |              |
| 14    | 3,682   |             |              |
| 15    | 3,586   |             |              |
| 16    | 3,452   |             |              |
| 17    | 3,405   |             |              |
| 18    | 1,214   |             |              |
| 21    | 3,803   |             |              |
| 22    | 3,850   |             |              |
| 23    | 3,909   |             |              |
| 24    | 3,700   |             |              |
| 25    | 3,612   |             |              |
| 26    | 3,481   |             |              |
| 27    | 3,446   |             |              |
| 28    | 1,221   |             |              |
| 31    | 3,826   |             |              |
| 32    | 3,844   |             |              |
| 33    | 3,942   |             |              |
| 34    | 3,834   |             |              |
| 35    | 3,696   |             |              |
| 36    | 3,386   |             |              |
| 37    | 3,331   |             |              |
| 38    | 1,582   |             |              |
| 41    | 3,821   |             |              |
| 42    | 3,845   |             |              |
| 43    | 3,934   |             |              |
| 44    | 3,831   |             |              |
| 45    | 3,717   |             |              |
| 46    | 3,399   |             |              |
| 47    | 3,319   |             |              |
| 48    | 1,571   |             |              |
| 합계  | 108,781 |             |              |

### Label

* 라벨 양식

```json
{
	'파일명':[
        {
            'class': 클래스값,
            'box': [x_min, y_min, x_max, y_max],
        }
        ...
    ]
    ,'파일명':{
        ...
    }
        ...
}
```

* 제출 파일 양식

```json
{
	'파일명':[
        {
            'class': 클래스값,
            'box': [x_min, y_min, x_max, y_max],
            'confidence_score': 0.1
        }
        ...
    ]
    ,'파일명':{
        ...
    }
        ...
}
```

* Bounding box 좌표 위치

```
    0,0 ------> x (width)
     |
     |  (x_min,y_min)
     |      *_________
     |      |         |
            |         |
     y      |_________|
  (height)            *
                (x_max,y_max)
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