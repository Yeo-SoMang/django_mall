# django로 만든 쇼핑몰 default

  - 사용 기술
    python, rest_framework, sqlite3, decorector
    
  - 구성
    - admin/ : adminsite
    - / : index: 로그인 하지 않았을 시 로그인페이지로 이동
    - register/: 회원가입페이지
    - login/: 로그인페이지
    - logout/: 로그아웃 후 로그인페이지로 이동
    - product/ 상품 리스트를 보여주는 페이지
    - product/<int:pk>/: 상품 디테일페이지를 보여줌. 주문 가능, 로그인하지않았을 시 작동안됨
    - product/create/: 상품 등록페이지, 유저 레벨이 어드민 등급일때만 가능
    - order/: 주문목록
    - order/create: 주문 생성
    - api/product/: api_list
    - api/product/<int:pk>/: api_detail
    
  
