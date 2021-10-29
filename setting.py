TICKER = "B8"
INTERVAL = "E8"

STATEMENT_TYPE = {
    "NHOM_1": {
        "DOUBLE_STATEMENT": "A48",
        "CFLOW_TEST": "A15",
        "Lưu chuyển tiền tệ": {"start": None, "length": None, "first_item": None},
        "Cân đối kế toán": {
            "start": 14,
            "length": 122,
            "first_item": "TÀI SẢN NGẮN HẠN",
        },
        "Kết quả Kinh doanh": {
            "start": 14,
            "length": 25,
            "first_item": "Doanh số",
        },
        "Lưu chuyển tiền tệ - Trực tiếp": {
            "start": 14,
            "length": 28,
            "first_item": "Tiền thu từ bán hàng, Cung cấp dịch vụ và DT khác",
        },
        "Lưu chuyển tiền tệ - Gián tiếp": {
            "start": 14,
            "length": 41,
            "first_item": "Lãi trước thuế",
        },
        "Lưu chuyển tiền tệ - Gián tiếp - 2": {
            "start": 47,
            "length": 41,
            "first_item": "Lãi trước thuế",
        },
        "Thuyết minh": {
            "start": 14,
            "length": 157,
            "first_item": "Tiền",
        },
    },
    "NHOM_2": {
        "DOUBLE_STATEMENT": "A79",
        "CFLOW_TEST": "A16",
        "Lưu chuyển tiền tệ": {"start": None, "length": None, "first_item": None},
        "Cân đối kế toán": {
            "start": 14,
            "length": 99,
            "first_item": "TỔNG TÀI SẢN",
        },
        "Kết quả Kinh doanh": {
            "start": 14,
            "length": 25,
            "first_item": "Thu nhập lãi và các khoản thu nhập tương tự",
        },
        "Lưu chuyển tiền tệ - Trực tiếp": {
            "start": 15,
            "length": 58,
            "first_item": "Thu nhập lãi và các khoản thu nhập tương tự nhận được",
        },
        "Lưu chuyển tiền tệ - Gián tiếp": {
            "start": 15,
            "length": 59,
            "first_item": "Lợi nhuận trước thuế",
        },
        "Lưu chuyển tiền tệ - Gián tiếp - 2": {
            "start": 78,
            "length": 59,
            "first_item": "Lợi nhuận trước thuế",
        },
        "Thuyết minh": {
            "start": 14,
            "length": 219,
            "first_item": "Chứng khoán kinh doanh",
        },
    },
    "NHOM_3": {
        "DOUBLE_STATEMENT": "A50",
        "CFLOW_TEST": "A15",
        "Lưu chuyển tiền tệ": {"start": None, "length": None, "first_item": None},
        "Cân đối kế toán": {
            "start": 14,
            "length": 159,
            "first_item": "TÀI SẢN NGẮN HẠN",
        },
        "Kết quả Kinh doanh": {
            "start": 14,
            "length": 80,
            "first_item": "Doanh thu phí bảo hiểm",
        },
        "Lưu chuyển tiền tệ - Trực tiếp": {
            "start": 14,
            "length": 30,
            "first_item": "Tiền thu phí bảo hiểm và thu lãi",
        },
        "Lưu chuyển tiền tệ - Gián tiếp": {
            "start": 14,
            "length": 49,
            "first_item": "Lợi nhuận trước thuế",
        },
        "Lưu chuyển tiền tệ - Gián tiếp - 2": {
            "start": 49,
            "length": 49,
            "first_item": "Lợi nhuận trước thuế",
        },
        "Thuyết minh": {
            "start": 14,
            "length": 303,
            "first_item": "Tiền",
        },
    },
    "NHOM_4": {
        "DOUBLE_STATEMENT": "A120",
        "CFLOW_TEST": "A16",
        "Lưu chuyển tiền tệ": {"start": None, "length": None, "first_item": None},
        "Cân đối kế toán": {
            "start": 14,
            "length": 217,
            "first_item": "TÀI SẢN NGẮN HẠN",
        },
        "Kết quả Kinh doanh": {
            "start": 14,
            "length": 89,
            "first_item": "DOANH THU HOẠT ĐỘNG",
        },
        "Lưu chuyển tiền tệ - Trực tiếp": {
            "start": 15,
            "length": 98,
            "first_item": "Tiền đã chi mua các tài sản tài chính",
        },
        "Lưu chuyển tiền tệ - Gián tiếp": {
            "start": 15,
            "length": 154,
            "first_item": "LỢI NHUẬN TRƯỚC THUẾ",
        },
        "Lưu chuyển tiền tệ - Gián tiếp - 2": {
            "start": 119,
            "length": 154,
            "first_item": "Lợi nhuận trước thuế",
        },
        "Thuyết minh": {
            "start": 14,
            "length": 642,
            "first_item": "CHỨNG KHOÁN LƯU KÝ NIÊM YẾT",
            "DOUBLE_STATEMENT": "A120",
        },
    },
}
