# Project cá nhân: 
**Mục đích**: Xây dựng data set về các đơn vận chuyển (giao hàng), phục vụ việc khai thác thông tin và tìm ra lộ trình giao hàng tối ưu từ nhà cung cấp đến kho trung chuyển, từ kho trung chuyển đến khách hàng: bố trí các đơn hàng vận chuyển sao cho có thể giao hàng đến tay khách hàng vào khoảng thời gian mong muốn, lấy hàng từ các kho đang có hàng tối ưu nhất, khai thác hết năng lực của đội xe, chọn tuyến đường xe được phép đi với chi phí ít nhất, chở được nhiều hàng nhất trên mỗi chặng ...

**Thông tin**: 10000 bản ghi / đối tượng (cần bổ sung chi tiết các thuộc tính cho từng đối tượng tùy thuộc vào bộ dữ liệu, mỗi đối tượng có không dưới 20 thuộc tính): Nhà cung cấp(Warehouse), Kho(Warehouse), Khách hàng(Customer), Hàng(Gooditem), Đơn mua hàng(Order), Đơn giao hàng(DeliveryOrder), Xe(Vehicle), Lộ trình của đội xe(FleetJourney), Lộ trình của từng xe(VehicelJourney), Lộ trình của từng tuyến đường(DeliveryJourney) (từ kho/nhà cung cấp nào, qua các khách nào, quay về kho nào).

**Bước1**: Tìm kiếm các data set hiện có: 10 File dữ liệu khác nhau trên Kaggle.

**Bước2**: Bổ sung, chỉnh sửa, chuẩn hóa, phối ghép về dạng data set đầy đủ các nội dung thông tin như yêu cầu: Dựa trên 10 File đã tìm thấy, chuẩn hóa, phối ghép thành file yêu cầu (Ở mục **Thông tin**).

**Bước3**: phân tích dữ liệu, trực quan hóa theo yêu cầu: 
Với mỗi loại đối tượng, có 1 biểu đồ phân tích và 1 biểu đồ thống kê tự chọn khớp với mục tiêu của đề bài
Ngoài ra, có các biểu đồ sau phục vụ mục đích đặt ra: 
- Biểu đồ hiện thị lượng tồn kho của một mặt hàng cụ thể tại tất cả các kho tại một thời điểm
- Biểu đồ thống kê lượng hàng (hoặc giá trị) nhập / xuất kho tại tất cả các kho trong một giai đoạn
- Biểu đồ thống kê sự có mặt của 1 mặt hàng cụ thể trong các đơn mua hàng trong một giai đoạn
- Biểu đồ thống kê số lượng đơn mua hàng của các khách hàng trong một giai đoạn
- Biểu đồ so sánh tần suất lựa chọn kho để lấy một mặt hàng trong một giai đoạn
- Biểu đồ so sánh tần suất sử dụng các xe của một đội xe trong một giai đoạn
- Biểu đồ so sánh tần suất sử dụng tuyến đường của các xe trong đội xe trong một giai đoạn
- Biểu đồ thể hiện chênh lệch doanh thu từ đơn vân chuyển / chi phí vận chuyển trong một giai đoạn

**Những file có -Wrangling là những File xử lý dữ liệu bằng Python (chuẩn hóa, phối ghép) của đối tượng đó.**
**Những File không có là những File Visualization dữ liệu bằng Python của chính đối tượng đó.**

Ngoài ra em/mình còn thực hiện một bản Report chi tiết về Project này, để có những insight mà em/mình tìm được về project, vui lòng ấn vào link dưới đây:

Google Docs: https://docs.google.com/document/d/1yqVyse-NGpIDU8vGTWmRku0iqsa8eXDxZUQ6HB5BH5s/edit?usp=sharing 

Slide Report: https://www.canva.com/vi_vn/mau/?category=tAExRLg81RI&fFormat=0BR
