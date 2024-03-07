# blog_website_jShop
Django를 활용한 쇼핑몰

# blog_website_jStory
Django를 활용한 Blog

# jCloud

Django 활용 페이지 제작 프로젝트

# URL 구조(모놀리식)

### accounts App

| URL                                   | Views Function         |    HTML                         | Note                           |
|---------------------------------------|------------------------|----------------------------------------|--------------------------------|
| '/accounts/login/'                    | login_view             | accounts/login.html                   | 로그인 화면                   |
| '/accounts/logout/'                   | logout_view            |      accounts/logout.html                               | 로그아웃 기능                 |
| '/accounts/signup/'                   | signup_view            | accounts/signup.html                  | 회원가입 화면               |

### profile_index App

| URL                                   | Views Function         | HTML                         | Note                           |
|---------------------------------------|------------------------|----------------------------------------|--------------------------------|
| '/profile_index/'                           | profile_index                | profile_index/profile.html                  | 프로필 화면                   |
| '/profile_content/'                           | profile_content                | profile_content/profile_content.html                  | 프로필 화면                   |

### photos App

| URL                                   | Views Function         | HTML                        | Note                           |
|---------------------------------------|------------------------|----------------------------------------|--------------------------------|
| '/photos/view/'                       | photo_list             | photos/photo_list.html                | 모든 사진 및 비디오 리스트    |
| '/photos/upload/'                     | photo_upload           | photos/photo_upload.html              | 사진 및 비디오 업로드 화면   |
| '/photos/delete/<int:photo_id>/'      | photo_delete           |                                     | 사진 및 비디오 삭제 기능     |

### drive App

| URL                                   | Views Function         | HTML                        | Note                           |
|---------------------------------------|------------------------|----------------------------------------|--------------------------------|
| '/drive/'                             | drive_files            | drive/drive_files.html                 | 드라이브 섹션 파일 리스트      |
| '/drive/upload/'                      | drive_upload           | drive/drive_upload.html                | 파일 업로드 화면             |
| '/drive/delete/<int:file_id>/'        | drive_delete           |                                     | 파일 삭제 기능               |

### notes App

| URL                                   | Views Function         | HTML                        | Note                           |
|---------------------------------------|------------------------|----------------------------------------|--------------------------------|
| '/notes/'                             | note_list              | notes/note_list.html                   | 메모 섹션 메모 리스트        |
| '/notes/create/'                      | note_create            | notes/note_create.html                 | 새로운 메모 작성 화면       |
| '/notes/delete/<int:note_id>/'        | note_delete            |                                     | 메모 삭제 기능               |




# 요구사항 구현

```mermaid
graph TB

subgraph cluster_auth
  A[로그인] -->|로그인 성공| B(메인페이지)
  A -->|회원가입| C(회원가입)
  B --> D{프로필페이지}
  B --> E{사진페이지}
  B --> F{드라이브 페이지}
  B --> G{메모 페이지}
  D -->|프로필 정보| D1(이름, 이메일, 자기소개, 로그아웃)
  D -->|프로필 이미지| D2(프로필 이미지 업로드)
end

subgraph cluster_photos
  E -->|썸네일| E1(사진 썸네일)
  E1 --> H(사진페이지)
  H -->|사진 리스트| H1(모든 사진 리스트)
  H -->|업로드 및 삭제| H2(사진 및 비디오 업로드 및 삭제)
end

subgraph cluster_drive
  F -->|파일 이름| F1(드라이브 섹션 파일 리스트)
  F1 --> I(드라이브 페이지)
  I -->|업로드 및 삭제| I1(다양한 형태의 파일 업로드 및 삭제)
end

subgraph cluster_notes
  G -->|메모 제목| G1(메모 섹션 메모 리스트)
  G1 --> J(메모 페이지)
  J -->|작성 및 삭제| J1(새로운 메모 작성 및 메모 삭제)
end

```

# DB 구성

```mermaid
erDiagram
  USER {
    id INT
    username VARCHAR
    email VARCHAR
    password VARCHAR
  }

  PROFILE {
    id INT
    user_id INT
    name VARCHAR
    bio TEXT
    profile_image VARCHAR
  }

  PHOTO {
    id INT
    user_id INT
    thumbnail VARCHAR
    image VARCHAR
    upload_date DATE
  }

  DRIVE_FILE {
    id INT
    user_id INT
    filename VARCHAR
    file_type VARCHAR
    upload_date DATE
  }

  NOTE {
    id INT
    user_id INT
    title VARCHAR
    content TEXT
    create_date DATE
  }

  USER ||--o{ PROFILE : Has
  USER ||--o{ PHOTO : Has
  USER ||--o{ DRIVE_FILE : Has
  USER ||--o{ NOTE : Has

```