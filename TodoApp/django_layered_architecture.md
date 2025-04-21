
# Django 계층형 아키텍처 정리

## 🎯 계층형 아키텍처 3계층 개요

| 계층              | 설명 |
|-------------------|------|
| **Presentation Layer** | 사용자 요청/응답 처리 (View, URL) |
| **Business Logic Layer** | 유효성 검사, 비즈니스 로직 처리 |
| **Data Access Layer** | DB 모델 정의 및 데이터 조작 |

---

## 🏗️ Django 프로젝트 아키텍처 구조 & 3계층 매핑

```
📦 TodoApp (프로젝트 루트)
├── manage.py                         # 🔧 프로젝트 실행 스크립트
├── requirements.txt                 # 📦 의존성 명세
│
├── TodoApp/                         # ⚙️ 프로젝트 설정 폴더
│   ├── __init__.py
│   ├── settings.py                  # ⚙️ 프로젝트 설정
│   ├── urls.py                      # 🌐 전체 URL 라우팅
│   └── wsgi.py / asgi.py            # 🖧 서버 인터페이스
│
└── tasks/                           # 🧩 기능 단위 앱
    ├── __init__.py
    ├── admin.py                     # 🧑‍💼 관리자 페이지 등록
    ├── apps.py                      # ⚙️ 앱 설정
    ├── models.py                    # 📦 [Data Layer] 모델 정의
    ├── serializers.py               # 🧪 [Business Layer] 데이터 구조 정의 및 검증
    ├── views.py                     # 🎯 [Presentation Layer] 요청/응답 처리
    ├── urls.py                      # 🌐 [Presentation Layer] URL 라우팅
    ├── dto.py (❌추천 안됨)         # ❗ Swagger용은 serializer로 대체
    ├── migrations/                  # 🧬 DB 마이그레이션 폴더
    │   └── 0001_initial.py
    └── tests.py                     # 🧪 테스트 코드
```

---

## 🧩 계층형 아키텍처 vs Django 구조 매핑 (ASCII 구조)

```
┌────────────────────────────────────────────┐
│           🎨 Presentation Layer            │
│    ─────────────────────────────────────   │
│    |  tasks/views.py                     |  # 사용자 요청 처리
│    |  tasks/urls.py                      |  # 앱 단위 URL 라우팅
│    |  TodoApp/urls.py                    |  # 전체 프로젝트 라우팅
│    ─────────────────────────────────────   │
└────────────────────────────────────────────┘

┌────────────────────────────────────────────┐
│           🧠 Business Logic Layer           │
│    ─────────────────────────────────────   │
│    |  tasks/serializers.py                |  # 데이터 검증 및 구조 정의
│    |  tasks/services.py (선택적)          |  # 비즈니스 로직 별도 분리 시
│    ─────────────────────────────────────   │
└────────────────────────────────────────────┘

┌────────────────────────────────────────────┐
│           🗃️ Data Access Layer              │
│    ─────────────────────────────────────   │
│    |  tasks/models.py                     |  # ORM 기반 DB 모델 정의
│    |  tasks/migrations/                   |  # DB 변경 관리
│    ─────────────────────────────────────   │
└────────────────────────────────────────────┘
```

---

## 💬 알게된 점

>  `views.py`는 단순히 ‘뷰’가 아니라 ‘컨트롤러’ 역할도 한다
