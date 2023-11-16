
CÁC VERSION CHƯƠNG TRÌNH:
Python 3.11.5

Angular CLI: 16.2.4
Node: 20.5.1 (Unsupported)
Package Manager: npm 9.8.0
OS: win32 x64

Angular: 16.2.7
... animations, cdk, common, compiler, compiler-cli, core, forms
... material, platform-browser, platform-browser-dynamic, router

Package                         Version
---------------------------------------------------------
@angular-devkit/architect       0.1602.4
@angular-devkit/build-angular   16.2.4
@angular-devkit/core            16.2.4
@angular-devkit/schematics      16.2.4
@angular/cli                    16.2.4
@schematics/angular             16.2.4
rxjs                            7.8.1
typescript                      5.1.6
zone.js                         0.13.3

HƯỚNG DẪN CHẠY CHƯƠNG TRINH:
1. Cấu hình dataBase:
B1: Giải nén thư mục database trong ổ đĩa
B2: Mở MySQL Workbench và kết nối vào MySQL Server của bạn
B3: Trong thanh công cụ, chọn tab "SQL Editor" hoặc "Query" để mở SQL Editor
B4: Trong SQL Editor, chọn File > Open SQL Script từ menu hoặc sử dụng biểu tượng hình thư mục để chọn tệp script SQL của bạn.
B5: Nếu script của bạn chứa lệnh USE your_database_name; để chọn cơ sở dữ liệu, hãy đảm bảo bạn đã chọn cơ sở dữ liệu muốn sử dụng. Bạn có thể chọn cơ sở dữ liệu từ danh sách thả xuống "Selected Schema" ở góc dưới bên phải của cửa sổ.
B6:Sau khi đã mở script và chọn cơ sở dữ liệu (nếu cần), bạn có thể chạy script bằng cách nhấn nút "Execute" (biểu tượng mũi tên xanh lá cây) hoặc sử dụng phím tắt Ctrl + Enter.
B7:Kiểm tra kết quả trong tab "Output" ở phía dưới SQL Editor để xem xét thông báo lỗi hoặc thông báo thành công.

2. Chạy ứng dụng fronend:
B1: Cài Đặt Node.js và npm
B2: Cài Đặt Angular CLI (Command Line Interface)
B3: Di Chuyển Đến Thư Mục Dự Án:______cd frontend\lagu\lagu
B4: Cài Đặt Các Thư Viện và Phụ Thuộc:_____npm install
B5: Chạy Dự Án Angular:________ng serve

3. Chạy chương trình backend:
B1: Cài đặt môi trường
B2: Cấu hình nơi lưu DataBase trong file setting.py
B3: cài đặt file requirements.txt trong chương trình
B4: Di chuyển vào ổ thư mục dự án: cd backend
B5: chạy lệnh: python manage.py runserver






