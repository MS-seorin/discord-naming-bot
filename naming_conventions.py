naming_conventions = {
    "JS/TS": {
        "공통규칙": {
            "변수": "영문자 사용, 카멜 케이스(camelCase)",
            "상수": "영어 대문자 사용, 스네이크 케이스(snake_case)",
            "함수": "영문자 사용, 동사로 시작, 카멜 케이스(camelCase)",
            "클래스": "영문자 사용, 대문자로 시작, 파스칼 케이스(PascalCase)",
            "인터페이스": "영어 대문자 사용, 파스칼 케이스(PascalCase)",
            "파일": "영어 소문자 사용, 스네이크 케이스(snake_case)",
            "폴더": "영어 소문자 사용, 스네이크 케이스(snake_case)"
        },
        # 내부 문서 참고
        # https://www.notion.so/makeshop/Naming-Conventions-b2be468f15a34c1c9dce1beaa6f4317b
        "메이크샵": {
            "변수": "영문자 사용, 카멜 케이스(camelCase)",
            "boolean 반환 변수": "영문자 사용, 카멜 케이스(isCamelCase), prefix로 is 사용",
            "컴포넌트": "영문자 사용, 대문자로 시작, 파스칼 케이스(PascalCase), 명사나 명사구 사용",
            "배열": "영문자 사용, 복수형 단어 사용, 카멜 케이스(camelCase)",
            "정규 표현식": "영문자 사용, 카멜 케이스(camelCase), prefix로 r 사용",
            "상수": "영어 대문자 사용, 스네이크 케이스(snake_case)",
            "Props": "영문자 사용, 카멜 케이스(camelCase), prefix로 on 사용",
            "함수": "영문자 사용, 카멜 케이스(camelCase), prefix로 on 사용",
            "Fetch 함수": "영문자 사용, 카멜 케이스(fetchCamelCase), prefix로 method(get/post/put/del) 사용",
            "Custom Hook": "영문자 사용, 카멜 케이스(useCamelCase), prefix로 use 사용",
            "파일": "영문자 사용, 기본 카멜 케이스(camelCase), 컴포넌트가 포함된 경우 파스칼 케이스(PascalCase) 사용",
            "Unit Test 파일": "영문자 사용, 테스트 대상 파일명.test.tsx",
            "폴더": "영문자 사용, 기본 카멜 케이스(camelCase), 컴포넌트가 포함된 경우 파스칼 케이스(PascalCase) 사용"
        }
    },
    
    "PHP": {
        "공통규칙": {
            "변수": "영어 소문자, 스네이크 케이스(snake_case), prefix로 $ 사용",
            "상수": "영어 대문자, 스네이크 케이스(snake_case)",
            "클래스": "영어 대문자로 시작, 카멜 케이스(camelCase)",
            "함수": "영어 소문자, 스네이크 케이스(snake_case)",
            "메소드": "영어 소문자, 스네이크 케이스(snake_case)",
            "파일": "영어 소문자, 스네이크 케이스(snake_case)",
            "폴더": "영어 소문자, 스네이크 케이스(snake_case)"
        },
        # 내부 문서 참고
        # https://www.notion.so/makeshop/_-_-bc40b76551bc4315a3ad56d846dfbc57
        # https://www.notion.so/makeshop/5e04e76f36dc40b6b1756fff95cd72fc
        "메이크샵": {
            "변수": "영어 소문자, 숫자 사용, 글로벌 변수의 경우에만 대문자 사용, 스네이크 케이스(snake_case), prefix로 $ 사용",
            "상수": "영어 대문자, 숫자 사용, 스네이크 케이스(snake_case)",
            "클래스": "영문자만 사용, 단어의 첫 글자는 대문자, 파스칼표기법(PascalCase), 단수 단어로 정의",
            "함수": "영어 소문자, 숫자 사용, 스네이크 케이스(snake_case)",
            "메소드": "영어 소문자, 숫자 사용, 스네이크 케이스(snake_case)",
            "파일": "영어 소문자 및 숫자로 구성, 스네이크 케이스(snake_case), 파일의 확장자는 html로 통일, 확장자 앞에 파일의 성격 표기(예: product.list.html, product.view.html)",
            "폴더": "영어 소문자, 스네이크 케이스(snake_case)"
        }
    },
    
    "DB": {
        "공통규칙": {
            "데이터베이스": "영어 소문자로 구성, 스네이크 케이스(snake_case)",
            "테이블": "영어 소문자로 구성, 스네이크 케이스(snake_case), 복수형 단어 사용",
            "컬럼": "영어 소문자로 구성, 스네이크 케이스(snake_case), 간결하면서 명확한 단어 사용",
            "시간 관련 컬럼": "영어 소문자로 구성, 스네이크 케이스(snake_case), postfix로 _date, _time, _created_at, _updated_at 등을 사용",
            "외래키 컬럼": "참조하는 테이블의 기본 키와 동일한 이름 사용, 참조하는 테이블의 이름을 포함하는 이름 사용"
        },
        # 내부 문서 참고
        # https://www.notion.so/makeshop/b1e6910a318e40129db566b5637a6911?pvs=4
        "메이크샵": {
            "데이터베이스": "영어 소문자로 구성, 언더스코어(_), 하이픈(-) 등을 사용하지 않음",
            "테이블": "영어 소문자로 구성, 단수형 단어 사용, 스네이크 케이스(snake_case), _tb를 postfix로 사용",
            "map 테이블": "영어 소문자로 구성, 단어는 항상 단수 단어, 스네이크 케이스(snake_case), _map_tb를 postfix로 사용",
            "컬럼": "영어 소문자로 구성, 스네이크 케이스(snake_case), 테이블명의 앞글자를 prefix로 사용, 테이블명이 여러 단어로 이루어진 경우에는 각 단어의 앞글자를 prefix로 사용, 최대 3글자 까지만 테이블명의 앞글자를 prefix로 사용",
            "시간 관련 컬럼": "영어 소문자로 구성, 스네이크 케이스(snake_case), 테이블명의 앞글자를 prefix로 사용, 테이블명이 여러 단어로 이루어진 경우에는 각 단어의 앞글자를 prefix로 사용, 최대 3글자 까지만 테이블명의 앞글자를 prefix로 사용, postfix로 _created_at, _updated_at 사용",
            "외래키 컬럼": "영어 소문자로 구성, 스네이크 케이스(snake_case), 참조하는 테이블명에서 _tb 제거, prefix로 현재 테이블명의 앞글자를 사용, postfix로 _id 사용"
        }
    }
}